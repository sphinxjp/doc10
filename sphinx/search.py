# -*- coding: utf-8 -*-
"""
    sphinx.search
    ~~~~~~~~~~~~~

    Create a search index for offline search.

    :copyright: Copyright 2007-2010 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""
import re
import cPickle as pickle

from docutils.nodes import comment, Text, NodeVisitor, SkipNode

from sphinx.util import jsdump, rpartition
import search_languages


class _JavaScriptIndex(object):
    """
    The search index as javascript file that calls a function
    on the documentation search object to register the index.
    """

    PREFIX = 'Search.setIndex('
    SUFFIX = ')'

    def dumps(self, data):
        return self.PREFIX + jsdump.dumps(data) + self.SUFFIX

    def loads(self, s):
        data = s[len(self.PREFIX):-len(self.SUFFIX)]
        if not data or not s.startswith(self.PREFIX) or not \
           s.endswith(self.SUFFIX):
            raise ValueError('invalid data')
        return jsdump.loads(data)

    def dump(self, data, f):
        f.write(self.dumps(data))

    def load(self, f):
        return self.loads(f.read())


js_index = _JavaScriptIndex()


class WordCollector(NodeVisitor):
    """
    A special visitor that collects words for the `IndexBuilder`.
    """

    def __init__(self, document, splitter):
        NodeVisitor.__init__(self, document)
        self.found_words = []
        self.splitter = splitter

    def dispatch_visit(self, node):
        if node.__class__ is comment:
            raise SkipNode
        if node.__class__ is Text:
            self.found_words.extend(self.splitter.split(node.astext()))


class IndexBuilder(object):
    """
    Helper class that creates a searchindex based on the doctrees
    passed to the `feed` method.
    """
    formats = {
        'jsdump':   jsdump,
        'pickle':   pickle
    }

    def __init__(self, env):
        self.env = env
        # filename -> title
        self._titles = {}
        # stemmed word -> set(filenames)
        self._mapping = {}
        # objtype -> index
        self._objtypes = {}
        # objtype index -> objname (localized)
        self._objnames = {}
        # support attribute for search index creation 
        self.lang = search_languages.get(env.config.html_search_language)
        self._stemmer = self.lang.Stemmer()
        self.splitter = self.lang.Splitter(
            env.config.html_search_language_option)

    def load(self, stream, format):
        """Reconstruct from frozen data."""
        if isinstance(format, basestring):
            format = self.formats[format]
        frozen = format.load(stream)
        # if an old index is present, we treat it as not existing.
        if not isinstance(frozen, dict):
            raise ValueError('old format')
        index2fn = frozen['filenames']
        self._titles = dict(zip(index2fn, frozen['titles']))
        self._mapping = {}
        for k, v in frozen['terms'].iteritems():
            if isinstance(v, int):
                self._mapping[k] = set([index2fn[v]])
            else:
                self._mapping[k] = set(index2fn[i] for i in v)
        # no need to load keywords/objtypes

    def dump(self, stream, format):
        """Dump the frozen index to a stream."""
        if isinstance(format, basestring):
            format = self.formats[format]
        format.dump(self.freeze(), stream)

    def get_objects(self, fn2index):
        rv = {}
        otypes = self._objtypes
        onames = self._objnames
        for domainname, domain in self.env.domains.iteritems():
            for fullname, dispname, type, docname, anchor, prio in \
                    domain.get_objects():
                # XXX use dispname?
                if docname not in fn2index:
                    continue
                if prio < 0:
                    continue
                # XXX splitting at dot is kind of Python specific
                prefix, name = rpartition(fullname, '.')
                pdict = rv.setdefault(prefix, {})
                try:
                    i = otypes[domainname, type]
                except KeyError:
                    i = len(otypes)
                    otypes[domainname, type] = i
                    otype = domain.object_types.get(type)
                    if otype:
                        # use unicode() to fire translation proxies
                        onames[i] = unicode(domain.get_type_name(otype))
                    else:
                        onames[i] = type
                pdict[name] = (fn2index[docname], i, prio)
        return rv

    def get_terms(self, fn2index):
        rv = {}
        for k, v in self._mapping.iteritems():
            if len(v) == 1:
                fn, = v
                if fn in fn2index:
                    rv[k] = fn2index[fn]
            else:
                rv[k] = [fn2index[fn] for fn in v if fn in fn2index]
        return rv

    def freeze(self):
        """Create a usable data structure for serializing."""
        filenames = self._titles.keys()
        titles = self._titles.values()
        fn2index = dict((f, i) for (i, f) in enumerate(filenames))
        terms = self.get_terms(fn2index)
        objects = self.get_objects(fn2index)  # populates _objtypes
        objtypes = dict((v, k[0] + ':' + k[1])
                        for (k, v) in self._objtypes.iteritems())
        objnames = self._objnames
        return dict(filenames=filenames, titles=titles, terms=terms,
                    objects=objects, objtypes=objtypes, objnames=objnames)

    def prune(self, filenames):
        """Remove data for all filenames not in the list."""
        new_titles = {}
        for filename in filenames:
            if filename in self._titles:
                new_titles[filename] = self._titles[filename]
        self._titles = new_titles
        for wordnames in self._mapping.itervalues():
            wordnames.intersection_update(filenames)

    def feed(self, filename, title, doctree):
        """Feed a doctree to the index."""
        self._titles[filename] = title

        visitor = WordCollector(doctree, self.splitter)
        doctree.walk(visitor)

        def add_term(word, stem=self._stemmer.stem):
            word = stem(word)
            if len(word) < 3 or word in self.lang.stopwords or word.isdigit():
                return
            self._mapping.setdefault(word, set()).add(filename)

        for word in self.splitter.split(title):
            add_term(word)

        for word in visitor.found_words:
            add_term(word)

    def globalcontext_for_searchtool(self):
        ctx = {'search_langauge_stemming_code': self.lang.js_stemmer_code}
        stopwords = ", ".join(["'%s'" % word for word in self.lang.stopwords])
        ctx['search_language_stop_words'] = "[%s]" % stopwords
        return ctx


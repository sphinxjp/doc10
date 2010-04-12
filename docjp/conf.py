# -*- coding: utf-8 -*-
#
# Sphinx documentation build configuration file

import re
import sphinx

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo',
              'sphinx.ext.autosummary', 'sphinx.ext.extlinks', 'rst2pdf.pdfbuilder']


# The suffix of source filenames.
#source_suffix = '.rst'

#source_encoding = 'utf-8'

master_doc = 'contents'

exclude_patterns = ['_build']
templates_path = ['_templates']
exclude_patterns = ['_build']

project = 'Sphinx'
copyright = '2007-2010, Georg Brandl, Shibukawa Yoshiki(Japanese)'

version = sphinx.__released__
release = version
show_authors = True

html_theme = 'sphinxdoc'
modindex_common_prefix = ['sphinx.']
html_static_path = ['_static']
html_last_updated_fmt = '%Y, %b %d'
html_index = 'index.html'
html_sidebars = {'index': ['indexsidebar.html', 'searchbox.html']}
html_additional_pages = {'index': 'index.html'}
html_use_opensearch = 'http://sphinx.pocoo.org'

htmlhelp_basename = 'Sphinxdoc'

html_search_language = 'ja'
html_search_language_option = {"type":"mecab",
"libpath":"/opt/local/lib/libmecab.dylib",
"appid":file("appid.txt").read().strip()}

# Epub fields
epub_theme = 'epub'
epub_basename = 'sphinx'
epub_author = 'Georg Brandl'
epub_publisher = 'http://sphinx.pocoo.org/'
epub_scheme = 'url'
epub_identifier = epub_publisher
epub_pre_files = [('index', 'Welcome')]
epub_exclude_files = ['_static/opensearch.xml', '_static/doctools.js',
    '_static/jquery.js', '_static/searchtools.js',
    '_static/basic.css', 'search.html']

latex_documents = [('contents', 'sphinx.tex', 'Sphinx Documentation',
                    'Georg Brandl', 'manual', 1)]
latex_logo = '_static/sphinx.png'
latex_elements = {
    'fontpkg': '\\usepackage{palatino}',
}

autodoc_member_order = 'groupwise'
todo_include_todos = True
extlinks = {'rstref': ('http://docutils.sourceforge.net/docs/ref/rst/'
                       'restructuredtext.html#%s', ''),
            'rstrole': ('http://docutils.sourceforge.net/docs/ref/rst/'
                        'roles.html#%s', ''),
            'rstdir': ('http://docutils.sourceforge.net/docs/ref/rst/'
                       'directives.html#%s', '')}

man_pages = [
    ('contents', 'sphinx-all', 'Sphinx documentation generator system manual',
     'Georg Brandl', 1),
    ('man/sphinx-build', 'sphinx-build', 'Sphinx documentation generator tool',
     '', 1),
    ('man/sphinx-quickstart', 'sphinx-quickstart', 'Sphinx documentation '
     'template generator', '', 1),
]

language = 'ja' 

pdf_documents = [ 
    ('contents', u'sphinx_jp', u'Sphinx Document(JP)', u'Georg Brandl(JP:SHIBUKAWA Yoshiki)'),
]
pdf_stylesheets = ['sphinx','kerning','a4','ja']

# -- Extension interface -------------------------------------------------------

from sphinx import addnodes

dir_sig_re = re.compile(r'\.\. (.+?)::(.*)$')

def parse_directive(env, sig, signode):
    if not sig.startswith('.'):
        dec_sig = '.. %s::' % sig
        signode += addnodes.desc_name(dec_sig, dec_sig)
        return sig
    m = dir_sig_re.match(sig)
    if not m:
        signode += addnodes.desc_name(sig, sig)
        return sig
    name, args = m.groups()
    dec_name = '.. %s::' % name
    signode += addnodes.desc_name(dec_name, dec_name)
    signode += addnodes.desc_addname(args, args)
    return name


def parse_role(env, sig, signode):
    signode += addnodes.desc_name(':%s:' % sig, ':%s:' % sig)
    return sig


event_sig_re = re.compile(r'([a-zA-Z-]+)\s*\((.*)\)')

def parse_event(env, sig, signode):
    m = event_sig_re.match(sig)
    if not m:
        signode += addnodes.desc_name(sig, sig)
        return sig
    name, args = m.groups()
    signode += addnodes.desc_name(name, name)
    plist = addnodes.desc_parameterlist()
    for arg in args.split(','):
        arg = arg.strip()
        plist += addnodes.desc_parameter(arg, arg)
    signode += plist
    return name


def setup(app):
    from sphinx.ext.autodoc import cut_lines
    app.connect('autodoc-process-docstring', cut_lines(4, what=['module']))
#    app.add_description_unit('directive', 'dir', 'pair: %s; directive',
    app.add_description_unit('directive', 'dir', 'pair: %s; ディレクティブ',
                             parse_directive)
#   app.add_description_unit('role', 'role', 'pair: %s; role', parse_role)
    app.add_description_unit('role', 'role', 'pair: %s; ロール', parse_role)
    app.add_description_unit('confval', 'confval',
                             objname='設定値',
                             indextemplate='pair: %s; 設定値')
#                             objname='configuration value',
#                             indextemplate='pair: %s; configuration value')
#    app.add_description_unit('event', 'event', 'pair: %s; event', parse_event)
    app.add_description_unit('event', 'event', 'pair: %s; イベント', parse_event)

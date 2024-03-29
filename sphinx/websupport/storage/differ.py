# -*- coding: utf-8 -*-
"""
    sphinx.websupport.storage.differ
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A differ for creating an HTML representations of proposal diffs

    :copyright: Copyright 2007-2010 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re
from cgi import escape
from difflib import Differ


class CombinedHtmlDiff(object):
    """Create an HTML representation of the differences between two pieces
    of text.
    """
    highlight_regex = re.compile(r'([\+\-\^]+)')

    def make_html(self, source, proposal):
        """Return the HTML representation of the differences between
        `source` and `proposal`.

        :param source: the original text
        :param proposal: the proposed text
        """
        proposal = escape(proposal)

        differ = Differ()
        diff = list(differ.compare(source.splitlines(1),
                                   proposal.splitlines(1)))
        html = []
        line = diff.pop(0)
        next = diff.pop(0)
        while True:
            html.append(self._handle_line(line, next))
            line = next
            try:
                next = diff.pop(0)
            except IndexError:
                html.append(self._handle_line(line))
                break
        return ''.join(html).rstrip()

    def _handle_line(self, line, next=None):
        """Handle an individual line in a diff."""
        prefix = line[0]
        text = line[2:]

        if prefix == ' ':
            return text
        elif prefix == '?':
            return ''

        if next is not None and next[0] == '?':
            tag = 'ins' if prefix == '+' else 'del'
            text = self._highlight_text(text, next, tag)
        css_class = 'prop_added' if prefix == '+' else 'prop_removed'

        return '<span class="%s">%s</span>\n' % (css_class, text.rstrip())

    def _highlight_text(self, text, next, tag):
        """Highlight the specific changes made to a line by adding
        <ins> and <del> tags.
        """
        next = next[2:]
        new_text = []
        start = 0
        for match in self.highlight_regex.finditer(next):
            new_text.append(text[start:match.start()])
            new_text.append('<%s>' % tag)
            new_text.append(text[match.start():match.end()])
            new_text.append('</%s>' % tag)
            start = match.end()
        new_text.append(text[start:])
        return ''.join(new_text)

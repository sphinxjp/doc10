# -*- coding: utf-8 -*-
"""
    sphinx.errors
    ~~~~~~~~~~~~~

    Contains SphinxError and a few subclasses (in an extra module to avoid
    circular import problems).

    :copyright: Copyright 2007-2009 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

class SphinxError(Exception):
    """
    Base class for Sphinx errors that are shown to the user in a nicer
    way than normal exceptions.
    """
    category = 'Sphinx error'


class SphinxWarning(SphinxError):
    """Raised for warnings if warnings are treated as errors."""
    category = 'Warning, treated as error'


class ExtensionError(SphinxError):
    """Raised if something's wrong with the configuration."""
    category = 'Extension error'

    def __init__(self, message, orig_exc=None):
        super(ExtensionError, self).__init__(message)
        self.orig_exc = orig_exc

    def __repr__(self):
        if self.orig_exc:
            return '%s(%r, %r)' % (self.__class__.__name__,
                                   self.message, self.orig_exc)
        return '%s(%r)' % (self.__class__.__name__, self.message)

    def __str__(self):
        parent_str = super(ExtensionError, self).__str__()
        if self.orig_exc:
            return '%s (exception: %s)' % (parent_str, self.orig_exc)
        return parent_str


class ThemeError(SphinxError):
    category = 'Theme error'

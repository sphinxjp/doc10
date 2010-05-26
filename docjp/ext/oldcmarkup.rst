.. :mod:`sphinx.ext.oldcmarkup` -- Compatibility extension for old C markup
   ========================================================================

:mod:`sphinx.ext.oldcmarkup` 古いC言語向けマークアップとの互換性維持
====================================================================

.. module:: sphinx.ext.oldcmarkup
   :synopsis: 以前のC言語ドメインのマークアップを使用できるようにする

.. :synopsis: Allow further use of the pre-domain C markup

.. moduleauthor:: Georg Brandl

.. versionadded:: 1.0


.. This extension is a transition helper for projects that used the old
   (pre-domain) C markup, i.e. the directives like ``cfunction`` and roles like
   ``cfunc``.  Since the introduction of domains, they must be called by their
   fully-qualified name (``c:function`` and ``c:func``, respectively) or, with the
   default domain set to ``c``, by their new name (``function`` and ``func``).
   (See :ref:`c-domain` for the details.)

この拡張機能は、 ``cfunction`` ディレクティブや、 ``cfunc`` ロールなどの古いC言語のマークアップを利用しているプロジェクトの移行を手助けします。ドメインが導入されて、これらは完全修飾名の ``c:function`` や ``c:func`` などの名前にするか、デフォルトのドメインを ``c`` に設定し、新しい名前(``function``, ``func``)を使用するように変更しなければなりません。

.. If you activate this extension, it will register the old names, and you can
   use them like before Sphinx 1.0.  The directives are:

この拡張機能を有効にすると、Sphinx 1.0以前で使用されていた古い名前を登録します。追加されるディレクティブは次の通りです:

- ``cfunction``
- ``cmember``
- ``cmacro``
- ``ctype``
- ``cvar``

.. The roles are:

追加されるロールには次のようなものがあります:

- ``cdata``
- ``cfunc``
- ``cmacro``
- ``ctype``

.. However, it is advised to migrate to the new markup -- this extension is a
   compatibility convenience and will disappear in a future version of Sphinx.

しかし、新しいマークアップへの移行をおすすめします。この拡張機能は互換性の維持のために一時的に追加されたモノで、将来のバージョンのSphinxでは削除されます。


.. :mod:`sphinx.ext.todo` -- Support for todo items

:mod:`sphinx.ext.todo` -- Todoアイテムのサポート
================================================

.. module:: sphinx.ext.todo
   :synopsis: Todoアイテムをドキュメントに挿入できるようにします。

.. :synopsis: Allow inserting todo items into documents.

.. moduleauthor:: Daniel Bültmann

.. versionadded:: 0.5

.. There are two additional directives when using this extension:

この拡張を使用すると、以下の二つのディレクティブが追加されます:

.. directive:: todo

   このディレクティブは :dir:`note` と同じように使用できます。

   このディレクティブの内容は :confval:`todo_include_todos` がtrueの場合だけ表示されます。

   .. Use this directive like, for example, :dir:`note`.

      It will only show up in the output if :confval:`todo_include_todos` is true.

.. directive:: todolist

   このディレクティブは、全ドキュメントのすべてのtodoディレクティブを含むリストで置換されます。
   :confval:`todo_include_todos` がtrueになったときだけ表示されます。

   .. This directive is replaced by a list of all todo directives in the whole
      documentation, if :confval:`todo_include_todos` is true.


.. There is also an additional config value:

この拡張機能によって以下の設定値が追加されます。

.. confval:: todo_include_todos

   もしもこの設定値が\ ``True``\ に設定されると、\ :dir:`todo`\ と\ :dir:`todolist`\ のディレクティブが出力を出すようになります。\ ``False``\ が設定されると何も出力されなくなります。デフォルトは\ ``False``\ です。

   .. If this is ``True``, :dir:`todo` and :dir:`todolist` produce output, else
      they produce nothing.  The default is ``False``.

.. :mod:`sphinx.ext.viewcode` -- Add links to highlighted source code
   ==================================================================

:mod:`sphinx.ext.viewcode` -- ハイライト済みのソースコードへのリンクを追加
============================================================================

..
   .. module:: sphinx.ext.viewcode
      :synopsis: Add links to a highlighted version of the source code.

.. module:: sphinx.ext.viewcode
   :synopsis: ハイライトされたバージョンのソースコードへのリンクを追加
.. moduleauthor:: Georg Brandl

.. versionadded:: 1.0


.. This extension looks at your Python object descriptions (``.. class::``,
   ``.. function::`` etc.) and tries to find the source files where the objects are
   contained.  When found, a separate HTML page will be output for each module with
   a highlighted version of the source code, and a link will be added to all object
   descriptions that leads to the source code of the described object.  A link back
   from the source to the description will also be inserted.

この拡張は、Pythonのオブジェクト説明(``.. class::``, ``.. function::`` など)、そのオブジェクトが含まれるソースコードを探しに行きます。もし見つかれば、それぞれのモジュールごとにハイライトされたソースコードのHTMLページを出力し、すべての説明オブジェクトからのリンクが追加されます。これにより、説明オブジェクトのソースコードを見に行くことができます。また、説明オブジェクトへの逆リンクも挿入されます。

.. There are currently no configuration values for this extension; you just need to
   add ``'sphinx.ext.viewcode'`` to your :confval:`extensions` value for it to work.

動作させるためには、 ``'sphinx.ext.viewcode'`` を :confval:`extensions` に追加する必要がありますが、現在はこの拡張はこれ以外の設定値を持ちません。


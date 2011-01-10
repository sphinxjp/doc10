
.. highlight:: rest

.. :mod:`sphinx.ext.ifconfig` -- Include content based on configuration

:mod:`sphinx.ext.ifconfig` -- 設定にしたがってコンテンツをON/OFFする
====================================================================

.. module:: sphinx.ext.ifconfig
   :synopsis: 設定値にしたがって、ドキュメントのコンテンツをON/OFFする.

..   :synopsis: Include documentation content based on configuration values.

.. This extension is quite simple, and features only one directive:

この拡張はきわめてシンプルです。ディレクティブもひとつだけ追加されます。

.. rst:directive:: ifconfig

   引数として与えられているPythonの式が、プロジェクトの設定ファイルの名前空間の中で評価されたときに、\ ``True``\ となった場合のみ、指定されたコンテンツをドキュメントの中に追加します。 :file:`conf.py` で定義されたすべての変数を使用可能です。

   たとえば、以下のようなディレクティブを書くことができます::
  
      .. ifconfig:: releaselevel in ('alpha', 'beta', 'rc')

         この内容は開発版(alpha, beta, rc)でビルドした場合のみ、ドキュメントの中に展開されます。

   もしも、カスタムの設定値を追加したい場合には、 :file:`conf.py` ファイルの中のsetup関数の中で、
   :func:`~sphinx.application.Sphinx.add_config_value` を使用すると行えます::

      def setup(app):
          app.add_config_value('releaselevel', '', True)

   2つめの引数はデフォルト値です。3つ目のパラメータはこのケースについては常に\ ``True``\ にしてください。このパラメータは、設定値が変更された場合に、ドキュメントを再読み込みするかどうかという動作を選択するのに使用します。

..
   Include content of the directive only if the Python expression given as an
   argument is ``True``, evaluated in the namespace of the project's
   configuration (that is, all registered variables from :file:`conf.py` are
   available).

   For example, one could write ::

      .. ifconfig:: releaselevel in ('alpha', 'beta', 'rc')

         This stuff is only included in the built docs for unstable versions.

   To make a custom config value known to Sphinx, use
   :func:`~sphinx.application.Sphinx.add_config_value` in the setup function in
   :file:`conf.py`, e.g.::

      def setup(app):
          app.add_config_value('releaselevel', '', True)

   The second argument is the default value, the third should always be ``True``
   for such values (it selects if Sphinx re-reads the documents if the value
   changes).

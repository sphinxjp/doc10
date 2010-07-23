.. highlight:: rest

.. :mod:`sphinx.ext.graphviz` -- Add Graphviz graphs

:mod:`sphinx.ext.graphviz` -- Graphvizのグラフを追加
====================================================

.. module:: sphinx.ext.graphviz
   :synopsis: Graphvizのグラフのサポート

.. :synopsis: Support for Graphviz graphs.

.. versionadded:: 0.6

.. This extension allows you to embed `Graphviz <http://graphviz.org/>`_ graphs in
   your documents.

この拡張モジュールを使用すると、 `Graphviz <http://graphviz.org/>`_ のグラフをドキュメント内に埋め込むことができるようになります。

.. It adds these directives:

この拡張モジュールは以下のディレクティブを提供します:


.. rst:directive:: graphviz

   .. Directive to embed graphviz code.  The input code for ``dot`` is given as the
      content.  For example::

   Graphvizのコードをドキュメント内に直接記述するためのディレクティブです。
   ここでコンテンツとして入力された内容は、 ``dot`` コマンドで処理されます。

   サンプル::

      .. graphviz::

         digraph foo {
            "bar" -> "baz";
         }

   .. In HTML output, the code will be rendered to a PNG or SVG image (see
      :confval:`graphviz_output_format`).  In LaTeX output, the code will be
      rendered to an embeddable PDF file.

   HTML出力されるときには、PNGのイメージファイルや、SVGイメージとしてレンダリングされます。
   LaTeX出力時にはこのコードは埋め込み可能なPDFファイルとしてレンダリングされます。
   :confval:`graphviz_output_format` を参照してください。


.. rst:directive:: graph

   .. Directive for embedding a single undirected graph.  The name is given as a
      directive argument, the contents of the graph are the directive content.
      This is a convenience directive to generate ``graph <name> { <content> }``.

   無向グラフをひとつ埋め込むのに使用するディレクティブです。
   グラフの名前はディレクティブ引数として渡します。ディレクティブのコンテンツがそのままグラフ作成に使用されます。
   このディレクティブは ``graph <名前> { <コンテンツ> }`` というグラフを作成するための便利機能です。

   サンプル::

      .. graph:: foo

         "bar" -- "baz";


.. rst:directive:: digraph

   .. Directive for embedding a single directed graph.  The name is given as a
      directive argument, the contents of the graph are the directive content.
      This is a convenience directive to generate ``digraph <name> { <content> }``.

   有向グラフをひとつ埋め込むために使用するディレクティブです。
   グラフの名前はディレクティブ引数として渡します。ディレクティブのコンテンツがそのままグラフ作成に使用されます。
   このディレクティブは ``digraph <名前> { <コンテンツ> }`` というグラフを作成するための便利機能です。
  
   サンプル::

      .. digraph:: foo

         "bar" -> "baz" -> "quux";

.. .. versionadded:: 1.0
      All three directives support an ``alt`` option that determines the image's
      alternate text for HTML output.  If not given, the alternate text defaults to
      the graphviz code.

.. versionadded:: 1.0

   これらの3つのディレクティブのすべてで、 ``alt`` オプションが追加されました。これは、HTML出力時には画像の代替テキストとして使用されます。もし指定しない場合には、デフォルトでgraphvizのコードが代替テキストとして使用されます。

.. There are also these new config values:

専用の設定もいくつか追加されます:

.. confval:: graphviz_dot

   .. The command name with which to invoke ``dot``.  The default is ``'dot'``; you
      may need to set this to a full path if ``dot`` is not in the executable
      search path.

   ``dot`` を呼び出すときに使用するコマンド名です。デフォルトでは ``'dot'`` です。
   もしも ``dot`` コマンドが実行時の検索パスに存在していなくて、フルパスを設定する必要がある場合にはこの設定値を変更してください。

   .. Since this setting is not portable from system to system, it is normally not
      useful to set it in ``conf.py``; rather, giving it on the
      :program:`sphinx-build` command line via the :option:`-D` option should be
      preferable, like this:

   この設定はシステム間では移植可能ではありません。通常の場合は ``conf.py`` で指定してしまうのは便利とはいえないでしょう。 :program:`sphinx-build` コマンドを実行するときに、コマンドラインで :option:`-D` オプションを指定する方が望ましいです::

      sphinx-build -b html -D graphviz_dot=C:\graphviz\bin\dot.exe . _build/html


.. confval:: graphviz_dot_args

   .. Additional command-line arguments to give to dot, as a list.  The default is
      an empty list.  This is the right place to set global graph, node or edge
      attributes via dot's ``-G``, ``-N`` and ``-E`` options.

   ``dot`` コマンドに渡す、追加のコマンドライン引数です。デフォルト値は空のリストです。
   ``-G``, ``-N``, ``-E`` オプションを使用して、ドキュメント内のすべてのGraphvizのグラフの、グラフ、ノード、エッジの属性を変更する場合にはこのオプションを使用してください。

.. confval:: graphviz_output_format

   .. The output format for Graphviz when building HTML files.  This must be either
      ``'png'`` or ``'svg'``; the default is ``'png'``.

   HTMLファイルをビルドするときに、Graphvizが出力するフォーマットを指定します。 ``'png'``,  ``'svg'`` のどちらかを指定します。デフォルトは ``'png'`` です。

   .. .. versionadded:: 1.0
         Previously, output always was PNG.

   .. versionadded:: 1.0
      以前は常にPNGイメージが出力されていました。

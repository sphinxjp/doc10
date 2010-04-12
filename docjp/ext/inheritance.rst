.. highlight:: rest

.. :mod:`sphinx.ext.inheritance_diagram` -- Include inheritance diagrams
   =====================================================================

:mod:`sphinx.ext.inheritance_diagram` -- 継承関係図の追加
===============================================================

.. module:: sphinx.ext.inheritance_diagram
   :synopsis: graphvizを使った、継承関係図のサポート

.. :synopsis: Support for displaying inheritance diagrams via graphviz.

.. versionadded:: 0.6

.. This extension allows you to include inheritance diagrams, rendered via the
   :mod:`Graphviz extension <sphinx.ext.graphviz>`.

この拡張機能を使うと、継承関係図をドキュメントに挿入することができます。図は、 :mod:`Graphviz拡張 <sphinx.ext.graphviz>` を使ってレンダリングされます。

.. It adds this directive:

この拡張機能は次のディレクティブを追加します。

.. directive:: inheritance-diagram

   .. This directive has one or more arguments, each giving a module or class
      name.  Class names can be unqualified; in that case they are taken to exist
      in the currently described module (see :dir:`module`).

   このディレクティブは1つ以上の引数を持ちます。モジュールかクラス名を与えます。現在説明中のモジュールの中であれば(:dir:`module` 参照)、クラス名の名前には完全修飾名以外も使えます。

   .. For each given class, and each class in each given module, the base classes
      are determined.  Then, from all classes and their base classes, a graph is
      generated which is then rendered via the graphviz extension to a directed
      graph.

   与えられたクラス、もしくは与えられたモジュールに含まれるクラスごとに、ベースクラスが決定され、すべてのクラスから、有向性グラフとして、graphviz拡張を利用して図がレンダリングされます。

   .. This directive supports an option called ``parts`` that, if given, must be an
      integer, advising the directive to remove that many parts of module names
      from the displayed names.  (For example, if all your class names start with
      ``lib.``, you can give ``:parts: 1`` to remove that prefix from the displayed
      node names.)

   このディレクティブは ``parts`` というオプションを指定しています。これには整数を指定します。もしこれが与えられると、表示名から、モジュール名にあたる部分が削除されます。例えば、もしすべてのクラスの名前が ``lib.`` で始まっている場合に、 ``:parts: 1`` を指定すると、それぞれの表示名から ``lib.`` という文字が表示されなくなります。

.. New config values are

新しい設定値も追加されます。

.. confval:: inheritance_graph_attrs

   .. A dictionary of graphviz graph attributes for inheritance diagrams.

   継承関係図を出力する際の、graphvizのgraphの属性の辞書です。

   .. For example:

   サンプル::

      inheritance_graph_attrs = dict(rankdir="LR", size='"6.0, 8.0"',
                                     fontsize=14, ratio='compress')


.. confval:: inheritance_node_attrs

   .. A dictionary of graphviz node attributes for inheritance diagrams.

   継承関係図を出力する際の、graphvizのnodeの属性の辞書です。

   .. For example:

   .. サンプル::

      inheritance_node_attrs = dict(shape='ellipse', fontsize=14, height=0.75,
                                    color='dodgerblue1', style='filled')


.. confval:: inheritance_edge_attrs

   .. A dictionary of graphviz edge attributes for inheritance diagrams.

   継承関係図を出力する際の、graphvizのedgeの属性の辞書です。

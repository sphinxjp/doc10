.. Glossary
.. ========

.. _glossary:

用語集
======

.. glossary::

   .. builder
         A class (inheriting from :class:`~sphinx.builders.Builder`) that takes
         parsed documents and performs an action on them.  Normally, builders
         translate the documents to an output format, but it is also possible to
         use the builder builders that e.g. check for broken links in the
         documentation, or build coverage information.
 
         See :ref:`builders` for an overview over Sphinx' built-in builders.

   ビルダー
      :class:`~sphinx.builders.Builder` を継承したクラスで、パースされたドキュメントを受け取り、それに対してアクションをします。通常、ビルダーは他の出力フォーマットへ、ドキュメントを変換しますが、壊れたリンクのチェックを行ったり、情報のカバレッジを計測したり、といった用途にも使用することができます。

      Sphinxの内蔵のビルダーに関しては、 :ref:`builders` のドキュメントを参照してください。

   .. description unit
       The basic building block of Sphinx documentation.  Every "description
       directive" (e.g. :dir:`function` or :dir:`describe`) creates such a unit;
       and most units can be cross-referenced to.

   説明ユニット
      Sphinxドキュメントを構築する、基本構成単位です。すべての "説明用ディレクティブ"(:dir:`function`, :dir:`describe`)はこのユニットを作成します。ほとんどのユニットに対して、クロスリファレンスを行うことができます。

   .. environment
      A structure where information about all documents under the root is saved, and used for cross-referencing.  The environment is pickled after the parsing stage, so that successive runs only need to read and parse new and changed documents.

   環境
      ルート以下のすべてのドキュメントの情報が格納される場所です。この情報はクロスリファレンスを作成する際に利用されます。この環境には、パース段階の後の結果のpickleされたものが入ります。ソースファイルが新規で作成されたり、変更されて、読み込んだりパースしたりする必要がない限りはこの中のデータが更新されることはありません。

   .. source directory
       The directory which, including its subdirectories, contains all source files for one Sphinx project.   

   ソースディレクトリ
      ひとつのSphinxプロジェクトにおいて、すべてのソースファイルを含むディレクトリ。このディレクトリ直下だけではなく、サブディレクトリを使用してソースファイルを分類して入れておくことも可能です。

   .. configuration directory
       The directory containing :file:`conf.py`.  By default, this is the same as the :term:`source directory`, but can be set differently with the **-c** command-line option.

   コンフィグレーションディレクトリ
      :file:`conf.py` を含むディレクトリ。デフォルトでは :term:`ソースディレクトリ` と同じですが、 **-c** コマンドラインオプションを使用することで変更することができます。




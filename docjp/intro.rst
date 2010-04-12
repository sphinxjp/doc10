.. Introduction
.. ============

イントロダクション
==================

.. This is the documentation for the Sphinx documentation builder.  Sphinx is a tool that translates a set of reStructuredText_ source files into various outputformats, automatically producing cross-references, indices etc.  That is, if you have a directory containing a bunch of reST-formatted documents (and possibly subdirectories of docs in there as well), Sphinx can generate a nicely-organized arrangement of HTML files (in some other directory) for easy browsing and navigation.  But from the same source, it can also generate a LaTeX file that you can compile into a PDF version of the documents.

これはSphinxドキュメンテーションビルダーのドキュメントです。Sphinxは一連の reStructuredText_ (以下reST)のソースファイルを様々な出力形式に変換したり、クロスリファレンスやインデックスなどを自動生成するツールです。これは、もしreSTフォーマットのドキュメント群が含まれるディレクトリがあったとしたら、Sphinxはそこから非常によくまとまった配置のHTMLファイル群を生成することができるということを意味しています。サブディレクトリにソースが分かれていても問題はありません。また、結果のHTMLはブラウザで簡単に見たり、ナビゲーションもしっかりしたものになります。それだけではなく、同じソースファイルから、同様にLaTeXファイルも出力することができ、これをコンパイルすることでPDFバージョンのドキュメントも生成することができます。

.. The focus is on hand-written documentation, rather than auto-generated API docs.Though there is limited support for that kind of docs as well (which is intendedto be freely mixed with hand-written content), if you need pure API docs have alook at `Epydoc <http://epydoc.sf.net/>`_, which also understands reST.

このドキュメントでは、自動生成のAPIのドキュメントではなく、手で作成するドキュメンテーションにフォーカスします。そのようなドキュメントのサポートに関してはまだ限定的にはあります(手で作成するコンテンツも自由に追加できるようにする予定)が、もし純粋なAPIドキュメントが必要であれば、 `Epydoc <http://epydoc.sf.net/>`_ をご覧ください。こちらもreSTを解釈することができます。

.. Conversion from other systems
.. -----------------------------

他のシステムからの変換
----------------------

.. This section is intended to collect helpful hints for those wanting to migrate to reStructuredText/Sphinx from other documentation systems.

このセクションでは、他のドキュメントシステムからreStructuredText/Sphinxへの移行を考えている人達へのヒントを集めています。

* Gerard FlanaganはHTMLからreSTに変換するスクリプトを作成しました。スクリプトは `BitBucket <http://bitbucket.org/djerdo/musette/src/tip/musette/html/html2rest.py>`_ 上で見つけることができます。

* 古いPythonのドキュメントをSphinxにコンバートするには、専用のコンバート用のツールを `PythonのSVNリポジトリ <http://svn.python.org/projects/doctools/converter>`_ で見つけることができます。これを使えば、Python-docスタイルのLaTeXのマークアップをSphinx reSTに変換できます。

* Marcin WojdyrはDocbookをreST＋Sphinxマークアップに変換するスクリプトを作成しました。 `Google Code <http://code.google.com/p/db2rst/>`_ にあります。

.. * Gerard Flanagan has written a script to convert pure HTML to reST; it can be found at `BitBucket <http://bitbucket.org/djerdo/musette/src/tip/musette/html/html2rest.py>`_.

.. * For converting the old Python docs to Sphinx, a converter was written which  can be found at `the Python SVN repository  <http://svn.python.org/projects/doctools/converter>`_.  It contains generic  code to convert Python-doc-style LaTeX markup to Sphinx reST.

.. * Marcin Wojdyr has written a script to convert Docbook to reST with Sphinx
     markup; it is at `Google Code <http://code.google.com/p/db2rst/>`_.



.. Prerequisites
.. -------------

前提条件
--------

.. Sphinx needs at least **Python 2.4** to run.  If you like to have source code highlighting support, you must also install the Pygments_ library, which you can do via setuptools' easy_install.  Sphinx should work with docutils version 0.4 or some (not broken) SVN trunk snapshot.

Sphinxの実行には **Python 2.4** よりも新しいバージョンのPythonが必要です。もしもソースコードハイライトのサポートが必要であれば、 Pygments_ ライブラリも一緒にインストールする必要がありますが、 setuptoolsのeasy_installを使用すれば一緒にインストールできます。Sphinxが依存しているコンポーネントとしては、docutilsのバージョン 0.4、もしくはSVNリポジトリのTrunkのスナップショット(壊れていないものに限定)があります。

.. _reStructuredText: http://docutils.sf.net/rst.html
.. _Pygments: http://pygments.org

.. Setting up the documentation sources
.. ------------------------------------

ドキュメントソースのセットアップ
--------------------------------

.. The root directory of a documentation collection is called the :dfn:`source directory`.  Normally, this directory also contains the Sphinx configuration file :file:`conf.py`, but that file can also live in another directory, the :dfn:`configuration directory`.

ドキュメント集のルートディレクトリは :dfn:`ソースディレクトリ` と呼ばれます。通常、このディレクトリには、Sphinxのコンフィグファイルの :file:`conf.py` が含まれますが、違うファイルにあってもかまいません。この場合は、 :file:`conf.py` が含まれるディレクトリを :dfn:`コンフィギュレーションディレクトリ` と呼びます。

.. versionadded:: 0.3
   コンフィギュレーションディレクトリを他のディレクトリに設定できるようになりました。 

..   Support for a different configuration directory.

.. Sphinx comes with a script called :program:`sphinx-quickstart` that sets up a source directory and creates a default :file:`conf.py` from a few questions it asks you.  Just run

Sphinxを使用するには、まずは :program:`sphinx-quickstart` と呼ばれるスクリプトを実行して、いくつかの質問に答えて、ソースディレクトリと、デフォルトの :file:`conf.py` のセットアップを行います。実行するには以下のようにします::

   $ sphinx-quickstart

.. and answer the questions.

そして、質問に回答していきます。


.. Running a build
.. ---------------

ビルドの実行
------------

.. A build is started with the :program:`sphinx-build` script.  It is called like this

ビルドは、 :program:`sphinx-build` スクリプトを起動して行います。以下のように実行します。

     $ sphinx-build -b latex sourcedir builddir

.. where *sourcedir* is the :term:`source directory`, and *builddir* is the directory in which you want to place the built documentation (it must be an existing directory).  The :option:`-b` option selects a builder; in this example Sphinx will build LaTeX files.

**sourcedir** には :term:`ソースディレクトリ` が、 **builddir** にはビルドしたドキュメントを置きたいディレクトリ(存在しているディレクトリでなければいけません)を指定します。 :option:`-b` オプションでビルダーを選択します。このサンプルではSphinxは LaTeXのファイルをビルドします。

The :program:`sphinx-build` script has several more options:

:program:`sphinx-build` スクリプトはこれ以外にもいくつかオプションを持っています:

**-a**

   もしこのオプションが設定されると、すべての出力ファイルを書き出します。デフォルトでは新規に作成されたり、変更のあったソースファイルに関連する出力ファイルだけを出力します。このオプションはすべてのビルダーに適応するわけではありません。

..   If given, always write all output files.  The default is to only write output files for new and changed source files.  (This may not apply to all builders.)

**-E**

   保存されている :term:`環境` を使用しないで、完全に再構築する場合に利用します。環境にはクロスリファレンスの構造を保持しています。デフォルトでは新規に作成されたり、最後に実行してから変更のあったソースファイルだけを読み込んで、パースします。

..   Don't use a saved :term:`environment` (the structure caching all cross-references), but rebuild it completely.  The default is to only read and parse source files that are new or have changed since the last run.

**-t** *タグ*
   *タグ* というタグを定義します。これは、タグが設定されているときにだけ内容を取り込むという、 :dir:`only` ディレクティブと関係があります。

   .. versionadded:: 0.6

.. **-t** *tag*
..   Define the tag *tag*.  This is relevant for :dir:`only` directives that only include their content if this tag is set.

.. **-d** *path*
..   Since Sphinx has to read and parse all source files before it can write an output file, the parsed source files are cached as "doctree pickles". Normally, these files are put in a directory called :file:`.doctrees` under the build directory; with this option you can select a different cache directory (the doctrees can be shared between all builders).

**-d** *パス*
   Sphinxは出力ファイルが書き込むことが可能になる前に、すべてのソースファイルを読み込むため、パースされたソースファイルは "doctree pickles"と呼ばれるディレクトリにキャッシュされます。通常は、これらのファイルはビルドディレクトリの下の :file:`.doctrees` と呼ばれるディレクトリに置かれます。このオプションを指定すると、キャッシュディレクトリを違う場所に設定できます。doctreeはすべてのビルダーで共有されます。

.. **-c** *path*
..   Don't look for the :file:`conf.py` in the source directory, but use the given configuration directory instead.  Note that various other files and paths given by configuration values are expected to be relative to the configuration directory, so they will have to be present at this location too.

**-c** *パス*
   ソースディレクトリ以下の :file:`conf.py` ではなく、オプションで指定されたコンフィグレーションディレクトリ以下の設定ファイルを利用するようにします。ただし、さまざまな他のファイル、パスなど、設定値で与えられたものに関しては、コンフィグレーションディレクトリからの相対パスで探索されることになるため、その状況になってもファイルがきちんと読めるようにしておく必要があります。

   .. versionadded:: 0.3

**-C**
   コンフィグファイルを無視します。設定は ``-D`` オプションを使って指定します。

   .. versionadded:: 0.5

..   Don't look for a configuration file; only take options via the ``-D`` option.



.. **-D** *setting=value*
..   Override a configuration value set in the :file:`conf.py` file.  The value
..   must be a string or dictionary value.  For the latter, supply the setting
..   name and key like this: ``-D latex_elements.docclass=scrartcl``.

**-D** *設定=値*
   :file:`conf.py` に書かれた設定値を上書きで設定します。値は文字列か辞書の値であるひつようがあります。後者の場合には設定名とキーは以下のように設定することができます: ``-D latex_elements.docclass=scartcl``

   .. versionchanged:: 0.6
      値として辞書の値が使えるようになりました。

..      The value can now be a dictionary value.

.. **-A** *name=value*
..    Make the *name* assigned to *value* in the HTML templates.

**-A** *名前=値*
   HTMLテンプレートの中の *名前* を *値* に設定します。

**-N**
   出力に色づけをしないようにします。ただし、Windows上では元々どのような場合にも色を付ける機能は無効になっています。

..   Do not do colored output.  (On Windows, colored output is disabled in any case.)

**-q**
   標準出力に何も出力しないようになります。警告やエラーのみが標準エラー出力に書き出されます。

..    Do not output anything on standard output, only write warnings and errors to standard error.

**-Q**
   標準出力に何も出力しないようになります。警告も抑制されます。エラーのみが標準エラー出力に書き出されます。

..    Do not output anything on standard output, also suppress warnings.  Only errors are written to standard error.

.. **-w** *file*
..   Write warnings (and errors) to the given file, in addition to standard error.

**-w** *ファイル*
   警告とエラーを指定されたファイルに書き出されます。なお、標準エラー出力にも同時に出力されます。

**-W**
   警告をエラーにします。最初の警告でビルドが中断され、 ``sphinx-build`` が終了値1を返すようになります。

..   Turn warnings into errors.  This means that the build stops at the first warning and ``sphinx-build`` exits with exit status 1.

**-P**
   (Sphinx自体のデバッグをする人用) キャッチされない例外がビルド中に発生したら、Pythonデバッガの :mod:`pdb` を実行します。

..   (Useful for debugging only.)  Run the Python debugger, :mod:`pdb`, if an unhandled exception occurs while building.

.. You can also give one or more filenames on the command line after the source and build directories.  Sphinx will then try to build only these output files (and their dependencies).

コマンドラインオプションでソースディレクトリ、ビルドディレクトリに追加して、1つ以上のファイル名を指定することもできます。Sphinxはこれらのファイルと、それに依存するファイル群だけを出力しようとします。
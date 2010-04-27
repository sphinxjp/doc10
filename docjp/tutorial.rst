.. highlight:: rst

.. First Steps with Sphinx
   =======================

Sphinxの最初の一歩
===================

.. This document is meant to give a tutorial-like overview of all common tasks
   while using Sphinx.

このドキュメントでは、チュートリアル形式で、Sphinxを使ってよく行うタスクについての概要を紹介していきます。

.. The green arrows designate "more info" links leading to advanced sections about
   the described task.

緑色の矢印は、説明しているタスクについての発展的な内容がリンク先に掲載されていることを示しています。


.. Setting up the documentation sources
   ------------------------------------

ドキュメントのソースの準備
----------------------------

.. The root directory of a documentation collection is called the :term:`source
   directory`.  This directory also contains the Sphinx configuration file
   :file:`conf.py`, where you can configure all aspects of how Sphinx reads your
   sources and builds your documentation.  [#]_

ドキュメントのソースが含まれているディレクトリのルートは :term:`ソースディレクトリ` と呼ばれます。このディレクトリには、Sphinxの設定ファイル :file:`conf.py` があり、Sphinxがどのようにソースを読み込んで出力するのか、というすべての設定がここに書かれています。 [#]_

.. Sphinx comes with a script called :program:`sphinx-quickstart` that sets up a
   source directory and creates a default :file:`conf.py` with the most useful
   configuration values from a few questions it asks you.  Just run ::

Sphinxの最初の第一歩は :program:`sphinx-quickstart` と呼ばれるプログラムを実行し、ソースディレクトリを作成して、いくつかの質問に答えながら、一般的な設定が既に書かれているデフォルトの :file:`conf.py` を生成するところから始まります。次のようにタイプします::

   $ sphinx-quickstart

.. and answer its questions.  (Be sure to say yes to the "autodoc" extension.)

いくつかの質問が行われます。ここでは最低限"autodoc"拡張に関する質問だけはYESと回答しておいてください。

.. Defining document structure
   ---------------------------

ドキュメント構造の定義
-----------------------

.. Let's assume you've run :program:`sphinx-quickstart`.  It created a source
   directory with :file:`conf.py` and a master document, :file:`index.rst` (if you
   accepted the defaults).  The main function of the :term:`master document` is to
   serve as a welcome page, and to contain the root of the "table of contents tree"
   (or *toctree*).  This is one of the main things that Sphinx adds to
   reStructuredText, a way to connect multiple files to a single hierarchy of
   documents.

もう :program:`sphinx-quickstart` は実行しましたね？ :file:`conf.py` と、マスタードキュメントの :file:`index.rst` (もしデフォルトで作成した場合)が含まれる、ソースディレクトリができています。 :term:`マスタードキュメント` の主な役割は、トップページを提供し、TOCツリー(索引のツリー、もしくは *toctree*)のルートが置かれています。このTOCツリーというのは、SphinxがreStructuredTextに追加した主要な要素の一つで、複数のファイルを単一の階層構造に結びつける役割を持っています。

.. .. sidebar:: reStructuredText directives

   ``toctree`` is a reStructuredText :dfn:`directive`, a very versatile piece of
   markup.  Directives can have arguments, options and content.

   *Arguments* are given directly after the double colon following the
   directive's name.  Each directive decides whether it can have arguments, and
   how many.

   *Options* are given after the arguments, in form of a "field list".  The
   ``maxdepth`` is such an option for the ``toctree`` directive.

   *Content* follows the options or arguments after a blank line.  Each
   directive decides whether to allow content, and what to do with it.

   A common gotcha with directives is that **the first line of the content must
   be indented to the same level as the options are**.

.. sidebar:: reStructuredTextディレクティブ

   ``toctree`` はreStructuredText :dfn:`ディレクティブ` です。ディレクティブというのは、さまざまな用途で使用される、マークアップの要素です。ディレクティブは引数、オプション、コンテンツを持つことができます。

   **引数** はディレクティブ名の末尾の2つのコロンの後ろに書かれます。それぞれのディレクティブごとに、引数を持つか、持つ場合はいくつか、というのが決まっています。

   **オプション** は引数の後ろに、フィールドリストの形式で書かれます。例えば、 ``toctree`` ディレクティブにおいては、 ``maxdepth`` というのがオプションにあたります。

   **コンテンツ** はオプションのや引数から空行を一行空けた、その後の内容になります。ディレクティブごとにコンテンツを書けるかどうか、何を書くのか、というのが決まっています。

   ディレクティブの一般的な書き方は、 **コンテンツの最初の行は、オプションと同じ高さに書く** というものです。


.. The toctree directive initially is empty, and looks like this:

最初に生成されたときは、toctreeディレクティブは次のようになっています::

   .. toctree::
      :maxdepth: 2

.. You add documents listing them in the *content* of the directive:

ディレクティブの **コンテンツ** のところにドキュメントのリストを追加します::

   .. toctree::
      :maxdepth: 2

      intro
      tutorial
      ...

.. This is exactly how the toctree for this documentation looks.  The documents to
   include are given as :term:`document name`\ s, which in short means that you
   leave off the file name extension and use slashes as directory separators.

これは、このドキュメントの目次がどのように見えるのか、というのとまったく同じです。ここに含めるドキュメントは、 :term:`ドキュメント名` を使って追加します。簡単に説明すると、拡張子を取り、ディレクトリの記号にスラッシュ(/)を利用した物です。

.. |more| Read more about :ref:`the toctree directive <toctree-directive>`.

|more| さらに詳しい情報については、 :ref:`toctreeディレクティブ <toctree-directive>` をご覧下さい。

.. You can now create the files you listed in the toctree and add content, and
   their section titles will be inserted (up to the "maxdepth" level) at the place
   where the toctree directive is placed.  Also, Sphinx now knows about the order
   and hierarchy of your documents.  (They may contain ``toctree`` directives
   themselves, which means you can create deeply nested hierarchies if necessary.)

次に、toctreeに追加下ファイルを作成し、内容を書くことができるようになりました。"maxdepth"で指定された階層まで、toctreeディレクティブの書かれた場所に、リストされたドキュメントのセクションタイトルとリンクが挿入され、目次ができあがります。Sphinxはこのディレクティブを通じて、ドキュメントの階層と順番を知ります。子供の文章の中にも ``toctree`` ディレクティブを書くことができるため、必要であれば深い階層構造を作ることもできます。

.. Adding content
   --------------

コンテンツの追加
------------------

.. In Sphinx source files, you can use most features of standard reStructuredText.
   There are also several features added by Sphinx.  For example, you can add
   cross-file references in a portable way (which works for all output types) using
   the :role:`ref` role.

Sphinxのソースファイルの中では、標準のreStructuredTextの機能をほとんどそのまま利用することができます。また、Sphinxによっていくつかの機能が追加されています。例えば、 :rst:role:`ref` を使用した、移植可能（すべての出力形式で動作する)な相互ファイル参照を追加することもできます。


.. For an example, if you are viewing the HTML version you can look at the source
   for this document -- use the "Show Source" link in the sidebar.

例えば、HTMLバージョンの出力を見ているとすると、サイドバーにある"ソースを見る"というリンクを使用すると、ドキュメントのソースを見ることができます。

..
   |more| See :ref:`rst-primer` for a more in-depth introduction to
   reStructuredText and :ref:`sphinxmarkup` for a full list of markup added by
   Sphinx.

|more| reStructuredTextのより詳しい説明については、 :ref:`rst-primer` をご覧下さい。また、Sphinxが追加したマークアップの完全なリストは :ref:`sphinxmarkup` を見ると書かれています。


.. Running the build
   -----------------

ビルドの実行
-------------

.. Now that you have added some files and content, let's make a first build of the
   docs.  A build is started with the :program:`sphinx-build` program, called like
   this:

   $ sphinx-build -b html sourcedir builddir

今、いくつかのファイルとコンテンツを追加したとしましょう。それではドキュメントをビルドしてみましょう。ビルドするには :program:`sphinx-build` プログラムを使用します。次のように実行します::

   $ sphinx-build -b html ソースディレクトリ ビルドディレクトリ

.. where *sourcedir* is the :term:`source directory`, and *builddir* is the
   directory in which you want to place the built documentation.  The :option:`-b`
   option selects a builder; in this example Sphinx will build HTML files.

**ソースディレクトリ** は :term:`ソースディレクトリ` を、 **ビルドディレクトリ** はビルドされたドキュメントが置かれるディレクトリを意味します。 :option:`-b` オプションを使用すると、ビルダーを選択することができます。このサンプルではHTMLファイルを出力するビルダーを選択しています。
   
.. 
   |more| See :ref:`invocation` for all options that :program:`sphinx-build`
   supports.

|more| :program:`sphinx-build` がサポートする完全なオプションは、 :ref:`invocation` を参照してください。

.. However, :program:`sphinx-quickstart` script creates a :file:`Makefile` and a
   :file:`make.bat` which make life even easier for you:  with them you only need
   to run :

しかし、 :program:`sphinx-quickstart` スクリプトは :file:`Makefile` と :file:`make.bat` を生成するため、作業はもっと簡単です。次のように実行するだけで、選択したビルドディレクトリの中にHTMLをビルドすることができます::

   $ make html

.. to build HTML docs in the build directory you chose.  Execute ``make`` without
   an argument to see which targets are available.

選択できるターゲットを見るためには、オプションを指定しないで ``make`` を実行してみてください。


.. Documenting objects
   -------------------

オブジェクトのドキュメントを書く
---------------------------------

.. One of Sphinx' main objectives is easy documentation of :dfn:`objects` (in a
   very general sense) in any :dfn:`domain`.  A domain is a collection of object
   types that belong together, complete with markup to create and reference
   descriptions of these objects.

Sphinxの主な目的にの一つが、簡単に :dfn:`ドメイン` に属する :dfn:`オブジェクト` (非常に一般的な意味です)のドキュメントを書けるようにする、というものです。ドメインというのはお互いに関連する、オブジェクトの型を集めた物です。オブジェクトの説明を作成したり、参照したりすることができます。

.. The most prominent domain is the Python domain.  To e.g. document the Python
   built-in function ``enumerate()``, you would add this to one of your source
   files:

   .. py:function:: enumerate(sequence[, start=0])

      Return an iterator that yields tuples of an index and an item of the
      *sequence*. (And so on.)

もっとも使用されるドメインは、Pythonドメインです。Pythonの組み込み関数の ``enumerate()`` のドキュメントを書く場合には、作成しているソースに次のように書き加えます::

   .. py:function:: enumerate(sequence[, start=0])

      *sequence* の要素と、そのインデックスのタプルを生成するイテレータを返します(....など)

.. This is rendered like this:

   .. py:function:: enumerate(sequence[, start=0])

      Return an iterator that yields tuples of an index and an item of the
      *sequence*. (And so on.)

これは次のようにレンダリングされます:

   .. py:function:: enumerate(sequence[, start=0])

      *sequence* の要素と、そのインデックスのタプルを生成するイテレータを返します(....など)

.. The argument of the directive is the :dfn:`signature` of the object you
   describe, the content is the documentation for it.  Multiple signatures can be
   given, each in its own line.

ディレクティブの引数は、説明したいオブジェクトの :dfn:`signature` です。コンテンツには、それに対するドキュメントそのものを書きます。複数のシグネチャを、1行ごとに書くこともできます。

.. The Python domain also happens to be the default domain, so you don't need to
   prefix the markup with the domain name:

   .. function:: enumerate(sequence[, start=0])

      ...

Pythonドメインはデフォルトのドメインとなるので、次のようにドメインを指定するプリフィックスを付けずに書くこともできます::

   .. function:: enumerate(sequence[, start=0])

      ...

.. does the same job if you keep the default setting for the default domain.

   There are several more directives for documenting other types of Python objects,
   for example :dir:`py:class` or :dir:`py:method`.  There is also a
   cross-referencing :dfn:`role` for each of these object types.  This markup will
   create a link to the documentation of ``enumerate()``::

      The :py:func:`enumerate` function can be used for ...

.. And here is the proof: A link to :func:`enumerate`.

.. Again, the ``py:`` can be left out if the Python domain is the default one.  It
   doesn't matter which file contains the actual documentation for ``enumerate()``;
   Sphinx will find it and create a link to it.

.. Each domain will have special rules for how the signatures can look like, and
   make the formatted output look pretty, or add specific features like links to
   parameter types, e.g. in the C/C++ domains.

.. |more| See :ref:`domains` for all the available domains and their
   directives/roles.

.. Basic configuration
   -------------------

基本設定
---------

.. Earlier we mentioned that the :file:`conf.py` file controls how Sphinx processes
   your documents.  In that file, which is executed as a Python source file, you
   assign configuration values.  For advanced users: since it is executed by
   Sphinx, you can do non-trivial tasks in it, like extending :data:`sys.path` or
   importing a module to find out the version your are documenting.

.. The config values that you probably want to change are already put into the
   :file:`conf.py` by :program:`sphinx-quickstart` and initially commented out
   (with standard Python syntax: a ``#`` comments the rest of the line).  To change
   the default value, remove the hash sign and modify the value.  To customize a
   config value that is not automatically added by :program:`sphinx-quickstart`,
   just add an additional assignment.

.. Keep in mind that the file uses Python syntax for strings, numbers, lists and so
   on.  The file is saved in UTF-8 by default, as indicated by the encoding
   declaration in the first line.  If you use non-ASCII characters in any string
   value, you need to use Python Unicode strings (like ``project = u'Expos辿'``).

.. |more| See :ref:`build-config` for documentation of all available config values.


Autodoc
-------

.. When documenting Python code, it is common to put a lot of documentation in the
   source files, in documentation strings.  Sphinx supports the inclusion of
   docstrings from your modules with an :dfn:`extension` (an extension is a Python
   module that provides additional features for Sphinx projects) called "autodoc".

.. In order to use autodoc, you need to activate it in :file:`conf.py` by putting
   the string ``'sphinx.ext.autodoc'`` into the list assigned to the
   :confval:`extensions` config value.  Then, you have a few additional directives
   at your disposal.

.. For example, to document the function ``io.open()``, reading its
   signature and docstring from the source file, you'd write this::

   .. autofunction:: io.open

.. You can also document whole classes or even modules automatically, using member
   options for the auto directives, like ::

   .. automodule:: io
      :members:

.. autodoc needs to import your modules in order to extract the docstrings.
   Therefore, you must add the appropriate path to :py:data:`sys.path` in your
   :file:`conf.py`.

.. 
   |more| See :mod:`sphinx.ext.autodoc` for the complete description of the
   features of autodoc.


.. More topics to be covered
   -------------------------

さらに説明すべきトピック
---------------------------

.. - Other extensions (math, intersphinx, viewcode, doctest)
   - Static files
   - Selecting a theme
   - Templating
   - Using extensions
   - Writing extensions

- 他の拡張機能(math, intersphinx, viewcode, doctest)
- 静的ファイル
- テーマの選択
- テンプレート
- 拡張機能の使用方法
- 拡張機能の書き方

.. 
   .. rubric:: Footnotes

   .. [#] This is the usual lay-out.  However, :file:`conf.py` can also live in
          another directory, the :term:`configuration directory`.  See
          :ref:`invocation`.

.. rubric:: 脚注
.. [#] これは基本的なレイアウトです。しかし、 :file:`conf.py` を :term:`設定ディレクトリ` と呼ばれる他の場所に置くこともできます。詳しくは :ref:`invocation` をご覧下さい。

.. 
   |more| image:: more.png
          :align: middle
          :alt: more info

.. |more| image:: more.png
       :align: middle
       :alt: 詳細情報
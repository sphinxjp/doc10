.. highlight:: rst

.. The TOC tree
   ============

.. _toctree-directive:

TOCツリー
=========

.. .. index:: pair: table of; contents

.. index:: single; 目次

.. Since reST does not have facilities to interconnect several documents, or split
   documents into multiple output files, Sphinx uses a custom directive to add
   relations between the single files the documentation is made of, as well as
   tables of contents.  The ``toctree`` directive is the central element.

ReSTにはドキュメント間の連携をサポートする機能はありませんし、結果のドキュメントを複数の出力ファイルに出すこともできません。 Sphinxは、目次など、ドキュメントを構成するファイル群の関係を追加するカスタムディレクティブを使用します。 ``toctree`` ディレクティブはその中でも一番中心的なものになります。

.. rst:directive:: toctree

   .. This directive inserts a "TOC tree" at the current location, using the
      individual TOCs (including "sub-TOC trees") of the documents given in the
      directive body. Relative document names (not beginning with slash) are 
      relative to the document the directive occurs in, absolute names are relative
      to the source directory.  A numeric ``maxdepth`` option may be given to 
      indicate the depth of the tree; by default, all levels are included. [#]_

   このディレクティブは"目次のツリー"を現在の場所に挿入します。目次の生成には、ディレクティブ本体で指定された関連ドキュメントの中の個別の目次("サブ目次ツリー"も含む)も使用されます。相対的なドキュメント名(``/`` で始まらない)が指定されると、。 ``maxdepth`` オプションの数値を設定すると、ツリーの深さを設定することができます。デフォルトではすべての階層を含むツリーが作成されます。 [#]_

   .. Consider this example (taken from the Python docs' library reference index):

      .. toctree::
         :maxdepth: 2

         intro
         strings
         datatypes
         numeric
         (many more documents listed here)

   このサンプルを見てください。このサンプルはPythonドキュメントのライブラリリファレンスからの引用です::

      .. toctree::
         :maxdepth: 2

         intro
         strings
         datatypes
         numeric
	 (実際はさらに数多くのドキュメントがリストされています)

   .. This accomplishes two things:

   このディレクティブは二つのことを行っています。

   .. * Tables of contents from all those documents are inserted, with a maximum
        depth of two, that means one nested heading.  ``toctree`` directives in
        those documents are also taken into account.
      * Sphinx knows that the relative order of the documents ``intro``,
        ``strings`` and so forth, and it knows that they are children of the shown
        document, the library index.  From this information it generates "next
        chapter", "previous chapter" and "parent chapter" links.

   * ここで指定されたファイル群(intro, stringsなど)の項目も取り込んで目次を作成しています。最大の深さは2に指定されています。つまり、関連するドキュメントからトップの1階層分の項目を取得してきて目次に挿入しています。指定されたファイルに ``toctree`` ディレクティブがあればそれも利用されます。
   * Sphinxはこのディレクティブから、関連するドキュメントが ``intro``, ``strings`` という順番を持っていて、これらのファイルがライブラリインデックスの子供であるという情報を収集します。これらの情報を使って、"next chapter", "previous chapter", "parent chapter"というリンクが作成されます。

   .. Document titles in the :rst:dir:`toctree` will be automatically read from the
      title of the referenced document. If that isn't what you want, you can
      specify an explicit title and target using a similar syntax to reST
      hyperlinks (and Sphinx's :ref:`cross-referencing syntax <xref-syntax>`). This
      looks like:


       .. toctree::

          intro
          All about strings <strings>
          datatypes

   :rst:dir:`toctree` の中のドキュメントのタイトルは、参照先のドキュメントのタイトル情報を自動的に読み込んで使用します。もしこの動作が望ましくなければ、reSTのハイパーリンクに似た文法(Sphinxの :ref:`cross-referencing syntax <xref-syntax>`)を使って明示的に指定することができます。サンプルを示します::

       .. toctree::

          intro
          文字列のすべて <strings>
          datatypes

   .. The second line above will link to the ``strings`` document, but will use the
      title "All about strings" instead of the title of the ``strings`` document.

   上記のサンプルの2行目は ``strings``ドキュメントへのリンクになります。デフォルトの動作では ``strings`` ドキュメントのタイトルが使用されますが、ここでは"文字列のすべて"という文字列がタイトルとして使用されます。

   .. You can also add external links, by giving an HTTP URL instead of a document
      name.

   また、ドキュメント名の代わりに、HTTPのURLを指定することで外部へのリンクを追加することもできます。

   If you want to have section numbers even in HTML output, give the toctree a
   ``numbered`` flag option.  For example:

   もし、セクション番号をHTML出力に追加したい場合には、 ``numbered`` フラグオプションをtoctreeに追加します::

      .. toctree::
         :numbered:

         foo
         bar

   .. Numbering then starts at the heading of ``foo``.  Sub-toctrees are
      automatically numbered (don't give the ``numbered`` flag to those).

   ナンバリングは ``foo`` の見出しから開始されます。サブの目次のツリーに対しても自動的にナンバリングされています。サブの文章のtoctreeには ``numbered`` フラグが設定されていなくても自動的に処理が行われます。  

   .. If you want only the titles of documents in the tree to show up, not other
      headings of the same level, you can use the ``titlesonly`` option:

   もしもドキュメントのタイトルだけをツリーに表示して、同じレベルの他の見出しを表示したくない場合には、 ``titlesonly`` オプションを使用します::

      .. toctree::
         :titlesonly:

         foo
         bar

   .. You can use "globbing" in toctree directives, by giving the ``glob`` flag
      option.  All entries are then matched against the list of available
      documents, and matches are inserted into the list alphabetically.  Example:

   toctreeディレクティブでは、 ``glob`` フラグオプションを指定することで、"GLOB"というものを使用することもできます。使用可能なドキュメントのうち、マッチするエントリーをすべて、アルファベット順に挿入します::

      .. toctree::
         :glob:

         intro*
         recipe/*
         *

   .. This includes first all documents whose names start with ``intro``, then all
      documents in the ``recipe`` folder, then all remaining documents (except the
      one containing the directive, of course.) [#]_

   このディレクティブの先頭では、名前が ``intro`` で始まるすべてのドキュメントが挿入されます。その次には、 ``recipe`` フォルダの中の全てのドキュメントが挿入されます。最後に、一度も挿入されていない、残ったドキュメントが挿入されます。 [#]_

   .. The special entry name ``self`` stands for the document containing the
      toctree directive.  This is useful if you want to generate a "sitemap" from
      the toctree.

   ``self`` は特別なエントリー名として扱われます。toctreeディレクティブを含むドキュメント自身を表します。これは、toctreeを使用して、"サイトマップ"を作成したい場合に便利です。

   .. You can also give a "hidden" option to the directive, like this:

   ``hidden`` オプションというものをディレクティブに設定することもできます::

      .. toctree::
         :hidden:

         doc_1
         doc_2

   .. This will still notify Sphinx of the document hierarchy, but not insert links
      into the document at the location of the directive -- this makes sense if you
      intend to insert these links yourself, in a different style, or in the HTML
      sidebar.

   このtoctreeのサンプルは、ドキュメントの階層構造をSphinxに教えますが、このディレクティブがある場所にはドキュメントのリンクは作成されません。これにより、違う形式で出力したり、サイドバーに入れたり、これらのリンクを自分で挿入したい場合にも、きちんとした構造を作ることができます。

   .. In the end, all documents in the :term:`source directory` (or subdirectories)
      must occur in some ``toctree`` directive; Sphinx will emit a warning if it
      finds a file that is not included, because that means that this file will not
      be reachable through standard navigation.  Use :confval:`unused_docs` to
      explicitly exclude documents from building, and :confval:`exclude_trees` to
      exclude whole directories.

   最後になりますが :term:`ソースディレクトリ` (サブディレクトリも含む)の中のドキュメントは、いずれかの ``toctree`` ディレクティブの中にリストアップされなければいけません。ソースフォルダには置いてあるが、リストアップされていないファイルがあると、通常のナビゲーションではそのファイルに到達できないということになるため、Sphinxは警告を出力します。 :confval:`unused_documents` を使って明示することで、ビルド対象からドキュメントを外すこともできます。また、 :confval:`exclude_dirs` を使うと、ディレクトリごと対象から外すこともできます。

   .. The "master document" (selected by :confval:`master_doc`) is the "root" of
      the TOC tree hierarchy.  It can be used as the documentation's main page, or
      as a "full table of contents" if you don't give a ``maxdepth`` option.

   "マスタードキュメント" (:confval:`master_doc` で指定します)はTOCツリー階層の"ルート"のドキュメントになります。これはドキュメントのメインページとして使うことができます。あるいは、``maxdepth``オプションを指定しない、完全な目次を作成することもできます。

   .. .. versionchanged:: 0.3
         Added "globbing" option.

   .. versionchanged:: 0.3
      "glob"オプションが追加されました

   .. .. versionchanged:: 0.6
         Added "numbered" and "hidden" options as well as external links and
         support for "self" references.

   .. versionchanged:: 0.6
      "numbered"と"hidden"オプション、外部リンクのサポート、"self"参照が追加されました。

   .. .. versionchanged:: 1.0
         Added "titlesonly" option.

   .. versionchanged:: 1.0
      "titlesonly" オプションが追加されました。


.. Special names
   -------------

特別なドキュメント名
--------------------

.. Sphinx reserves some document names for its own use; you should not try to
   create documents with these names -- it will cause problems.

Sphinxはいくつかのドキュメント名を、自分で使用するために予約済みとしています。これらの名前を持つドキュメントを作ろうとしてはいけません。問題が発生することになります。

.. The special document names (and pages generated for them) are:

以下の名前(もしくはこれらから作られるページ名)が特別なドキュメント名です:

.. * ``genindex``, ``modindex``, ``search``

     These are used for the general index, the Python module index, and the search
     page, respectively.

     The general index is populated with entries from modules, all index-generating
     :ref:`object descriptions <basic-domain-markup>`, and from :rst:dir:`index`
     directives.

     The module index contains one entry per :rst:dir:`module` directive.

     The search page contains a form that uses the generated JSON search index and
     JavaScript to full-text search the generated documents for search words; it
     should work on every major browser that supports modern JavaScript.

* ``genindex``, ``modindex``, ``search``

  これらの名前は、それぞれ、全体のインデックス、モジュールインデックス、検索ページを作成するのに使用されます。

  全体のインデックスはモジュールに含まれるのエントリーから作られます。すべてのインデックスを生成する :ref:`オブジェクト説明 <basic-domain-markup>` と、 rst:dir:`index` ディレクティブが利用されます。

  モジュールインデックスには rst:dir:`module` ディレクティブで指定されたエントリーが含まれます。

  検索ページは、ビルドされた文章から生成されたJSONの検索インデックスと、JavaScriptを利用した全文検索を行うフォームを含みます。検索は現代的なJavaScriptをサポートする、主要なブラウザで動作するはずです。

.. * every name beginning with ``_``

     Though only few such names are currently used by Sphinx, you should not create
     documents or document-containing directories with such names.  (Using ``_`` as
     a prefix for a custom template directory is fine.)

* ``_`` で始まるすべての名前

  Sphinx内ではまだそれほど使用されていませんが、このような名前のドキュメントや、ドキュメントを含むディレクトリは作らないでください。 ``_`` をカスタムテンプレートを入れるディレクトリのプリフィックスに使用することはできます。


.. .. rubric:: Footnotes

   .. [#] The ``maxdepth`` option does not apply to the LaTeX writer, where the
          whole table of contents will always be presented at the begin of the
          document, and its depth is controlled by the ``tocdepth`` counter, which
          you can reset in your :confval:`latex_preamble` config value using
          e.g. ``\setcounter{tocdepth}{2}``.

   .. [#] A note on available globbing syntax: you can use the standard shell
          constructs ``*``, ``?``, ``[...]`` and ``[!...]`` with the feature that
          these all don't match slashes.  A double star ``**`` can be used to match
          any sequence of characters *including* slashes.

.. rubric:: 脚注

.. [#] ``maxdepth`` オプションはLaTeXの出力では適用できません。常に、完全な目次がドキュメントの先頭に挿入されます。このときの深さは ``tocdpeth`` カウンタを使って制御することができます。この値をリセットするには :confval:`latex_preamble` コンフィグを使用して、以下のように設定します。 ``\setcounter{tocdepth}{2}``

.. [#] "GLOB"文法に関する追加説明: 標準のシェル構文で使用できる ``*``, ``?``, ``[...]``, ``[!...]`` が使用できます。これらはスラッシュ(/)にはマッチしません。 ``**`` を使用すると、スラッシュ(/)も *含む* すべての文字列に対してマッチします。

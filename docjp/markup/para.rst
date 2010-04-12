.. highlight:: rest

.. Paragraph-level markup
.. ----------------------

パラグラフ階層のマークアップ
----------------------------

.. index:: note, warning
           pair: changes; in version

.. These directives create short paragraphs and can be used inside information units as well as normal text:

これらのディレクティブは短いパラグラフ(段落)を作成します。通常のテキスト同様、情報の固まりに対して使用できます。

.. directive:: note

　 特別に重要な情報が少しだけある場合に使用します。APIを使用する際に、ユーザが気をつけなければならないことの説明をする場合などに使うと良いでしょう。このディレクティブの中身には、適切に句読点が付いた、完全な文章を書くべきです。

   サンプル::

      .. note::
         この関数はspamの電子メールを送付するには適しません。

..   An especially important bit of information about an API that a user should be aware of when using whatever bit of API the note pertains to.  The content of the directive should be written in complete sentences and include all appropriate punctuation

..         This function is not suitable for sending spam e-mails.

.. directive:: warning

   noteよりも重要な情報があり、APIを使用する際に、気をつけなければならない警告情報をユーザに伝えるために使用するのに適しています。このディレクティブの中身には、適切に句読点が付いた、完全な文章を書くべきです。 ``note`` との違いで言えば、セキュリティに関する情報は ``note`` よりもこのディレクティブを使用する方が良いでしょう。

..   An important bit of information about an API that a user should be very aware of when using whatever bit of API the warning pertains to.  The content of the directive should be written in complete sentences and include all appropriate punctuation. This differs from ``note`` in that it is recommended over ``note`` for information regarding security.

.. .. directive:: .. versionadded:: version

..   This directive documents the version of the project which added the described feature to the library or C API. When this applies to an entire module, it should be placed at the top of the module section before any prose.

..   The first argument must be given and is the version in question; you can add a second argument consisting of a *brief* explanation of the change.


..   Example

..      .. versionadded:: 2.5
..         The `spam` parameter.

..   Note that there must be no blank line between the directive head and the explanation; this is to make these blocks visually continuous in the markup.

.. directive:: .. versionadded:: バージョン

   このディレクティブは説明している機能がライブラリ、もしくはC APIに追加された時のプロジェクトのバージョンについて記述するのに使用します。このディレクティブがモジュール全体に対して適用する場合には、モジュールセクションの先頭の、文章が始まる前の位置に置くべきです。

   最初の引数は必須で、バージョン番号を書く必要があります。2番目の引数も追加することができ、変化に対する *短い* 説明を書くことができます。

..   Example

   サンプル::

      .. versionadded:: 2.5
         `spam` パラメータ

   ディレクティブヘッドと説明の間には空行を入れてはいけません。マークアップの中では見た目上つながっているようにしなければなりません。

.. .. directive:: .. versionchanged:: version

..   Similar to ``versionadded``, but describes when and what changed in the named feature in some way (new parameters, changed side effects, etc.).

.. directive:: .. versionchanged:: バージョン

   ``versionadded`` と似ていますが、現在説明している機能がいつどのように変化したのか(新しい引数、副作用の変更など)を説明するのに使用します。

--------------

..   Many sections include a list of references to module documentation or external documents.  These lists are created using the ``seealso`` directive.

..   The ``seealso`` directive is typically placed in a section just before any sub-sections.  For the HTML output, it is shown boxed off from the main flow of the text.

..   The content of the ``seealso`` directive should be a reST definition list.
..   Example

..      .. seealso::

..         Module :mod:`zipfile`
..            Documentation of the :mod:`zipfile` standard module.

..         `GNU tar manual, Basic Tar Format <http://link>`_
..            Documentation for tar archive files, including GNU tar extensions.

..   There's also a "short form" allowed that looks like this::

..      .. seealso:: modules :mod:`zipfile`, :mod:`tarfile`

..   .. versionadded:: 0.5
..      The short form.

.. directive:: seealso

   多くのセクションがモジュールのドキュメントへの参照やが、外部ドキュメントへの参照を含む場合、このようなリストは ``seealso`` ディレクティブを使用して作ることができます。

   ``seealso`` ディレクティブはサブセクションの直前のセクションに置かれることが多いです。HTMLアウトプットにおいては、メインのテキストの流れから離されて、箱に囲まれて表示されます。

   ``seealso`` の中身は、reSTの定義リストを使用しなければなりません。

   サンプル::

      .. seealso::

         Module :mod:`zipfile`
            標準モジュールの :mod:`zipfile` のドキュメント。

         `GNU tar マニュアル, 基本Tarフォーマット <http://link>`_
            GNUによるtar拡張も含む、tarアーカイブファイルのドキュメント。

   "短縮形"の書き方もサポートされており、以下のように書くことができます::

      .. seealso:: modules :mod:`zipfile`, :mod:`tarfile`

   .. versionadded:: 0.5
      短縮形の追加

.. .. directive:: .. rubric:: title

..   This directive creates a paragraph heading that is not used to create a
..   table of contents node.

..   .. note::

..      If the *title* of the rubric is "Footnotes", this rubric is ignored by
..      the LaTeX writer, since it is assumed to only contain footnote
..      definitions and therefore would create an empty heading.

.. directive:: .. rubric:: タイトル

   このディレクティブは、目次に表示されないパラグラフの見出しを作成します。(訳注:rubricは注釈の意味です)

   .. note::

      もし rubricディレクティブの *タイトル* が"Footnotes"だった場合には、脚注の定義だけが含まれていると見なして、LaTeXライターでは無視されます。この場合は空の見出しだけが作成されます。


.. .. directive:: centered

..   This directive creates a centered boldfaced line of text.  Use it as follows::

..      .. centered:: LICENSE AGREEMENT

.. directive:: centered

   このディレクティブはセンターに置かれた、太字のテキストを作成するのに使用します。以下のように使用されます::

      .. centered:: ラインセンス契約


.. directive:: hlist

   このディレクティブは短い文章のリストを含みます。このディレクティブは、水平にも数カラム展開することで、よりコンパクトなリストに変換するか、アイテム間のスペースを小さくします。どちらになるかはビルダー次第です。

   水平に展開する機能をサポートしたビルダーでは、 ``columns`` オプションを使用して、水平のカラム数の設定をすることができます。デフォルトでは2になっています。サンプルを示します::

      .. hlist::
         :columns: 3

         * このリストの
         * 短い項目は
         * 表示するときに
         * 水平に
         * 表示されるべきです。

   .. versionadded:: 0.6

..   This directive must contain a bullet list.  It will transform it into a more compact list by either distributing more than one item horizontally, or reducing spacing between items, depending on the builder.

..   For builders that support the horizontal distribution, there is a ``columns`` option that specifies the number of columns; it defaults to 2.  Example

..         * A list of
..         * short items
..         * that should be
..         * displayed
..         * horizontally


.. Table-of-contents markup
.. ------------------------

目次のマークアップ
------------------

.. The :dir:`toctree` directive, which generates tables of contents of subdocuments, is described in "Sphinx concepts".

サブドキュメントの目次を作る :dir:`toctree` ディレクティブに関しては "Sphinxコンセプト"のドキュメントを読んでください。

.. For local tables of contents, use the standard reST :dir:`contents` directive.

ローカルな目次を作成する場合には、標準reSTの :dir:`contents` ディレクティブを使用してください。

.. Index-generating markup
.. -----------------------

インデックス生成のためのマークアップ
------------------------------------

.. Sphinx automatically creates index entries from all information units (like functions, classes or attributes) like discussed before.

Sphinxはすべての情報のユニット(関数、クラス、属性)から、自動的にインデックスのエントリーを作成します。

.. However, there is also an explicit directive available, to make the index more comprehensive and enable index entries in documents where information is not mainly contained in information units, such as the language reference.

しかし、これ以外に明示的に指定するディレクティブもあります。これを使用することで、言語のリファレンスのように、メインの情報のユニットが存在しない情報をドキュメントの中に書いてインデックスのエントリーを作ることができるようになります。より包括的なインデックスを作成することができるようになります。

.. directive:: .. index:: <エントリー>

   このディレクティブは一つ以上のインデックスのエントリーを含みます。それぞれのエントリーはコロン(:)で区切られた、タイプ、値を含みます。

   サンプル::

      .. index::
         single: execution; context
         module: __main__
         module: sys
         triple: module; search; path

      実行時のコンテキスト
      ---------------------

      ...
   
   このディレクティブは5つのエントリーを含んでいます。これらは生成されたインデックスのエントリーに変換され、index文の正確な位置へのリンクが張られることになります。オフラインのメディアに出力される場合には、リンクの代わりに対応するページ番号が出力されます。

   indexディレクティブはそのソースの位置のターゲットとのクロスリファレンスを生成するため、それらが参照するものの *前の位置* に置くことが大切になります。上記のサンプルコードの例では、リンクを張りたい見出しの前に配置されています。

   設定可能なエントリーのタイプは以下の通りです:

   single
      単体のインデックスのエントリーを作成します。 サブエントリーのテキストとの間をセミコロンで区切ることにより、サブエントリーをサブエントリーを作ることもできます。この記法はどのエントリーが作成されたのか、という説明のところで詳しく説明します。

   pair
      ``pair: loop; statement`` はインデックスエントリーを2つ作成します。
      ``loop; statement`` と ``statement; loop`` の2つのエントリーが作成されます。

   triple
      pairと似ていますが ``triple: module; search; path`` は3つのエントリーを作成します。 ``module; search path``, ``search; path, module``, ``path; module search`` が作成されます。

   module, keyword, operator, object, exception, statement, builtin
      これらはすべて、2つのエントリーを作成します。例えば、 ``module: hashlib`` という項目があると、 ``module; hashlib`` と ``hashlib; module`` の2つのエントリーが作成されます。

   "single"のエントリーだけが含まれるindexディレクティブの場合、以下のように短縮記法で簡単に作成することもできます::

      .. index:: BNF, grammar, syntax, notation

   これは4つのインデックスのエントリーが作成されます。

.. .. directive:: .. index:: <entries>

..   This directive contains one or more index entries.  Each entry consists of a type and a value, separated by a colon.

..   For example

..      .. index
..         single: execution; context
..         module: __main__
..         module: sys
..         triple: module; search; path

..      The execution context
..      ---------------------

..      ...

..   This directive contains five entries, which will be converted to entries in the  generated index which link to the exact location of the index statement (or, in case of offline media, the corresponding page number).

..   Since index directives generate cross-reference targets at their location in the source, it makes sense to put them *before* the thing they refer to -- e.g. a heading, as in the example above.

..   The possible entry types are:

..   single
..      Creates a single index entry.  Can be made a subentry by separating the
..      subentry text with a semicolon (this notation is also used below to describe what entries are created).
..   pair
..      ``pair: loop; statement`` is a shortcut that creates two index entries, namely ``loop; statement`` and ``statement; loop``.
..   triple
..      Likewise, ``triple: module; search; path`` is a shortcut that creates three index entries, which are ``module; search path``, ``search; path, module`` and ``path; module search``.
..   module, keyword, operator, object, exception, statement, builtin
..      These all create two index entries.  For example, ``module: hashlib`` creates the entries ``module; hashlib`` and ``hashlib; module``.

..   For index directives containing only "single" entries, there is a shorthand notation::

..      .. index:: BNF, grammar, syntax, notation

..   This creates four index entries.

.. Glossary
.. --------

用語集

.. directive:: glossary

   このディレクティブは用語と定義がリストになった、reST定義リストを含みます。定義は :role:`term` というロールを利用することで参照が可能になります。以下にサンプルを示します::

      .. glossary::

         環境
            ルート以下のすべてのドキュメントの情報が格納される場所です。この情報はクロスリファレンスを作成する際に利用されます。この環境には、パース段階の後の結果のpickleされたものが入ります。ソースファイルが新規で作成されたり、変更されて、読み込んだりパースしたりする必要がない限りはこの中のデータが更新されることはありません。
   
         ソースディレクトリ
            ひとつのSphinxプロジェクトにおいて、すべてのソースファイルを含むディレクトリ。このディレクトリ直下だけではなく、サブディレクトリを使用してソースファイルを分類して入れておくことも可能です。

   .. versionadded:: 0.6
      glossaryディレクティブに ``:sorted:`` というフラッグを与えることができるようになりました。これを指定すると、自動的にエントリーをアルファベット順に並べることができます。

..   This directive must contain a reST definition list with terms and definitions.  The definitions will then be referencable with the :role:`term` role.  Example::

..      .. glossary::

..         environment
..            A structure where information about all documents under the root is saved, and used for cross-referencing.  The environment is pickled after the parsing stage, so that successive runs only need to read and parse new and changed documents.

..         source directory
..            The directory which, including its subdirectories, contains all source files for one Sphinx project.

..   .. versionadded:: 0.6
..      You can now give the glossary directive a ``:sorted:`` flag that will
..      automatically sort the entries alphabetically.

.. Grammar production displays
.. ---------------------------

文法規則表示
------------

(訳注: grammar productionを文法規則と意訳してます)

.. Special markup is available for displaying the productions of a formal grammar. The markup is simple and does not attempt to model all aspects of BNF (or any derived forms), but provides enough to allow context-free grammars to be displayed in a way that causes uses of a symbol to be rendered as hyperlinks to the definition of the symbol.  There is this directive:

形式がきちんとした文法の規則を表示するための特別なマークアップを利用することができます。マークアップはシンプルに作られています。その代わりに、BNFや、BNFの派生の記法をすべてのモデル化することは目標とされていませんが、文脈自由文法を表現するには十分な機能を持っていて、シンボルを書くと、定義にリンクが張られるようにレンダリングされます。以下のディレクティブがあります:

.. directive:: productionlist

   このディレクティブは文法の規則を表現するためのものです。それぞれの規則は一行で表現され、コロン(:)の前が名前で、その後ろが定義になります。定義を複数行で書くこともできますが、この場合は、それぞれの定義の行の先頭に、最初の行と同じ高さにそろえてコロン(:)を書く必要があります。

   ディレクティブの引数の ``規則リスト`` の中には空行を入れることはできません。

   定義には解釈済みのテキストとしてマークされたトークン名を含むことができます。これらのトークンの規則との間にクロスリファレンスが生成されます。(例 ``sum ::= `integer` "+" `integer```)

   規則の中ではreSTパーサは動作しないため、 ``*`` や、 ``|`` といった文字をエスケープすることはできません。

.. .. directive:: productionlist

..   This directive is used to enclose a group of productions.  Each production is given on a single line and consists of a name, separated by a colon from the following definition.  If the definition spans multiple lines, each continuation line must begin with a colon placed at the same column as in the first line.

..   Blank lines are not allowed within ``productionlist`` directive arguments.

..   The definition can contain token names which are marked as interpreted text (e.g. ``sum ::= `integer` "+" `integer```) -- this generates cross-references to the productions of these tokens.

..   Note that no further reST parsing is done in the production, so that you don't have to escape ``*`` or ``|`` characters.

.. XXX describe optional first parameter

The following is an example taken from the Python Reference Manual::

   .. productionlist::
      try_stmt: try1_stmt | try2_stmt
      try1_stmt: "try" ":" `suite`
               : ("except" [`expression` ["," `target`]] ":" `suite`)+
               : ["else" ":" `suite`]
               : ["finally" ":" `suite`]
      try2_stmt: "try" ":" `suite`
               : "finally" ":" `suite`








.. highlight:: rest

.. Miscellaneous markup
.. ====================

その他のマークアップ
=====================

.. _metadata:

.. File-wide metadata
.. ------------------



.. reST has the concept of "field lists"; these are a sequence of fields marked up
   like this::

   :Field name: Field content

reSTは "フィールドリスト"という考えがあります。以下のようなものが、このフィールドのマークアップのリストのサンプルになります。

.. A field list at the very top of a file is parsed as the "docinfo", which in
   normal documents can be used to record the author, date of publication and
   other metadata.  In Sphinx, the docinfo is used as metadata, too, but not
   displayed in the output.

ファイルの先頭のフィールドリストは "docinfo" としてパースされます。これは通常のドキュメントでは著者名や、公開日などのメタデータを記録するのに使用します。Sphinxでは、 docinfoはメタデータとして使用されますが、出力はされません。

.. At the moment, these metadata fields are recognized:

このタイミングでは、以下のメタデータのフィールドが識別されています:

``tocdepth``
   このファイルに表示する目次の最大の深さ

   .. versionadded:: 0.4

..  The maximum depth for a table of contents of this file.


``nocomments``
   もし設定されていれば、このソースファイルから生成されたページをウェブアプリケーションが表示する際には、コメントフォームが表示されなくなります。

.. If set, the web application won't display a comment form for a page generated
   from this source file.


.. Meta-information markup
.. -----------------------

メタ情報マークアップ
--------------------

.. directive:: sectionauthor

   現在のセクションの著者名を指定します。引数には必ず、表示するための著者の名前と、電子メールのアドレスを入れます。アドレスのドメイン名の部分は小文字でなければなりません::

     .. sectionauthor:: Guido van Rossum <guido@python.org>

   デフォルトでは、このマークアップは出力に反映されません(貢献者の名前を調べる手助けにはなります)。しかし、設定ファイルの :confval:`show_authors` をTrueに設定すると、出力ファイルの中にこの情報に関する段落が作成されます。

.. Identifies the author of the current section.  The argument should include
   the author's name such that it can be used for presentation and email
   address.  The domain name portion of the address should be lower case.
   Example::

      .. sectionauthor:: Guido van Rossum <guido@python.org>

   By default, this markup isn't reflected in the output in any way (it helps
   keep track of contributions), but you can set the configuration value
   :confval:`show_authors` to True to make them produce a paragraph in the
   output.

.. _tags:

タグを使用したインクルード
--------------------------

.. Including content based on tags
   -------------------------------

.. .. directive:: .. only:: <expression>

   Include the content of the directive only if the *expression* is true.  The
   expression should consist of tags, like this::

      .. only:: html and draft

   Undefined tags are false, defined tags (via the ``-t`` command-line option or
   within :file:`conf.py`) are true.  Boolean expressions, also using
   parentheses (like ``html and (latex or draft)`` are supported.

   The format of the current builder (``html``, ``latex`` or ``text``) is always
   set as a tag.

.. directive:: .. only:: <式>

   *<式>* が真のときだけ、ディレクティブの内容をインクルードします。式は以下のようにタグで構成されます。

      .. only:: html and draft

   未定義のタグはflaseになります。コマンドラインの ``-t`` オプションもしくは :file:`conf.py` によって定義されたタグはtrueとして扱われます。カッコも含めて、ブール演算も使用することができます。 ``html and (latex or draft)`` というような表現がサポートされています。

   現在のビルダーのフォーマットのタグ (``html``, ``latex``, ``text``) は常にタグとしてセットされます。

   .. versionadded:: 0.6


.. Tables
.. ------

テーブル
--------

.. Use standard reStructuredText tables.  They work fine in HTML output, however
   there are some gotchas when using tables in LaTeX: the column width is hard to
   determine correctly automatically.  For this reason, the following directive
   exists:

標準のreStructuredTextの表を使用すると、HTML出力では非常にきれいな表を作成することができますが、LaTeXで出力すると、ちょっとがっかりしてしまうでしょう。現在の仕様ではカラムを自動で正しく決定するのは簡単ではありません。このような理由から、それをサポートするディレクティブがいくつか用意されています:

.. .. directive:: .. tabularcolumns:: column spec

   This directive gives a "column spec" for the next table occurring in the
   source file.  The spec is the second argument to the LaTeX ``tabulary``
   package's environment (which Sphinx uses to translate tables).  It can have
   values like ::

      |l|l|l|

   which means three left-adjusted, nonbreaking columns.  For columns with
   longer text that should automatically be broken, use either the standard
   ``p{width}`` construct, or tabulary's automatic specifiers:

   +-----+------------------------------------------+
   |``L``| ragged-left column with automatic width  |
   +-----+------------------------------------------+
   |``R``| ragged-right column with automatic width |
   +-----+------------------------------------------+
   |``C``| centered column with automatic width     |
   +-----+------------------------------------------+
   |``J``| justified column with automatic width    |
   +-----+------------------------------------------+

   The automatic width is determined by rendering the content in the table, and
   scaling them according to their share of the total width.

   By default, Sphinx uses a table layout with ``L`` for every column.

   .. versionadded:: 0.3

.. directive:: .. tabularcolumns:: カラム 仕様

   このディレクティブは次に作成するテーブルの "カラム仕様" を設定します。仕様はSphinxがテーブルの変換に使用している、LaTeXの ``tabulary`` パッケージ環境のためのものです。2番目の引数として設定します。以下のような値を設定します::

      |l|l|l|

   これは、３つの左寄せの、改行なしのカラムの意味になります。それぞれのカラムで、長いテキストを適切に自動的に改行させるためには、標準の ``p{width}`` 構造体を使用するか、tabularyの自動設定を使用します。

   +-----+------------------------------------------+
   |``L``| 左寄せのカラム。長さは自動調整。         |
   +-----+------------------------------------------+
   |``R``| 右寄せのカラム。長さは自動調整。         |
   +-----+------------------------------------------+
   |``C``| 中央寄せのカラム。長さは自動調整。       |
   +-----+------------------------------------------+
   |``J``| テキストを広げるカラム。長さは自動調整。 |
   +-----+------------------------------------------+

   長さが自動調整となっているものは、全体の長さのうち、それぞれのカラムが占める幅の割合に応じて列の大きさはスケールします。

   デフォルトでは、Sphinxはすべてのカラムに対して ``L`` を適用したレイアウトを自動で行います。

.. warning::

   リテラルブロックを含むテーブルには ``tabulary`` は適用できません。このような場合には、LaTeX標準の ``tabular`` 環境がしようされます。また、 ``p{width}`` を設定しないと、同様な環境は使用することはできません。デフォルトでは、というのは、Sphinxはそのようなテーブルのためには、そのようなカラムを生成します。 :dir:`tabularcolums` ディレクティブを使用することで、テーブルに対して細かい制御ができるようになります。

.. Tables that contain literal blocks cannot be set with ``tabulary``.  They are
   therefore set with the standard LaTeX ``tabular`` environment.  Also, the
   verbatim environment used for literal blocks only works in ``p{width}``
   columns, which means that by default, Sphinx generates such column specs for
   such tables.  Use the :dir:`tabularcolumns` directive to get finer control
   over such tables.


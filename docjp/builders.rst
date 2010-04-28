.. Available builders

.. _builders:

利用可能なビルダー
==================

.. module:: sphinx.builders
   :synopsis: 利用可能な組み込みのビルダークラス

..   :synopsis: Available built-in builder classes.

.. These are the built-in Sphinx builders.  More builders can be added by
   :ref:`extensions <extensions>`.

このドキュメントにあるのが組み込みのSphinxのビルダーです。
また、 :ref:`拡張 <extensions>` の仕組みを使うと、ビルダーを追加することもできます。

.. The builder's "name" must be given to the **-b** command-line option of
   :program:`sphinx-build` to select a builder.

:program:`sphinx-build` の起動時には、コマンドラインオプション\ **-b**\ でビルダーの名前を指定しなければなりません。

.. module:: sphinx.builders.html
.. class:: StandaloneHTMLBuilder


   .. This is the standard HTML builder.  Its output is a directory with HTML
      files, complete with style sheets and optionally the reST sources.  There are
      quite a few configuration values that customize the output of this builder,
      see the chapter :ref:`html-options` for details.

   これは標準的なHTMLビルダーです。
   このビルダーはディレクトリにHTMLファイルと、スタイルシート、追加のreSTソースを出力します。
   このビルダーにはビルダーの出力を変更できる設定値をいくつか持っています。
   詳しくは :ref:`html-options` をご覧ください。

   .. Its name is ``html``.

   このビルダーの名前は ``html`` です。


.. class:: DirectoryHTMLBuilder

   .. This is a subclass of the standard HTML builder.  Its output is a directory
      with HTML files, where each file is called ``index.html`` and placed in a
      subdirectory named like its page name.  For example, the document
      ``markup/rest.rst`` will not result in an output file ``markup/rest.html``,
      but ``markup/rest/index.html``.  When generating links between pages, the
      ``index.html`` is omitted, so that the URL would look like ``markup/rest/``.

  このクラスは、標準のHTMLビルダーのサブクラスです。これは\ ``index.html`` \という名前のHTMLファイルと一緒にディレクトリを出力します。そのときに、そのページ名がディレクトリの名前になります。例えば、\ ``markup/rest.rst``\ というファイルがあるとすると、\  ``markup/rest.html``\ というファイルが出力されるのではなく、\ ``markup/rest/index.html``\ というファイルが出力されます。ページ間のリンクが生成される場合には、末尾の\ ``index.html``\ を省いて、\  ``markup/rest/``\ というようなURLが生成されます。

   .. Its name is ``dirhtml``.

   このビルダーの名前は\ ``dirhtml``\ になります。

   .. versionadded:: 0.6


.. class:: SingleFileHTMLBuilder

   .. This is an HTML builder that combines the whole project in one output file.
      (Obviously this only works with smaller projects.)  The file is named like
      the master document.  No indices will be generated.

   これは、プロジェクト全体のファイルを結合して、1ファイルにして出力するHTMLビルダーです。
   (これは小さなプロジェクトでうまく動作します。) このファイルは、マスタードキュメントに似た名前になります。
   また、索引は生成されません。

   .. Its name is ``singlehtml``.

   このビルダーの名前は ``singlehtml`` になります。

   .. versionadded:: 1.0


.. module:: sphinx.builders.htmlhelp
.. class:: HTMLHelpBuilder

   .. This builder produces the same output as the standalone HTML builder, but
      also generates HTML Help support files that allow the Microsoft HTML Help
      Workshop to compile them into a CHM file.

   このビルダーは標準のHTMLビルダーと同じものを出力しますが、MicrosoftのHTML Help Workshopで使用できる、HTMLヘルプのサポートファイルも生成します。これらの入力をHTML Help Workshop上でコンパイルすると、CHMファイルが生成されます。

   .. Its name is ``htmlhelp``.

   このビルダーの名前は\ ``htmlhelp``\ になります。


.. module:: sphinx.builders.qthelp
.. class:: QtHelpBuilder

   .. This builder produces the same output as the standalone HTML builder, but
      also generates Qt help collection support files that allow
      the Qt collection generator to compile them.

   このビルダーは標準のHTMLビルダーと同じものを出力しますが、 `Qt help`_ collectionを使ってコンパイルするのに必要なサポートファイル群も一緒に出力します。

   .. Its name is ``qthelp``.

   このビルダーの名前は\ ``qthelp``\ になります。

   .. _Qt help: http://doc.trolltech.com/4.6/qthelp-framework.html

.. module:: sphinx.builders.devhelp
.. class:: DevhelpBuilder

   .. This builder produces the same output as the standalone HTML builder, but
      also generates `GNOME Devhelp <http://live.gnome.org/devhelp>`__ 
      support file that allows the GNOME Devhelp reader to view them.

   このビルダーは標準のHTMLビルダーと同じものを出力しますが、 `GNOME Devhelp <http://live.gnome.org/devhelp>`__ を使ってコンパイルするのに必要なサポートファイル群も一緒に出力します。これらのファイルはGNOME Devhelp readerを使って見ることができます。

   .. Its name is ``devhelp``.

   このビルダーの名前は\ ``devhelp``\ になります。


.. module:: sphinx.builders.epub
.. class:: EpubBuilder

   .. This builder produces the same output as the standalone HTML builder, but
      also generates an *epub* file for ebook readers.  See :ref:`epub-faq` for
      details about it.  For definition of the epub format, have a look at
      `<http://www.idpf.org/specs.htm>`_ or `<http://en.wikipedia.org/wiki/EPUB>`_

   このビルダーはstandaloneのHTMLビルダーと同じものを出力しますが、電子ブックリーダーのための、 *epub* ファイルも一緒に生成します。詳しくは :ref:`epub-faq` を参照してください。epubフォーマットの定義については `<http://www.idpf.org/specs.htm>`_ もしくは `<http://en.wikipedia.org/wiki/EPUB>`_ を参照してください。

   .. Some ebook readers do not show the link targets of references.  Therefore
      this builder adds the targets after the link when necessary.  The display
      of the URLs can be customized by adding CSS rules for the class
      ``link-target``.

   電子ブックリーダーによっては、参照のリンクターゲットが表示されない場合があります。そのため、必要に応じて、このビルダーはリンクの後ろにターゲットを追加します。URLの表示は、 ``link-target`` クラスをCSSのルールに追加することで、カスタマイズすることができます。

   .. Its name is ``epub``.

   このビルダーの名前は\ ``epub``\ になります。


.. module:: sphinx.builders.latex
.. class:: LaTeXBuilder

   .. This builder produces a bunch of LaTeX files in the output directory.  You
      have to specify which documents are to be included in which LaTeX files via
      the :confval:`latex_documents` configuration value.  There are a few
      configuration values that customize the output of this builder, see the
      chapter :ref:`latex-options` for details.

   このビルダーは出力フォルダ内に、LaTeXのファイル群を生成します。どのドキュメントを含むかを、 :confval:`latex_documents` の設定値を使って設定します。このビルダーの出力をカスタマイズするための設定値はいくつかあります。詳しくは :ref:`latex-options` の章を参照してください。

   .. note::

      .. The produced LaTeX file uses several LaTeX packages that may not be
         present in a "minimal" TeX distribution installation.  For TeXLive,
         the following packages need to be installed:

      生成されるLaTeXファイルは、最低限のTeXディストリビューションいくつかのLaTeXパッケージを使用しています。例えば、TeXLiveでは以下のパッケージをインストールする必要があります。

      * latex-recommended
      * latex-extra
      * fonts-recommended

   .. Its name is ``latex``.   

   このビルダーの名前は\ ``latex``\ です。

   .. Note that a direct PDF builder using ReportLab is available in `rst2pdf
      <http://rst2pdf.googlecode.com>`_ version 0.12 or greater.  You need to add
      ``'rst2pdf.pdfbuilder'`` to your :confval:`extensions` to enable it, its name is
      ``pdf``.  Refer to the `rst2pdf manual
      <http://lateral.netmanagers.com.ar/static/manual.pdf>`_ for details.

   `rst2pdf <http://rst2pdf.googlecode.com>`_ のバージョン 0.12以降を使うと、ReportLabを使用して、PDFを直接出力するビルダーが利用できます。これを使用するためには、 :confval:`extensions` に ``'rst2pdf.pdfbuilder'`` を追加して、ビルダー名 ``pdf`` を指定してビルドします。詳しくは、 `rst2pdfのマニュアル <http://lateral.netmanagers.com.ar/static/manual.pdf>`_ を参照してください。


.. module:: sphinx.builders.text
.. class:: TextBuilder

   .. This builder produces a text file for each reST file -- this is almost the
      same as the reST source, but with much of the markup stripped for better
      readability.

   このビルダーはそれぞれのreSTファイルからテキストファイルを生成します。多くのマークアップが読みやすさのために落とされていますが、ほぼソースのreSTと同じです。

   .. Its name is ``text``.

   このビルダーの名前は\ ``text``\ です。

   .. versionadded:: 0.4


.. module:: sphinx.builders.manpage
.. class:: ManualPageBuilder

   .. This builder produces manual pages in the groff format.  You have to specify
      which documents are to be included in which manual pages via the
      :confval:`man_pages` configuration value.

   このビルダーは、groffフォーマットのmanページを作成します。manページに含めるドキュメントは、 :confval:`man_pages` 設定値を使って指定します。

   .. Its name is ``man``.

   このビルダーの名前は ``man`` になります。

   .. note::

      .. This builder requires the docutils manual page writer, which is only
         available as of docutils 0.6.

      このビルダーを実行するには、docutilsのmanページライターが必要になるため、
      docutils 0.6以降が必要となります。

   .. versionadded:: 1.0


.. currentmodule:: sphinx.builders.html
.. class:: SerializingHTMLBuilder

   .. This builder uses a module that implements the Python serialization API
      (`pickle`, `simplejson`, `phpserialize`, and others) to dump the generated
      HTML documentation.  The pickle builder is a subclass of it.

   このビルダーはPythonのシリアライズAPI(`pickle`, `simplejson`, `phpserialize` など)を利用して、実装されています。生成されたHTMLをダンプします。 pickleビルダーはこのクラスのサブクラスになります。

   .. A concrete subclass of this builder serializing to the `PHP serialization`_
      format could look like this:

   このビルダーのサブクラスを作成して `PHP シリアライズ`_ フォーマットでシリアライズするには、以下のようにします::

        import phpserialize

        class PHPSerializedBuilder(SerializingHTMLBuilder):
            name = 'phpserialized'
            implementation = phpserialize
            out_suffix = '.file.phpdump'
            globalcontext_filename = 'globalcontext.phpdump'
            searchindex_filename = 'searchindex.phpdump'

   .. 
      _PHP serialization: http://pypi.python.org/pypi/phpserialize

   .. _PHP シリアライズ: http://pypi.python.org/pypi/phpserialize

   .. attribute:: implementation

      .. A module that implements `dump()`, `load()`, `dumps()` and `loads()`
         functions that conform to the functions with the same names from the
         pickle module.  Known modules implementing this interface are
         `simplejson` (or `json` in Python 2.6), `phpserialize`, `plistlib`,
         and others.

      pickleモジュールと同じ名前の `dump()`, `load()`, `dumps()`,  `loads()` 関数が実装されているモジュールです。このようなインタフェースを実装しているモジュールでよく知られているものには、 `simplejson` (Python2.6では `json`), `phpserialize`, `plistlib` などがあります。

   .. attribute:: out_suffix

      .. The suffix for all regular files.

      すべての通常のファイルに付くサフィックスです。

   .. attribute:: globalcontext_filename

      .. The filename for the file that contains the "global context".  This
         is a dict with some general configuration values such as the name
         of the project.

      "グローバルコンテキスト"を含むファイルのファイル名です。これは、プロジェクト名などの一般的な設定値を含む辞書です。

   .. attribute:: searchindex_filename

      .. The filename for the search index Sphinx generates.

      Sphinxが作成する、検索インデックスのファイル名です。

   .. See :ref:`serialization-details` for details about the output format.

   出力フォーマットの詳細については、 :ref:`serialization-details` を参照してください。

   .. versionadded:: 0.5


.. class:: PickleHTMLBuilder

   .. This builder produces a directory with pickle files containing mostly HTML
      fragments and TOC information, for use of a web application (or custom
      postprocessing tool) that doesn't use the standard HTML templates.

   このビルダーは、pickleでシリアライズしたほとんどのHTML片と、目次情報を含むディレクトリを作成します。このビルダーで生成した結果は、標準のHTMLテンプレートを使用しない、ウェブアプリケーションや、カスタムの後処理ツールで使用することができます。

   .. See :ref:`serialization-details` for details about the output format.

   出力フォーマットの詳細については、 :ref:`serialization-details` を参照してください。

   .. Its name is ``pickle``.  (The old name ``web`` still works as well.)

   このビルダーの名前は ``pickle`` です。以前の名前である ``web`` もまだ使用できます。

   .. The file suffix is ``.fpickle``.  The global context is called
      ``globalcontext.pickle``, the search index ``searchindex.pickle``.

   ファイルのサフィックスは ``.fpickle`` になります。グローバルコンテキストは ``globalcontext.pickle`` に、検索インデックスは ``searchindex.pickle`` になります。


.. class:: JSONHTMLBuilder

   .. This builder produces a directory with JSON files containing mostly HTML
      fragments and TOC information, for use of a web application (or custom
      postprocessing tool) that doesn't use the standard HTML templates.

   このビルダーは、jsonでシリアライズしたほとんどのHTML片と、目次情報を含むディレクトリを作成します。このビルダーで生成した結果は、標準のHTMLテンプレートを使用しない、ウェブアプリケーションや、カスタムの後処理ツールで使用することができます。

   .. See :ref:`serialization-details` for details about the output format.

   出力フォーマットの詳細については、 :ref:`serialization-details` を参照してください。

   .. Its name is ``json``.

   このビルダーの名前は ``json`` です。

   .. The file suffix is ``.fjson``.  The global context is called
      ``globalcontext.json``, the search index ``searchindex.json``.

   ファイルのサフィックスは ``.fjson`` になります。グローバルコンテキストは ``globalcontext.json`` に、検索インデックスは ``searchindex.json`` になります。

   .. versionadded:: 0.5


.. module:: sphinx.builders.changes
.. class:: ChangesBuilder

   .. This builder produces an HTML overview of all :rst:dir:`versionadded`,
      :rst:dir:`versionchanged` and :rst:dir:`deprecated` directives for the current
      :confval:`version`.  This is useful to generate a ChangeLog file, for
      example.

   このビルダーは、現在の :confval:`version` の設定値と、 :rst:dir:`versionadded`, :rst:dir:`versionchanged`, :rst:dir:`deprecated` の各ディレクティブの情報から、HTMLを生成します。このビルダーは、例えばChangeLogファイルを生成するのに便利です。

   .. Its name is ``changes``.

   このビルダーの名前は ``changes`` です。


.. module:: sphinx.builders.linkcheck
.. class:: CheckExternalLinksBuilder

   .. This builder scans all documents for external links, tries to open them with
      :mod:`urllib2`, and writes an overview which ones are broken and redirected
      to standard output and to :file:`output.txt` in the output directory.

   このビルダーは、すべてのドキュメントの外部リンクをチェックして、 :mod:`urllib2` を使用してきちんと開けるかどうか確認を行います。壊れたリンク、および、リダイレクトされるリンクの情報を、標準出力と、出力ディレクトリの :file:`output.txt` というファイルに出力します。

   .. Its name is ``linkcheck``.

   このビルダーの名前は ``linkcheck`` です。


.. Built-in Sphinx extensions that offer more builders are:

組み込みのSphinx拡張には、以下の追加のビルダーが含まれます:

* :mod:`~sphinx.ext.doctest`
* :mod:`~sphinx.ext.coverage`

.. Serialization builder details
   -----------------------------

.. _serialization-details:

シリアライズを行うビルダーの詳細
--------------------------------

.. All serialization builders outputs one file per source file and a few special
   files.  They also copy the reST source files in the directory ``_sources``
   under the output directory.

すべてのシリアライズを行うビルダーは、ソースファイル１つごとに対応するファイルと、いくつかの特殊なファイルを出力します。また、reST形式のソースファイルは、出力ディレクトリ内の ``_sources`` ディレクトリ内にコピーされます。

.. The :class:`PickleHTMLBuilder` is a builtin subclass that implements the pickle
   serialization interface.

:class:`PickleHTMLBuilder` クラスは組み込みのサブクラスで、pickleでシリアライズを行うインタフェースを実装しています。

.. The files per source file have the extensions of
   :attr:`~SerializingHTMLBuilder.out_suffix`, and are arranged in directories
   just as the source files are.  They unserialize to a dictionary (or dictionary
   like structure) with these keys:

ソースファイルごとに出力されるファイルは :attr:`~SerializingHTMLBuilder.out_suffix` で指定された拡張子を持ち、ソースファイルと同様のディレクトリ構成で書き出されます。これらのファイルは以下のようなキーを持つ辞書、あるいは辞書のようなオブジェクトとして復元することが可能です。

``body``
   HTMLの本体が格納されています。HTMLトランスレータを利用してレンダリングされたものになります。

``title``
   ドキュメントのタイトルです。HTMLのマークアップが含まれている可能性があります。

``toc``
   ファイルの索引になります。HTMLの ``<ul>`` を使って表現されています。

``display_toc``
   ``toc`` が一つ以上のエントリーを含む場合に ``True`` になる、ブール型の値になります。

``current_page_name``
   現在のファイルのドキュメント名になります。

``parents``, ``prev``, ``next``
   TOCツリー上で関連する章の情報です。関連は辞書として表現されます。 ``key``\ (HREF情報)と\ ``title``\ (関連ドキュメントのタイトル情報のHTML)が含まれます。 ``parents``\ の場合には、関連のリストが含まれますが、\ ``prev``\ と\ ``next``\ の場合には関連が一つだけ含まれます。

``sourcename``
   ``_sources``\ 以下に置かれている、ソースファイルの名前になります。

.. The HTML "body" (that is, the HTML rendering of the source file), as rendered
   by the HTML translator.

   ``title``
      The title of the document, as HTML (may contain markup).

   ``toc``
      The table of contents for the file, rendered as an HTML ``<ul>``.

   ``display_toc``
      A boolean that is ``True`` if the ``toc`` contains more than one entry.

   ``current_page_name``
      The document name of the current file.

   ``parents``, ``prev`` and ``next``
      Information about related chapters in the TOC tree.  Each relation is a
   dictionary with the keys ``link`` (HREF for the relation) and ``title``
   (title of the related document, as HTML).  ``parents`` is a list of
   relations, while ``prev`` and ``next`` are a single relation.

   ``sourcename``
      The name of the source file under ``_sources``.

.. The special files are located in the root output directory.  They are:

出力ディレクトリのルートには、以下の特殊なファイルが配置されます:

:attr:`SerializingHTMLBuilder.globalcontext_filename`
   pickleでシリアライズされた辞書です。以下のキーを持っています:

   ``project``, ``copyright``, ``release``, ``version``
      設定ファイルで指定された、同じ名前の設定の値が入ります。

   ``style``
      :confval:`html_style`

   ``last_updated``
      最後にビルドした日時です。

   ``builder``
      使用したビルダーの名前です。この場合はこれは常に\ ``'pickle'``\ になります。

   ``titles``
      すべてのドキュメントのHTML形式のタイトルを含む辞書です。

.. A pickled dict with these keys:

   ``project``, ``copyright``, ``release``, ``version``
      The same values as given in the configuration file.

   ``style``
      :confval:`html_style`.

   ``last_updated``
      Date of last build.

   ``builder``
      Name of the used builder, in the case of pickles this is always
      ``'pickle'``.

   ``titles``
      A dictionary of all documents' titles, as HTML strings.

:attr:`SerializingHTMLBuilder.searchindex_filename`
   ドキュメントの検索で使用されるインデックスになります。以下のエントリーを含む、pickleでシリアライズされたエントリーのリストになります。

   * インデックスが作成されたドキュメント名のリストです。
   * HTMLの文字列形式で作成された、タイトルのリストです。最初のリストと同じ順序になっています。
   * 単語から、数値のリストへの辞書です。この数値は最初のリストのインデックスになります。

.. An index that can be used for searching the documentation.  It is a pickled
   list with these entries:

   * A list of indexed docnames.
   * A list of document titles, as HTML strings, in the same order as the first
     list.
   * A dict mapping word roots (processed by an English-language stemmer) to a
     list of integers, which are indices into the first list.

``environment.pickle``
   ビルド環境です。これは常にpickleでシリアライズされたファイルで、ビルダーとは独立しています。ビルダーが起動された地点で使用された、環境のコピーです。ドキュメント間の共有のメンバーです。

   .. todo:: 共通メンバーのドキュメントを書く

   他のシリアライズされたファイルとは異なり、このファイルは ``Sphinx`` のパッケージのみが中を読むことを想定しています。

.. The build environment.  This is always a pickle file, independent of the
   builder and a copy of the environment that was used when the builder was
   started.

   .. todo:: Document common members

   Unlike the other pickle files this pickle file requires that the ``sphinx``
   package is available on unpickling.
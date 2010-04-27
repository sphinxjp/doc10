.. highlightlang:: python

.. The build configuration file
.. ============================

.. _build-config:

ビルド設定ファイル
==================

.. .. module:: conf
      :synopsis: Build configuration file.

.. module:: conf
    :synopsis: ビルド設定ファイル

.. The :term:`configuration directory` must contain a file named :file:`conf.py`.
   This file (containing Python code) is called the "build configuration file" and
   contains all configuration needed to customize Sphinx input and output behavior.

:term:`コンフィグレーションディレクトリ` には必ず :file:`conf.py` が含まれています。このファイルは
"ビルド設定ファイル" と呼ばれていて、Sphinxの入出力の動作をカスタマイズするのに必要な
設定はこのファイルに含まれています。この設定ファイルはPythonのプログラムとして書かれています。

.. The configuration file is executed as Python code at build time (using
   :func:`execfile`, and with the current directory set to its containing
   directory), and therefore can execute arbitrarily complex code.  Sphinx then
   reads simple names from the file's namespace as its configuration.

設定ファイルは、ビルド時にPythonコードとして実行されます。 設定ファイルが含まれる
フォルダをカレントディレクトリに設定し、:func:`execfile` を使用してコールされので、
任意の複雑なコードを記述することができます。Sphinxが読み込む際には単純にファイルの
中の名前空間に定義されている名前を使うことで、設定を読み込みます。

.. Important points to note:

詳細に説明するにあたっての注意点を列挙します。

.. * If not otherwise documented, values must be strings, and their default is the
     empty string.

* 特別に指定されていない場合には、設定値は文字列型になります。また、指定されていない場合のデフォルト値は空文字列です。

.. * The term "fully-qualified name" refers to a string that names an importable
     Python object inside a module; for example, the FQN
     ``"sphinx.builders.Builder"`` means the ``Builder`` class in the
     ``sphinx.builders`` module.

* "完全限定名(FQN)"という用語は、モジュール内のインポート可能なPythonオブジェクトをあらわす名前です。例えば、 ``"sphinx.builders.Builder"`` という完全限定名は、 ``sphinx.builders`` モジュールにある ``Builder`` クラスを意味します。

.. * Remember that document names use ``/`` as the path separator and don't contain
     the file name extension.

* ドキュメント名は、パスのセパレータとして ``/`` を使用します。また、拡張子は含まないで表記します。

.. * Since :file:`conf.py` is read as a Python file, the usual rules apply for
     encodings and Unicode support: declare the encoding using an encoding cookie
     (a comment like ``# -*- coding: utf-8 -*-``) and use Unicode string literals
     when you include non-ASCII characters in configuration values.

* :file:`conf.py` はPythonファイルとして読み込むため、Pythonの標準のエンコーディングや、ユニコードサポートなどを利用することができます。設定値にASCII文字以外の文字を含む場合には、エンコーディング宣言(行頭に ``# -*- coding: utf-8 -*-`` とコメントを入れる)を使用して、ユニコード文字列リテラルを使用してください。

.. * The contents of the config namespace are pickled (so that Sphinx can find out
     when configuration changes), so it may not contain unpickleable values --
     delete them from the namespace with ``del`` if appropriate.  Modules are
     removed automatically, so you don't need to ``del`` your imports after use.

*  設定の名前空間の内容はpickle化されます(そのため、Sphinxは設定の変更されたのを確認することができます)。そのため、pickle化できない値が含まれているのを発見したら、 ``del`` を使って名前空間から削除します。モジュールは自動的に削除されるため、 ``import`` したモジュールがあったら、使用後に ``del`` を行う必要はありません。

.. * There is a special object named ``tags`` available in the config file.
     It can be used to query and change the tags (see :ref:`tags`).  Use
     ``tags.has('tag')`` to query, ``tags.add('tag')`` and ``tags.remove('tag')``
     to change.

* 設定ファイルには、 ``tags`` という名前の特別なオブジェクトがあります。これはタグの問い合わせをしたり、変更したりするのに使用します。詳しくは :ref:`tags` も参照してください。問い合わせには ``tags.has('tag')`` 、変更には ``tags.add('tag')`` 、 ``tags.remove('tag')`` という使い方をします。


.. General configuration
   ---------------------

一般的な設定
------------

.. confval:: extensions

   .. A list of strings that are module names of Sphinx extensions.  These can be
      extensions coming with Sphinx (named ``sphinx.ext.*``) or custom ones.

   使用したいSphinx拡張のモジュールを指定する配列です。この設定自体は配列で、中に、使用したい拡張モジュールの名前の文字列が含まれます。文字列としてはSphinxに付属のもの( ``sphinx.ext.*`` )か、カスタムの拡張機能を指定できます。

   .. Note that you can extend :data:`sys.path` within the conf file if your
      extensions live in another directory -- but make sure you use absolute paths.
      If your extension path is relative to the :term:`configuration directory`,
      use :func:`os.path.abspath` like so:

   もし拡張機能が他のディレクトリにある場合には、confファイルの中で :data:`sys.path` にパスを追加することで、使用できるようになります。注意すべき点としては、絶対パスを指定しなければならない点です。もし、 :term:`コンフィグレーションディレクトリ` からの相対パスが分かっている場合には、以下のように :func:`os.path.abspath` を以下のように使用します::

      import sys, os

      sys.path.append(os.path.abspath('sphinxext'))

      extensions = ['extname']

   .. That way, you can load an extension called ``extname`` from the subdirectory
      ``sphinxext``.

   上記のコードでは ``sphinxext`` というサブディレクトリに含まれる ``extname`` という名前の拡張機能をロードしています。

   .. The configuration file itself can be an extension; for that, you only need to
      provide a :func:`setup` function in it.

   設定ファイル自身で拡張機能を実装してもかいません。その場合には、 :func:`setup` という名前の関数を提供する必要があります。


.. confval:: source_suffix

   .. The file name extension of source files.  Only files with this suffix will be
      read as sources.  Default is ``'.rst'``.

   ソースファイルに付く、ファイル名の拡張子を指定します。ここで指定された名前が末尾に付くファイルだけがソースファイルとして読み込まれます。デフォルトは ``'.rst'`` です。


.. confval:: source_encoding

   .. The encoding of all reST source files.  The recommended encoding, and the
      default value, is ``'utf-8-sig'``.

   すべてのreSTのソースファイルのエンコーディングを指定します。デフォルトかつ、推奨のエンコーディングは ``'utf-8-sig'`` です。

   .. .. versionadded:: 0.5

         Previously, Sphinx accepted only UTF-8 encoded sources.

   .. versionadded:: 0.5

      以前はSphinxはUTF-8エンコードされたソースしか読み込むことができませんでした。


.. confval:: master_doc

   .. The document name of the "master" document, that is, the document that
      contains the root :rst:dir:`toctree` directive.  Default is ``'contents'``.

   "マスター"ドキュメントのドキュメント名を指定します。"マスター"ドキュメントには、ルートとなる :rst:dir:`toctree` ディレクティブが含まれます。デフォルトは ``'contents'`` です。


.. confval:: exclude_patterns

   .. A list of glob-style patterns that should be excluded when looking for source
      files. [1]_ They are matched against the source file names relative to the
      source directory, using slashes as directory separators on all platforms.

   globスタイルのパターンのリストを設定し、ソースファイルの探索時に排除すべきファイルを指定します。これらのパターンは、ソースディレクトリからの相対パスで渡されるソースファイル名に対してマッチします。すべての環境で、ディレクトリの指定として、スラッシュ(/)が使用されます。

   .. Example patterns:

   サンプルのパターン:

   .. - ``'library/xml.rst'`` -- ignores the ``library/xml.rst`` file (replaces
        entry in :confval:`unused_docs`
   .. - ``'library/xml'`` -- ignores the ``library/xml`` directory (replaces entry
        in :confval:`exclude_trees`)
   .. - ``'library/xml*'`` -- ignores all files and directories starting with
        ``library/xml``
   .. - ``'**/.svn'`` -- ignores all ``.svn`` directories (replaces entry in
        :confval:`exclude_dirnames`)

   - ``'library/xml.rst'`` -- ``library/xml.rst`` ファイルを無視します。 :confval:`unused_docs` のエントリーの置き換えになります。
   - ``'library/xml'`` -- ``library/xml`` ディレクトリを無視します。 :confval:`exclude_trees` のエントリーの置き換えになります。
   - ``'library/xml*'`` -- ``library/xml`` から始まる全てのファイルとディレクトリを無視します。
     ``library/xml``
   - ``'**/.svn'`` -- すべての ``.svn`` ディレクトリを無視します。 :confval:`exclude_dirnames` のエントリーの置き換えになります。

   .. :confval:`exclude_patterns` is also consulted when looking for static files
      in :confval:`html_static_path`.

   :confval:`exclude_patterns` は、 :confval:`html_static_path` の中の静的ファイルを探索する時にも参照されます。

   .. versionadded:: 1.0


.. confval:: unused_docs

   .. A list of document names that are present, but not currently included in the
      toctree.  Use this setting to suppress the warning that is normally emitted
      in that case.

   ディレクトリ内には存在するが、現在はtoctreeに読み込まないドキュメント名のリストです。Sphinxはこのようなファイルがあると、警告を出力しますが、この警告を非表示にしたいときにこの設定を使用します。

   .. .. deprecated:: 1.0
         Use :confval:`exclude_patterns` instead.

   .. deprecated:: 1.0
      代わりに :confval:`exclude_patterns` を使用してください


.. confval:: exclude_trees

   .. A list of directory paths, relative to the source directory, that are to be
      recursively excluded from the search for source files, that is, their
      subdirectories won't be searched too.  The default is ``[]``.

   ソースファイルの検索から除外したいディレクトリパスの配列です。ソースディレクトリからの相対パスで、このフォルダからの再帰的な検索もされなくなるため、サブディレクトリも検索されません。デフォルトは ``[]`` です。

   .. versionadded:: 0.4

   .. .. deprecated:: 1.0
         Use :confval:`exclude_patterns` instead.

   .. deprecated:: 1.0
      代わりに :confval:`exclude_patterns` を使用してください


.. confval:: exclude_dirnames

   .. A list of directory names that are to be excluded from any recursive
      operation Sphinx performs (e.g. searching for source files or copying static
      files).  This is useful, for example, to exclude version-control-specific
      directories like ``'CVS'``.  The default is ``[]``.

   Sphinxが行う再帰的な処理で使用されたくないディレクトリ名のリストです。Sphinxではソースファイルの探索や静的ファイルのコピーなどで、再帰的にディレクトリを探索します。 ``'CVS'`` などの、バージョンコントロールのシステムのためのディレクトリを一括で除外したい場合などに便利です。デフォルトは ``[]`` です。

   .. versionadded:: 0.5

   .. .. deprecated:: 1.0
         Use :confval:`exclude_patterns` instead.

   .. deprecated:: 1.0
      代わりに :confval:`exclude_patterns` を使用してください


.. confval:: locale_dirs

   .. versionadded:: 0.5

   .. Directories in which to search for additional Sphinx message catalogs (see
      :confval:`language`), relative to the source directory.  The directories on
      this path are searched by the standard :mod:`gettext` module for a domain of
      ``sphinx``; so if you add the directory :file:`./locale` to this settting,
      the message catalogs must be in
      :file:`./locale/{language}/LC_MESSAGES/sphinx.mo`.

   追加のSphinxメッセージカタログ( :confval:`language` 参照)を探索するディレクトリを指定します。ここで指定されたパスが、標準の :mod:`gettext` モジュールによって、 ``sphinx`` ドメインで検索されます。 :file:`./locale` を設定ファイルに指定した場合には、 :file:`./locale/{language}/LC_MESSAGES/sphinx.mo` という場所にメッセージカタログを置かなければなりません。

   .. The default is ``[]``.

   デフォルトは ``[]`` です。


.. confval:: templates_path

   .. A list of paths that contain extra templates (or templates that overwrite
      builtin/theme-specific templates).  Relative paths are taken as relative to
      the configuration directory.

   追加のテンプレート(もしくは組み込みのテーマに関するテンプレートをオーバーライトするテンプレート)が含まれているパスのリストです。 コンフィギュレーションディレクトリからの相対パスで設定します。


.. confval:: template_bridge

   .. A string with the fully-qualified name of a callable (or simply a class) that
      returns an instance of :class:`~sphinx.application.TemplateBridge`.  This
      instance is then used to render HTML documents, and possibly the output of
      other builders (currently the changes builder).  (Note that the template
      bridge must be made theme-aware if HTML themes are to be used.)

   `~sphinx.application.TemplateBridge` のインスタンスを返す、呼び出し可能なオブジェクト、もしくはシンプルなクラスをあらわす完全限定名です。このインスタンスはHTMLドキュメントや、その他のビルダーの出力をレンダリングする際に使用されます。現在ではchanges builderに使用されています。テンプレートブリッジはHTMLテーマが使用された場合には、これに対応するように作られるべきです。


.. confval:: rst_epilog

   .. .. index:: pair: global; substitutions

   .. index:: pair: グローバル; 置換

   .. A string of reStructuredText that will be included at the end of every source
      file that is read.  This is the right place to add substitutions that should
      be available in every file.  An example:

   読み込まれたすべてのソースファイルの末尾に挿入されるreSturucturedTextの文字列を設定します。この設定を利用すると、文字列置換をすべてのファイルに対して行いたいときに、うまく動作します:

   .. rst_epilog = """
      .. |psf| replace:: Python Software Foundation
      """

   .. code-block:: python

      rst_epilog = """
      .. |psf| replace:: Pythonソフトウェア財団
      """

   .. versionadded:: 0.6


.. confval:: rst_prolog

   .. A string of reStructuredText that will be included at the beginning of every
      source file that is read.

   読み込まれたすべてのソースファイルの先頭に挿入されるreSturucturedTextの文字列を設定します。

   .. versionadded:: 1.0


.. confval:: default_domain

   .. .. index:: default; domain

   .. index:: デフォルト; ドメイン

   .. The name of the default :ref:`domain <domains>`.  Can also be ``None`` to
      disable a default domain.  The default is ``'py'``.

   デフォルトの :ref:`ドメイン <domains>` を指定します。 ``None`` を設定すると、デフォルトドメインを無効にします。デフォルトは ``'py'`` です。

   .. versionadded:: 1.0


.. confval:: default_role

   .. .. index:: default; role

   .. index:: デフォルト; ロール

   .. The name of a reST role (builtin or Sphinx extension) to use as the default
      role, that is, for text marked up ```like this```.  This can be set to
      ``'py:obj'`` to make ```filter``` a cross-reference to the function "filter".
      The default is ``None``, which doesn t reassign the default role.

   デフォルトロールとして使用する、reSTロールの名前(組み込み、もしくはSphinx拡張)を設定します。これは ```このような``` テキストのマークアップに対して適用されます。これは ``'py:obj'`` というものがあれば、 ```filter``` という関数と、Pythonの "filter" のクロスリファレンスを行います。デフォルトは ``None`` で、デフォルトのロールは適用されません。

   .. The default role can always be set within individual documents using the
      standard reST :rst:dir:`default-role` directive.

   デフォルトのロールは、reST標準の :rst:dir:`default-role` ディレクティブを使用することによっても個々のドキュメントに対して設定することができます。

   .. versionadded:: 0.4


.. confval:: keep_warnings

   .. If true, keep warnings as "system message" paragraphs in the built documents.
      Regardless of this setting, warnings are always written to the standard error
      stream when ``sphinx-build`` is run.

   Trueが設定されると、警告の内容がビルド済みドキュメントの"システムメッセージ"パラグラフの中に保存されます。この設定に関係なく、 ``sphinx-build`` 実行時標準エラー出力には警告が出力されます。

   .. The default is ``False``, the pre-0.5 behavior was to always keep them.

   デフォルトは ``False`` で 0.5以前の振る舞いを維持するにはこのままにしてください。

   .. versionadded:: 0.5


.. confval:: needs_sphinx

   .. If set to a ``major.minor`` version string like ``'1.1'``, Sphinx will
      compare it with its version and refuse to build if it is too old.  Default is
      no requirement.

   ドキュメントが想定しているSphinxのバージョンを設定します。 ``'1.1'`` というような形式で、 ``メジャー.マイナー`` というバージョン文字列を設定すると、Sphinxは自分のバージョンとの比較を行い、もしもバージョンが古すぎる場合にはビルドを中止します。デフォルトでは、チェックをしないようになっています。

   .. versionadded:: 1.0


.. confval:: nitpicky

   .. If true, Sphinx will warn about *all* references where the target cannot be
      found.  Default is ``False``.  You can activate this mode temporarily using
      the :option:`-n` command-line switch.

   もしもTrueが設定されると、 **すべての** 参照に対して、参照先が見つからないと警告を出します。デフォルトは ``False`` です。コマンドラインスイッチの :option:`-n` を使用すると、一時的にこの機能を有効にすることもできます。

   .. versionadded:: 1.0


.. Project information
   -------------------

プロジェクト情報
----------------

.. confval:: project

   .. The documented project s name.

   ドキュメントを書いているプロジェクト名です。


.. confval:: copyright

   .. A copyright statement in the style ``'2008, Author Name'``.

   ``'2008, Author Name'`` という形式の著作権表記です。


.. confval:: version

   .. The major project version, used as the replacement for ``|version|``.  For
      example, for the Python documentation, this may be something like ``2.6``.

   主要なプロジェクトのバージョンです。 ``|version|`` と置換されます。例えば、Pythonのドキュメントであれば、これは ``2.6`` になります。


.. confval:: release

   .. The full project version, used as the replacement for ``|release|`` and
      e.g. in the HTML templates.  For example, for the Python documentation, this
      may be something like ``2.6.0rc1``.

   完全なプロジェクトのバージョンです。HTMLのテンプレートなどの中の ``|release|`` と置換されます。例えば、Pthonのドキュメントの場合には、 ``2.6.0rc1`` のような文字列になります。

   .. If you don t need the separation provided between :confval:`version` and
      :confval:`release`, just set them both to the same value.

   :confval:`version` と :confval:`release` を分けて設定する必要がなければ、同じ文字列を入れてください。


.. confval:: language

   .. The code for the language the docs are written in.  Any text automatically
      generated by Sphinx will be in that language.  Also, in the LaTeX builder, a
      suitable language will be selected as an option for the *Babel* package.
      Default is ``None``, which means that no translation will be done.

   ドキュメントの言語のコードです。Sphinxが自動的に生成する文章が、その言語で出力されるようになります。LaTeXビルダーでは *Babel* パッケージのオプションとして、適切な言語が選択されます。デフォルトは ``None`` で翻訳はされません(訳注:英語で出力されます)

   .. versionadded:: 0.5

   .. Currently supported languages are:

   現在は以下の言語をサポートしています:

   .. * ``ca`` -- Catalan
      * ``cs`` -- Czech
      * ``de`` -- German
      * ``en`` -- English
      * ``es`` -- Spanish
      * ``fi`` -- Finnish
      * ``fr`` -- French
      * ``it`` -- Italian
      * ``nl`` -- Dutch
      * ``pl`` -- Polish
      * ``pt_BR`` -- Brazilian Portuguese
      * ``ru`` -- Russian
      * ``sl`` -- Slovenian
      * ``tr`` -- Turkish
      * ``uk_UA`` -- Ukrainian
      * ``zh_CN`` -- Simplified Chinese
      * ``zh_TW`` -- Traditional Chinese

   * ``ca`` -- カタロニア語
   * ``cs`` -- チェコ語
   * ``de`` -- ドイツ語
   * ``en`` -- 英語
   * ``es`` -- スペイン語
   * ``fi`` -- フィンランド語
   * ``fr`` -- フランス語
   * ``it`` -- イタリア語
   * ``nl`` -- オランダ語
   * ``pl`` -- ポーランド語
   * ``pt_BR`` -- ブラジルのポーランド語
   * ``ru`` -- ロシア語
   * ``sl`` -- スロベニア語
   * ``tr`` -- トルコ語
   * ``uk_UA`` -- ウクライナ語
   * ``zh_CN`` -- 簡体字中国語
   * ``zh_TW`` -- 繁体字中国語
   * ``ja`` -- 日本語


.. confval:: today
             today_fmt

   .. These values determine how to format the current date, used as the
      replacement for ``|today|``.

   これらの値は現在の日付をどのようにフォーマットするのか、というものを決めます。これは ``|today|`` を置き換える時に使用されます。

   .. * If you set :confval:`today` to a non-empty value, it is used.
      * Otherwise, the current time is formatted using :func:`time.strftime` and
        the format given in :confval:`today_fmt`.

   * もし :confval:`today` に空ではない値が設定されたらそれが使用されます。
   * そうでない場合には、 :confval:`today_fmt` で与えられたフォーマットを使い、 :func:`time.strftime` で生成された値が使用されます。

   .. The default is no :confval:`today` and a :confval:`today_fmt` of ``'%B %d,
      %Y'`` (or, if translation is enabled with :confval:`language`, am equivalent
      %format for the selected locale).

   デフォルトでは、 :confval:`today` は空で、 :confval:`today_fmt` には ``'%B %d, %Y'`` という値が設定されています。もしも :confval:`language` が設定されていて、翻訳機能が有効になっている場合には、選択された言語の %format が使用されます。


.. confval:: highlight_language

   .. The default language to highlight source code in.  The default is
      ``'python'``.  The value should be a valid Pygments lexer name, see
      :ref:`code-examples` for more details.

   ドキュメント内でハイライトするデフォルトの言語を設定します。デフォルト値は ``'python'`` です。値はPygmentsのlexer名として有効な名前でなければなりません。詳しくは :ref:`code-examples` を参照してください。

   .. versionadded:: 0.5


.. confval:: pygments_style

   .. The style name to use for Pygments highlighting of source code.  Default is
      ``'sphinx'``, which is a builtin style designed to match Sphinx' default
      style.

   Pygmentsがソースコードをハイライトする際に使用するスタイルの名前を設定します。デフォルトのスタイルはHTMLの出力のテーマで指定されたものになります。そうでない場合には ``'sphinx'`` になります。

   .. .. versionchanged:: 0.3
         If the value is a fully-qualified name of a custom Pygments style class,
         this is then used as custom style.

   .. versionchanged:: 0.3
      もし値として、Pygmentsのカスタムスタイルクラスの完全限定名が指定されると、カスタムスタイルとして使用されます。


.. confval:: add_function_parentheses

   .. A boolean that decides whether parentheses are appended to function and
      method role text (e.g. the content of ``:func:`input```) to signify that the
      name is callable.  Default is ``True``.

   関数とメソッドのロールテキストにカッコを付加するかどうかを決めるブール値です。ロールテキストというのは ``func:`input``` の ``input`` の箇所で、これをTrueにすると、その名前が呼び出し可能オブジェクトであるということが分かるようになります。デフォルトは ``True`` です。


.. confval:: add_module_names

   .. A boolean that decides whether module names are prepended to all
      :term:`object` names (for object types where a "module" of some kind is
      defined), e.g. for :rst:dir:`function` directives.  Default is ``True``.

   モジュール定義がされている場所にある、 :rst:dir:`function` などの :term:`オブジェクト` 名のタイトルのすべてに、モジュール名を付けるかどうかを決めるブール値です。デフォルトは ``True`` です。


.. confval:: show_authors

   .. A boolean that decides whether :rst:dir:`moduleauthor` and :rst:dir:`sectionauthor`
      directives produce any output in the built files.

   :rst:dir:`moduleauthor` と :rst:dir:`sectionauthor` ディレクティブの出力を、ビルドしたファイルに含めるかどうかのブール値です。


.. confval:: modindex_common_prefix

   .. A list of prefixes that are ignored for sorting the module index (e.g.,
      if this is set to ``['foo.']``, then ``foo.bar`` is shown under ``B``, not
      ``F``). This can be handy if you document a project that consists of a single
      package.  Works only for the HTML builder currently.   Default is ``[]``.

   モジュールのインデックスをソートする際に、無視するプリフィックスのリストです。例えば、 ``['foo.']`` が設定されると、 ``foo.bar`` に関しては ``foo.`` が削除されて ``bar`` になるため、 ``F`` ではなく、 ``B`` の項目として表示されます。プロジェクトの中のひとつのパッケージについてドキュメントを書く際にこの機能は便利に使えるでしょう。現在はHTMLビルダーについて使用されています。デフォルトは ``[]`` です。

   .. versionadded:: 0.6


.. confval:: trim_footnote_reference_space

   .. Trim spaces before footnote references that are necessary for the reST parser
      to recognize the footnote, but do not look too nice in the output.

   脚注参照の前のスペースをトリムします。スペースはreSTパーサーが脚注を見分けるためには必要ですが、出力されると見た目があまり良くありません。

   .. versionadded:: 0.6


.. confval:: trim_doctest_flags

   .. If true, doctest flags (comments looking like ``# doctest: FLAG, ...``) at
      the ends of lines are removed for all code blocks showing interactive Python
      sessions (i.e. doctests).  Default is true.  See the extension
      :mod:`~sphinx.ext.doctest` for more possibilities of including doctests.

   Trueのに設定されると、doctestを表す、Pythonのインタラクティブセッション形式のコードブロックの行末のdoctestのフラグ(``# doctest: FALG, ...`` ) が削除されます。デフォルトはTrueです。doctestに関連して可能なことはまだ多くありますので、詳しくはSphinx拡張モジュールの :mod:`~sphinx.ext.doctest` をご覧ください。

   .. versionadded:: 1.0


.. _html-options:

HTML出力のオプション
--------------------

.. Options for HTML output
   -----------------------

.. These options influence HTML as well as HTML Help output, and other builders
   that use Sphinx HTMLWriter class.

これらのオプションはHTMLと、HTMLヘルプ出力、SphinxのHTMLWriterクラスを利用しているその他のビルダーに対して影響を与えます。

.. confval:: html_theme

   .. The "theme" that the HTML output should use.  See the :doc:`section about
      theming <theming>`.  The default is ``'default'``.

   HTML出力で使用される"テーマ"です。詳しくは :doc:`テーマに関するセクション <theming>` を参照してください。デフォルト値は ``'default'`` です。

   .. versionadded:: 0.6


.. confval:: html_theme_options

   .. A dictionary of options that influence the look and feel of the selected
      theme.  These are theme-specific.  For the options understood by the builtin
      themes, see :ref:`this section <builtin-themes>`.

   選択したテーマのルックアンドフィールの設定を行うためのオプションのための辞書です。どのようなオプションがあるかは、テーマごとに異なります。組み込みのテーマで提供されるオプションに関しては、 :ref:`こちらのセクション <builtin-themes>` を参照してください。

   .. versionadded:: 0.6


.. confval:: html_theme_path

   .. A list of paths that contain custom themes, either as subdirectories or as
      zip files.  Relative paths are taken as relative to the configuration
      directory.

   カスタムテーマを含むパスへのリストです。パスはテーマを含むサブディレクトリか、もしくはzipファイルを指定することができます。相対パスを設定すると、コンフィグレーションディレクトリからの相対パスになります。

   .. versionadded:: 0.6


.. confval:: html_style

   .. The style sheet to use for HTML pages.  A file of that name must exist either
      in Sphinx :file:`static/` path, or in one of the custom paths given in
      :confval:`html_static_path`.  Default is the stylesheet given by the selected
      theme.  If you only want to add or override a few things compared to the
      theme s stylesheet, use CSS ``@import`` to import the theme s stylesheet.

   HTMLページで使用されるスタイルシートを設定します。ここで指定されたファイル名はSphinxの :file:`static/` か、 :confval:`html_static_path` で与えられたパスのどちらかの中になければなりません。デフォルトでは選択されたテーマで提供されるスタイルシートを使用します。テーマで使用しているスタイルシートに対して、要素を追加したり、一部の要素の上書きしたいだけの場合には、テーマで提供されるスタイルシートを ``@import`` するようにしてください。


.. confval:: html_title

   .. The "title" for HTML documentation generated with Sphinx own templates.
      This is appended to the ``<title>`` tag of individual pages, and used in the
      navigation bar as the "topmost" element.  It defaults to :samp:`'{<project>}
      v{<revision>} documentation'`, where the placeholders are replaced by the
      config values of the same name.

   Sphinx自身のテンプレートで生成されるHTMLドキュメントの"タイトル"を指定します。ここで設定された値は、それぞれのページ内の ``<title>`` タグに対して追加され、ナビゲーションバーの一番トップの要素として使用されます。デフォルト値は `'{<project>} v{<revision>} document'` となっています。内部のプレースホルダーは同名のコンフィグ値で置き換えられます。


.. confval:: html_short_title

   .. A shorter "title" for the HTML docs.  This is used in for links in the header
      and in the HTML Help docs.  If not given, it defaults to the value of
     :confval:`html_title`.

   HTMLドキュメントの短いタイトルを設定します。これはヘッダ内のリンク、HTMLヘルプのドキュメントで使用されます。設定されない場合には、 :confval:`html_title` と同じ値がデフォルトで使用されます。

   .. versionadded:: 0.4


.. confval:: html_logo

   .. If given, this must be the name of an image file that is the logo of the
      docs.  It is placed at the top of the sidebar; its width should therefore not
      exceed 200 pixels.  Default: ``None``.

   もし設定されると、ドキュメントのロゴ画像として使用されます。設定値は家像ファイル名でなければなりません。画像ファイルはサイドバーのトップに表示されます。画像サイズの幅は200ピクセル以下にしてください。デフォルト値は ``None`` です。

   .. .. versionadded:: 0.4.1
         The image file will be copied to the ``_static`` directory of the output
         HTML, so an already existing file with that name will be overwritten.

   .. versionadded:: 0.4.1
      画像ファイルはHTML出力時に ``_static`` ディレクトリにコピーされます。もし同名のファイルが存在する場合には上書きされます。


.. confval:: html_favicon

   .. If given, this must be the name of an image file (within the static path, see
      below) that is the favicon of the docs.  Modern browsers use this as icon for
      tabs, windows and bookmarks.  It should be a Windows-style icon file
      (``.ico``), which is 16x16 or 32x32 pixels large.  Default: ``None``.

   もし設定されると、ドキュメントのfaviconとして使用されます。設定値は静的なパスで、画像ファイルの名前でなければなりません。最近のブラウザでは、タブやウインドウ、ブックマークでこのfaviconの画像を利用します。これは 16x16 あるいは 32x32 の大きさの、Windowsの形式のアイコンファイル(``.ico``)でなければなりません。デフォルト値は ``None`` です。

   .. versionadded:: 0.4


.. confval:: html_static_path

   スタイルシートやスクリプトファイルといった、カスタムの静的ファイル類が含まれるパスのリストです。相対パスが設定されると、コンフィグレーションディレクトリからの相対パスとして処理されます。これらのファイルは、テーマが提供する静的ファイルをコピーした後にコピー処理が行われるため、 :file:`default.css` という名前のファイルがあると、テーマで使用する :file:`default.css` を上書きしてしまうので注意してください。

   .. A list of paths that contain custom static files (such as style sheets or
      script files).  Relative paths are taken as relative to the configuration
      directory.  They are copied to the output directory after the theme s static
      files, so a file named :file:`default.css` will overwrite the theme s
      :file:`default.css`.

   .. .. versionchanged:: 0.4
         The paths in :confval:`html_static_path` can now contain subdirectories.

   .. versionchanged:: 0.4
      :confval:`html_static_path` で指定されるパスにはサブディレクトリも含めることができます。

   .. .. versionchanged:: 1.0
         The entries in :confval:`html_static_path` can now be single files.

   .. versionchanged:: 1.0
      1.0からは、 :confval:`html_static_path` 内のエントリーに、単独のファイルを入れることができます。


.. confval:: html_last_updated_fmt

   .. If this is not the empty string, a 'Last updated on:' timestamp is inserted
      at every page bottom, using the given :func:`strftime` format.  Default is
      ``'%b %d, %Y'`` (or a locale-dependent equivalent).

   空の文字列以外が設定されると、すべてのページの最下部に挿入される '最終更新:' というタイムスタンプを出力されるためのテンプレートとして使用されます。テンプレートは :func:`strftime` で解釈できるフォーマットを指定してください。デフォルトは ``'%b %d, %Y'`` (ロケールによって異なります)になります。


.. confval:: html_use_smartypants
   
   .. If true, *SmartyPants* will be used to convert quotes and dashes to
      typographically correct entities.  Default: ``True``.

   Trueが設定されると、 *SmartyPants* は、印刷上で実体を修正するために引用文とダッシュを変換するのに使用されるでしょう。 デフォルトは ``True`` です。


.. confval:: html_add_permalinks

   .. If true, Sphinx will add "permalinks" for each heading and description
      environment as paragraph signs that become visible when the mouse hovers over
      them.  Default: ``True``.

   Trueが設定されると、Sphinxはそれぞれの見出しに "パーマリンク" を追加します。マウスをそれぞれのリンクの上に持って行くと、パラグラフサインが表示されます。デフォルトは ``True`` です。 

   .. .. versionadded:: 0.6
         Previously, this was always activated.

   .. versionadded:: 0.6
      以前は常に有効になってました。


.. confval:: html_sidebars

   .. Custom sidebar templates, must be a dictionary that maps document names to
      template names.  

   カスタムのサイドバーのテンプレートです。設定値は、ドキュメント名をキーに、テンプレート名を値に持つ辞書として設定します。

   .. The keys can contain glob-style patterns [1]_, in which case all matching
      documents will get the specified sidebars.  (A warning is emitted when a
      more than one glob-style pattern matches for any document.)

   キーには、globスタイルパターンを含めることができます。この場合、マッチしたすべてのドキュメントには、指定されたサイドバーが設定されます。1つ以上のglobスタイルのパターンがマッチすると、警告が出されます。

   .. The values can be either lists or single strings.

   辞書の値には、リストか、文字列を設定することができます。

   .. * If a value is a list, it specifies the complete list of sidebar templates
        to include.  If all or some of the default sidebars are to be included,
        they must be put into this list as well.
 
        The default sidebars (for documents that don't match any pattern) are:

   * もしも値がリストの場合には、含めるべきサイドバーテンプレートの完全なリストとして使用されます。もしもデフォルトサイドバーのすべて、もしくはいくつかが含まれていたら、それらはこのリストに含められます。

     デフォルトサイドバー(どのパターンにもマッチしなかったドキュメントで使用される)としては、以下の設定がされたものとして動作します:

     ``['localtoc.html', 'relations.html', 'sourcelink.html',
     'searchbox.html']``.

   .. * If a value is a single string, it specifies a custom sidebar to be added
        between the ``'sourcelink.html'`` and ``'searchbox.html'`` entries.  This
        is for compatibility with Sphinx versions before 1.0.

   * もしも値が文字列だった場合には、指定されたカスタムサイドバーが、 ``'sourcelink.html'`` と ``'searchbox.html'`` の間に追加されます。これは、Sphinxの1.0よりも前のバージョンと互換性があります。


   .. Builtin sidebar templates that can be rendered are:

   組み込みのサイドバーテンプレートは以下のようにビルドされます:

   .. * **localtoc.html** -- a fine-grained table of contents of the current document
      * **globaltoc.html** -- a coarse-grained table of contents for the whole
        documentation set, collapsed
      * **relations.html** -- two links to the previous and next documents
      * **sourcelink.html** -- a link to the source of the current document, if
        enabled in :confval:`html_show_sourcelink`
      * **searchbox.html** -- the "quick search" box

   * **localtoc.html** -- 現在のドキュメントの、詳細な目次
   * **globaltoc.html** -- ドキュメントセット全体に関する、荒い粒度の折りたたまれた目次
   * **relations.html** -- 前のドキュメントと、次のドキュメントへの２つのリンク
   * **sourcelink.html** -- もし :confval:`html_show_sourcelink` が有効にされている場合に、現在のドキュメントのソースへのリンク
   * **searchbox.html** -- "クイック検索"ボックス

   .. Example:

   サンプル::

      html_sidebars = {
         '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html'],
         'using/windows': ['windowssidebar.html', 'searchbox.html'],
      }

   .. This will render the custom template ``windowssidebar.html`` and the quick
      search box within the sidebar of the given document, and render the default
      sidebars for all other pages (except that the local TOC is replaced by the
      global TOC).

   これは ``windowssidebar.html`` カスタムテンプレートと、クイック検索ボックスをレンダリングし、指定されたドキュメントのサイドバーに組み込みます。その他のドキュメントに関しては、デフォルトサイドバーをビルドします。ただし、ローカルの目次はグローバルな目次に置き換えられます。

   .. .. versionadded:: 1.0
         The ability to use globbing keys and to specify multiple sidebars.

   .. versionadded:: 1.0
      globスタイルのキーが利用できるようになり、複数のサイドバーが設定できるようになりました。

   .. Note that this value only has no effect if the chosen theme does not possess
      a sidebar, like the builtin **scrolls** and **haiku** themes.

   これらの値は、組み込みの **scrolls** と **haiku** テーマのように、設定したテーマによっては効果がありません。


.. confval:: html_additional_pages

   .. Additional templates that should be rendered to HTML pages, must be a
      dictionary that maps document names to template names.

   HTMLページにレンダリングする、追加のHTMLテンプレートを指定します。設定値はドキュメント名をキーに、テンプレート名を値に持つ辞書として設定します。

   .. Example:

   サンプル::

      html_additional_pages = {
          'download': 'customdownload.html',
      }

   .. This will render the template ``customdownload.html`` as the page
      ``download.html``.

   この設定では、 ``customdownload.html`` というテンプレートが ``download.html`` というページにレンダリングされます。

   .. note::

      .. Earlier versions of Sphinx had a value called :confval:`html_index` which
         was a clumsy way of controlling the content of the "index" document.  If
         you used this feature, migrate it by adding an ``'index'`` key to this
         setting, with your custom template as the value, and in your custom
         template, use :

      Sphinxの昔のバージョンには :confval:`html_index` と呼ばれる値を持っていて、これだけが唯一 "index" ドキュメントのコンテンツを制御する方法でした。もしこの機能を使っていた場合には、 ``html_additional_pages`` に ``index`` というキーを追加して、それまで使用していたカスタムテンプレートを値として設定します。その後、カスタムテンプレートを下記のように書き換えます:

      .. {% extend "defindex.html" %}
         {% block tables %}
         ... old template content ...
         {% endblock %}

      .. code-block:: python

         {% extend "defindex.html" %}
         {% block tables %}
         ... 古いテンプレートの内容 ...
         {% endblock %}


.. confval:: html_domain_indices

   .. If true, generate domain-specific indices in addition to the general index.
      For e.g. the Python domain, this is the global module index.  Default is
      ``True``.

   真に設定されると、ドメイン限定の索引を通常の索引に追加します。例えば、Pythonドメインの場合には、グローバルなモジュールの索引が該当します。デフォルトでは ``True`` です。

   .. This value can be a bool or a list of index names that should be generated.
      To find out the index name for a specific index, look at the HTML file name.
      For example, the Python module index has the name ``'py-modindex'``.

   この設定値にはブール型か、生成すべき索引名のリストを設定することができます。特定の索引名をしていると、HTMLのファイル名を探しに行きます。例えば、Pythonのモジュール索引は ``'py-modindex'`` という名前を持ちます。

   .. versionadded:: 1.0


.. confval:: html_use_modindex

   .. If true, add a module index to the HTML documents.   Default is ``True``.

   もしTrueに設定されると、HTMLドキュメントにモジュールの索引を挿入します。デフォルトは ``True`` です。

   .. .. deprecated:: 1.0
         Use :confval:`html_domain_indices`.

   .. deprecated:: 1.0
      :confval:`html_domain_indices` を使用してください。


.. confval:: html_use_index

   ..   If true, add an index to the HTML documents.  Default is ``True``.

   Trueが設定されると、HTMLドキュメントに索引を追加します。デフォルトは ``True`` です。

   .. versionadded:: 0.4


.. confval:: html_split_index

   .. If true, the index is generated twice: once as a single page with all the
      entries, and once as one page per starting letter.  Default is ``False``.

   もしTrueが設定されると、索引が２回作成されます。一つ目は全てのエントリーを含む索引です。2つめは最初の文字ごとにページ分割された索引になります。デフォルトは ``False`` です。

   .. versionadded:: 0.4


.. confval:: html_copy_source

   .. If true, the reST sources are included in the HTML build as
      :file:`_sources/{name}`.  The default is ``True``.

   Trueに設定されると、 HTMLのビルド時に :file:`_sources/{name}` としてreSTのソースファイルが含まれるようになります。デフォルトは ``True`` です。

   .. warning::

      .. If this config value is set to ``False``, the JavaScript search function
         will only display the titles of matching documents, and no excerpt from
         the matching contents.

      もしもこの設定値が ``False`` に設定されると、 JavaScriptの検索機能を使用したときに、マッチしたドキュメントのタイトルしか表示できなくなります。マッチした文章の内容を表示することはできません。


.. confval:: html_show_sourcelink

   .. If true (and :confval:`html_copy_source` is true as well), links to the
      reST sources will be added to the sidebar.  The default is ``True``.

   :confval:`html_copy_source` がTrueに設定されていて、かつ、この設定値もTrueに設定された場合に、サイドバーにreSTのソースファイルへのリンクを表示します。デフォルト値は ``True`` です。

   .. versionadded:: 0.6


.. confval:: html_use_opensearch

   .. If nonempty, an `OpenSearch <http://opensearch.org>` description file will be
      output, and all pages will contain a ``<link>`` tag referring to it.  Since
      OpenSearch doesnt support relative URLs for its search page location, the
      value of this option must be the base URL from which these documents are
      served (without trailing slash), e.g. ``"http://docs.python.org"``.  The
      default is ``''``.

   もしこの値が空でなかったら、 `OpenSearch <http://opensearch.org>` の説明ファイルが生成され、すべてのページにこのファイルを参照する ``<link>`` タグが含まれるようになります。OpenSearchが検索ページの位置を示すのに、相対パスをサポートしていないので、 この値はこの設定値の値は、これらのドキュメントが提供されるベースのURLにします。最後のスラッシュ(/)は不要です。例えば、Pythonのドキュメントであれば、 ``"http://docs.python.org"`` とします。デフォルト値は ``''`` です。


.. confval:: html_file_suffix

   .. If nonempty, this is the file name suffix for generated HTML files.  The
      default is ``".html"``.

   もし空でなければ、HTMLファイルを生成するときに、ファイル名の末尾に追加される文字列として使用されます。デフォルトでは ``".html"`` となります。

   .. versionadded:: 0.4


.. confval:: html_link_suffix

   .. Suffix for generated links to HTML files.  The default is whatever
      :confval:`html_file_suffix` is set to; it can be set differently (e.g. to
      support different web server setups).

   HTMLファイルに対して生成されるリンクの末尾に付けられる文字列です。デフォルト値としては :confval:`html_file_suffix` の値が設定されます。他のウェブサーバのセットアップをサポートする場合などに、別の値を設定することができます。

   .. versionadded:: 0.6


.. confval:: html_translator_class

   .. A string with the fully-qualified name of a HTML Translator class, that is, a
      subclass of Sphinx :class:`~sphinx.writers.html.HTMLTranslator`, that is used
      to translate document trees to HTML.  Default is ``None`` (use the builtin
      translator).

   HTML変換クラスへの完全限定名(FQN)を表す文字列です。これはSphinxの :class:`~sphinx.writers.html.HTMLTranslator` のサブクラスです。これはドキュメントツリーをHTMLに変換するのに使用されます。デフォルト値は ``None`` で、組み込みのトランスレータが使用されます。


.. confval:: html_show_copyright

   .. If true, "(C) Copyright ..." is shown in the HTML footer. Default is ``True``.

   もしTrueに設定されると、 "(C) Copyright ..." という文字列をHTMLのフッターに出力します。デフォルトは ``True`` です。

   .. versionadded:: 1.0


.. confval:: html_show_sphinx

   .. If true, "Created using Sphinx" is shown in the HTML footer.  Default is
      ``True``.

   もしTrueが設定されると、 "このドキュメントは Sphinx 0.6.2 で生成しました。" という説明がHTMLのフッターに追加されます。デフォルトは ``True`` です。

   .. versionadded:: 0.4


.. confval:: html_output_encoding

   .. Encoding of HTML output files. Default is ``'utf-8'``.  Note that this
      encoding name must both be a valid Python encoding name and a valid HTML
      ``charset`` value.

   HTML出力ファイルのエンコーディングを指定します。デフォルトは ``'utf-8'`` です。このエンコーディング名Pythonのエンコーディング指定と、HTMLの ``charset`` の両方で使用できる名前でなければなりません。

   .. versionadded:: 1.0


.. confval:: html_compact_lists

   .. If true, list items containing only a single paragraph will not be rendered
      with a ``<p>`` element.  This is standard docutils behavior.  Default:
      ``True``.

   もし真に設定されると、1つのパラグラフのみを含むリストのアイテムは ``<p>`` エレメントを使ってレンダリングされなくなります。これは標準のdocutilsの振る舞いと同じです。デフォルト値は ``True`` です。

   .. versionadded:: 1.0

.. confval:: html_secnumber_suffix

   .. Suffix for section numbers.  Default: ``". "``.  Set to ``" "`` to suppress
      the final dot on section numbers.

   セクション番号のサフィックスです。デフォルトは ``". "`` です。 ``" "`` を指定すると、セクション番号の末尾のピリオドが表示されなくなります。

   .. versionadded:: 1.0


.. confval:: htmlhelp_basename

   .. Output file base name for HTML help builder.  Default is ``'pydoc'``.

   HTMLヘルプビルダーについて、出力ファイルのベース名を設定します。デフォルト値は ``'pydoc'`` です。


.. Options for epub output
   -----------------------

.. _epub-options:

epub出力のオプション
--------------------

.. These options influence the epub output.  As this builder derives from the HTML
   builder, the HTML options also apply where appropriate.  The actual values for
   some of the options is not really important, they just have to be entered into
   the `Dublin Core metadata <http://dublincore.org/>`_.

これらのオプションを設定すると、epub出力に影響を与えます。このepubビルダーはHTMLビルダーを継承しているため、HTML出力のオプションも適切に反映されます。いくつか、ビルダーへの影響はないが、 `ダブリン・コア・メタデータ <http://dublincore.org/>`_ の中の値として使用される設定値もあります。

.. confval:: epub_basename

   .. The basename for the epub file.  It defaults to the :confval:`project` name.

   epubファイルのベース名です。デフォルトでは :confval:`project` 名が使用されます。


.. confval:: epub_theme

   .. The HTML theme for the epub output.  Since the default themes are not
      optimized for small screen space, using the same theme for HTML and epub
      output is usually not wise.  This defaults to ``'epub'``, a theme designed to
      save visual space.

   epub出力時のHTMLデータｍで素。デフォルトのテーマは小さい画面サイズで見るような調整がされおらず、HTMLのテーマと同じになっていて、epub出力は賢くありません。デフォルトは ``'epub'`` で、このテーマはビジュアルなための空間を減らすようにデザインされています。


.. confval:: epub_title

   .. The title of the document.  It defaults to the :confval:`html_title` option
      but can be set independently for epub creation.

   ドキュメントのタイトルです。デフォルトでは :confval:`html_title` オプションと同じですが、epub作成時のみの名前が設定できるようになります。


.. confval:: epub_author

   .. The author of the document.  This is put in the Dublin Core metadata.  The
      default value is ``'unknown'``.

   ドキュメントの著者名です。この設定値はダブリン・コア・メタデータの中に出力されます。デフォルト値は ``'unknown'`` です。


.. confval:: epub_language

   .. The language of the document.  This is put in the Dublin Core metadata.  The
      default is the :confval:`language` option or ``'en'`` if unset.

   ドキュメントの言語設定です。この設定値はダブリン・コア・メタデータの中に出力されます。デフォルトでは、 :confval:`language` オプションが設定されるか、もしそれも設定されていなければ ``'en'`` になります。


.. confval:: epub_publisher

   .. The publisher of the document.  This is put in the Dublin Core metadata.  You
      may use any sensible string, e.g. the project homepage.  The default value is
      ``'unknown'``.

   ドキュメントの出版社情報になります。この設定値はダブリン・コア・メタデータの中に出力されます。プロジェクトのホームページなど、なんらかの意味のある文字列を入れることになるでしょう。デフォルト値は ``'unknown'`` です。


.. confval:: epub_copyright

   .. The copyright of the document.  It defaults to the :confval:`copyright`
      option but can be set independently for epub creation.

   ドキュメントの著作権表示です。デフォルトでは :confval:`copyright` オプションと同じですが、epub作成時のみの名前が設定できるようになります。


.. confval:: epub_identifier

   .. An identifier for the document.  This is put in the Dublin Core metadata.
      For published documents this is the ISBN number, but you can also use an
      alternative scheme, e.g. the project homepage.  The default value is
      ``'unknown'``.

   ドキュメントの識別子です。この設定値はダブリン・コア・メタデータの中に出力されます。出版物であれば、ISBNコードを入れることになりますが、そうでない場合にはプロジェクトのウェブサイトなどの別のスキーマを使うこともできます。デフォルト値は ``'unknown'`` です。


.. confval:: epub_scheme

   .. The publication scheme for the :confval:`epub_identifier`.  This is put in
      the Dublin Core metadata.  For published books the scheme is ``'ISBN'``.  If
      you use the project homepage, ``'URL'`` seems reasonable.  The default value
      is ``'unknown'``.

   :confval:`epub_identifier` に使用する、出版物のスキーマです。この設定値はダブリン・コア・メタデータの中に出力されます。出版物であれば、 ``'ISBN'`` になります。プロジェクトのウェブサイトのURLを指定するのであれば、 ``'URL'`` を使うのが良いでしょう。デフォルト値は ``'unknown'`` です。


.. confval:: epub_uid

   .. A unique identifier for the document.  This is put in the Dublin Core
      metadata.  You may use a random string.  The default value is ``'unknown'``.

   ドキュメントのユニークな識別子です。この設定値はダブリン・コア・メタデータの中に出力されます。ランダムな文字列を使うことが出来ます。デフォルト値は ``'unknown'`` です。


.. confval:: epub_pre_files

   .. Additional files that should be inserted before the text generated by
      Sphinx. It is a list of tuples containing the file name and the title.

   Sphinxによって生成されたテキストの前に追加されるファイル群を指定します。ファイル名とタイトルが組になったタプルを含む配列となります。

   .. Example:

   サンプル::

      epub_pre_files = [
          ('index.html', 'Welcome'),
      ]

   .. The default value is ``[]``.

   デフォルト値は ``[]`` です。


.. confval:: epub_post_files

   .. Additional files that should be inserted after the text generated by Sphinx.
      It is a list of tuples containing the file name and the title.  The default
      value is ``[]``.

   Sphinxによって生成されたテキストの後ろに追加されるファイル群を指定します。ファイル名とタイトルが組になったタプルを含む配列となります。デフォルト値は ``[]`` です。


.. confval:: epub_exclude_files

   .. A list of files that are generated/copied in the build directory but should
      not be included in the epub file.  The default value is ``[]``.

   buildディレクトリには生成されたりコピーされるが、epubファイルの中には含めないファイルのリストを指定します。デフォルト値は ``[]`` です。


.. confval:: epub_tocdepth


   .. The depth of the table of contents in the file :file:`toc.ncx`.  It should
      be an integer greater than zero.  The default value is 3.  Note: A deeply
      nested table of contents may be difficult to navigate.

   :file:`toc.ncx` という目次ファイルに含める、セクションタイトルの階層数を指定します。1以上の数値でなければなりません。デフォルト値は ``3`` です。あまり深いと、ユーザが見て辿るのが難しくなることに注意しましょう。


.. _latex-options:

LaTeX出力のオプション
-----------------------

.. Options for LaTeX output
   ------------------------

.. These options influence LaTeX output.

これらのオプションはLaTeX出力に影響を与えます。

.. confval:: latex_documents

   .. This value determines how to group the document tree into LaTeX source files.
      It must be a list of tuples ``(startdocname, targetname, title, author,
      documentclass, toctree_only)``, where the items are:

   この値はドキュメントツリーをどのようにグループ化するかを決定します。これは、 ``(startdocname, targetname, title, author, documentclass, toctree_only)`` というタプルのリストでなければなりません。それぞれの項目は次のような意味を持ちます。

   .. * *startdocname*: document name that is the "root" of the LaTeX file.  All
        documents referenced by it in TOC trees will be included in the LaTeX file
        too.  (If you want only one LaTeX file, use your :confval:`master_doc`
        here.)
      * *targetname*: file name of the LaTeX file in the output directory.
      * *title*: LaTeX document title.  Can be empty to use the title of the
        *startdoc*.  This is inserted as LaTeX markup, so special characters like a
        backslash or ampersand must be represented by the proper LaTeX commands if
        they are to be inserted literally.
      * *author*: Author for the LaTeX document.  The same LaTeX markup caveat as
        for *title* applies.  Use ``\and`` to separate multiple authors, as in:
        ``'John \and Sarah'``.
      * *documentclass*: Must be one of ``'manual'`` or ``'howto'``.  Only "manual"
        documents will get appendices.  Also, howtos will have a simpler title
        page.
      * *toctree_only*: Must be ``True`` or ``False``.  If ``True``, the *startdoc*
        document itself is not included in the output, only the documents
        referenced by it via TOC trees.  With this option, you can put extra stuff
        in the master document that shows up in the HTML, but not the LaTeX output.

   * *startdocname*: LaTeXファイルの"ルート"となるドキュメントの名前です。このファイルから参照されたすべてのドキュメントはLaTeXファイルの中のTOCツリーにも含まれるようになります。もしも1つのファイルをマスターにしたLaTeXファイルにしたい場合には、 :confval:`master_doc` で設定した値をここに指定して下さい。
   * *targetname*: 出力ディレクトリに出力される、LaTeXのファイル名です。
   * *title*: LaTeXのドキュメントのタイトルです。 *startdoc* の名前を使用する場合には、空にすることも可能です。この設定値はLaTeXのマークアップとして挿入されます。バックスラッシュやアンパサンドなどの特別な文字を入れる場合には、適切なLaTeXコマンドを使って表現しなければなりません。
   * *author*: LaTeXドキュメントの著者です。これも *title* と同じように、LaTeXマークアップとして挿入されます。複数人の名前を書く場合には、著者名の区切りに ``\and`` を使用して、 ``'John \and Sarah'`` のように書きます。
   * documentclass*: ``'manual'`` か ``'howto'`` を使用します。 "manual"ドキュメントにはAppendixが追加されます。"howto"はシンプルなタイトルページが追加されます。
   * toctree_only*: ``True`` か ``False`` を設定します。もしも ``True`` を設定した場合には *startdoc* ドキュメント自身は出力には含まれず、そのドキュメントのTOCツリーで参照されたドキュメントだけになります。このオプションを付けると、HTMLではマスタードキュメント内の項目も表示させて、LaTeXでは出さない、ということができます。

   .. .. versionadded:: 0.3
         The 6th item ``toctree_only``.  Tuples with 5 items are still accepted.

   .. versionadded:: 0.3
      6番目の ``toctree_only`` が追加されました。現在でも、5要素のタプルを指定することもできます。


.. confval:: latex_logo

   .. If given, this must be the name of an image file (relative to the
      configuration directory) that is the logo of the docs.  It is placed at the
      top of the title page.  Default: ``None``.

   このオプションが設定されると、ドキュメントのロゴとして使用されます。指定されるのは、設定ディレクトリからの相対パスの、イメージファイル名でなければなりません。タイトルページのトップに表示されます。デフォルトでは ``None`` です。


.. confval:: latex_use_parts

   .. If true, the topmost sectioning unit is parts, else it is chapters.  Default:
      ``False``.

   Trueが設定されると、一番上位のセクションの単位がpartになります。そうでない場合はchapterになります。デフォルトは ``False`` です。

   .. versionadded:: 0.3

.. confval:: latex_appendices

   .. A list of document names to append as an appendix to all manuals.

   すべてのマニュアルのappendixに追加されるドキュメント名のリストです。

.. confval:: latex_domain_indices

   .. If true, generate domain-specific indices in addition to the general index.
      For e.g. the Python domain, this is the global module index.  Default is
      ``True``.

   Trueが設定されると、ドメインに特化した索引が、全体の索引に追加されます。Pythonのドメインの場合には、グローバルなモジュールの索引が該当します。デフォルトは ``True`` です。

   .. This value can be a bool or a list of index names that should be generated,
      like for :confval:`html_domain_indices`.

   :confval:`html_domain_indices` と同じく、この設定値にはブール型か、生成すべき索引名のリストを設定することができます。

   .. versionadded:: 1.0


.. confval:: latex_use_modindex

   .. If true, add a module index to LaTeX documents.   Default is ``True``.

   Trueが設定されると、モジュールの索引がLaTeXのドキュメントに追加されます。デフォルトでは ``True`` です。

   .. .. deprecated:: 1.0
         Use :confval:`latex_domain_indices`.

   .. deprecated:: 1.0
      :confval:`latex_domain_indices` を使用して下さい。


.. confval:: latex_elements

   .. versionadded:: 0.5

   .. A dictionary that contains LaTeX snippets that override those Sphinx usually
      puts into the generated ``.tex`` files.

   LaTeXのスニペットコードが含まれる辞書です。Sphinxはこれらのスニペットを使って、生成された ``.tex`` ファイルの中の要素をオーバーライドします。

   .. Keep in mind that backslashes must be doubled in Python string literals to
      avoid interpretation as escape sequences.

   Pythonの文字列中のバックスラッシュは、エスケープシーケンスとして解釈されるのを避けるために、2重に書く必要があります。

   .. * Keys that you may want to override include:

        ``'papersize'``
           Paper size option of the document class (``'a4paper'`` or
           ``'letterpaper'``), default ``'letterpaper'``.
        ``'pointsize'``
           Point size option of the document class (``'10pt'``, ``'11pt'`` or
           ``'12pt'``), default ``'10pt'``.
        ``'babel'``
           "babel" package inclusion, default ``'\\usepackage{babel}'``.
        ``'fontpkg'``
           Font package inclusion, default ``'\\usepackage{times}'`` (which uses
           Times and Helvetica).  You can set this to ``''`` to use the Computer
           Modern fonts.
        ``'fncychap'``
           Inclusion of the "fncychap" package (which makes fancy chapter titles),
           default ``'\\usepackage[Bjarne]{fncychap}'`` for English documentation,
           ``'\\usepackage[Sonny]{fncychap}'`` for internationalized docs (because
           the "Bjarne" style uses numbers spelled out in English).  Other
           "fncychap" styles you can try include "Lenny", "Glenn", "Conny" and
           "Rejne".  You can also set this to ``''`` to disable fncychap.
        ``'preamble'``
           Additional preamble content, default empty.
        ``'footer'```
           Additional footer content (before the indices), default empty.

   * オーバーライドするキーには、次のようなものがあります:

     ``'papersize'``
        document classの用紙サイズのオプションです。 ``'a4paper'`` か ``'letterpaper'`` が指定できます。デフォルトは ``'letterpaper'`` です。
     ``'pointsize'``
        document classのポイントサイズのオプションです。 ``'10pt'`` か ``'11pt'``, ``'12pt'`` が指定できます。デフォルトは ``'10pt'`` です。
     ``'babel'``
        "babel" パッケージの挿入をします。デフォルトは ``'\\usepackage{babel}'`` です。
     ``'fontpkg'``
        フォントパッケージの挿入をします。デフォルトはTimesとHelveticaを使用する ``'\\usepackage{times}'`` です。 ``''`` を指定すると、Computer Modernフォントが利用されます。
     ``'fncychap'``
        "fncychap"パッケージの挿入をします。これは"fancy chapter tilte"処理を行います。英語のドキュメントのデフォルトは ``'\\usepackage[Bjarne]{fncychap}'`` で、国際化されたドキュメントのデフォルトは ``'\\usepackage[Sonny]{fncychap}'`` になります。"Bjarne" は数字を英語表記します。他にも"fncychap"スタイルには、 "Lenny", "Glenn", "Conny", "Rejne" を含めることができます。 ``''`` を指定すると、fncychap処理を無効にすることができます。
     ``'preamble'``
        前書き(preamble)を追加します。デフォルトでは追加しません。
     ``'footer'```
        フッターのコンテンツ(索引の前)を追加します。デフォルトでは追加しません。
        Additional footer content (before the indices), default empty.

   .. * Keys that don't need be overridden unless in special cases are:
   
        ``'inputenc'``
           "inputenc" package inclusion, default
           ``'\\usepackage[utf8]{inputenc}'``.
        ``'fontenc'``
           "fontenc" package inclusion, default ``'\\usepackage[T1]{fontenc}'``.
        ``'maketitle'``
           "maketitle" call, default ``'\\maketitle'``.  Override if you want to
           generate a differently-styled title page.
        ``'tableofcontents'``
           "tableofcontents" call, default ``'\\tableofcontents'``.  Override if
           you want to generate a different table of contents or put content
           between the title page and the TOC.
        ``'printindex'``
           "printindex" call, the last thing in the file, default
           ``'\\printindex'``.  Override if you want to generate the index
           differently or append some content after the index.

   * 次のキーは、特別な場合でなければ、オーバーライドする必要はありません:

        ``'inputenc'``
           "inputenc"パッケージを挿入します。デフォルトでは ``'\\usepackage[utf8]{inputenc}'`` になります。
        ``'fontenc'``
           "fontenc"パッケージを挿入します。デフォルトでは ``'\\usepackage[T1]{fontenc}'`` になります。
        ``'maketitle'``
           "maketitle"呼び出しです。デフォルトでは ``'\\maketitle'`` が使用されます。異なるスタイルのタイトルページを生成したい場合には、オーバーライドしてください。
        ``'tableofcontents'``
           "tableofcontents"呼び出しです。デフォルトでは ``'\\tableofcontents'`` です。異なるスタイルの目次を生成したい場合や、タイトルページと目次の間に何かコンテンツを追加したい場合にはオーバーライドしてください。
        ``'printindex'``
           "printindex"呼び出しです。ファイルの最後の項目になります。デフォルトでは ``'\\printindex'`` になります。異なる索引を生成したい場合や、索引の後に何かコンテンツを追加したい場合にはオーバーライドしてください。

   .. * Keys that are set by other options and therefore should not be overridden are:

   * 次のようなキーは、他のオプションによって指定されるため、オーバーライドすべきではありません:

     ``'docclass'``
     ``'classoptions'``
     ``'title'``
     ``'date'``
     ``'release'``
     ``'author'``
     ``'logo'``
     ``'releasename'``
     ``'makeindex'``
     ``'shorthandoff'``


.. confval:: latex_docclass

   .. A dictionary mapping ``'howto'`` and ``'manual'`` to names of real document
      classes that will be used as the base for the two Sphinx classes.  Default
      is to use ``'article'`` for ``'howto'`` and ``'report'`` for ``'manual'``.

   ``'howto'`` と ``'manual'`` から実際にSphinxのクラスとして使われるdocument classへのマッピングをする辞書です。デフォルトでは ``'howto'`` には ``'article'``, ``'manual'`` には ``'report'`` が使われます。

   .. versionadded:: 1.0

.. confval:: latex_additional_files

   .. A list of file names, relative to the configuration directory, to copy to the
      build directory when building LaTeX output.  This is useful to copy files
      that Sphinx doesn't copy automatically, e.g. if they are referenced in custom
      LaTeX added in ``latex_elements``.  Image files that are referenced in source
      files (e.g. via ``.. image::``) are copied automatically.

   設定ディレクトリからの相対パスのファイル名のリストです。LaTeX出力のビルドが行われる時にビルドディレクトリに出力されます。 ``latex_elements`` などで参照していて、Sphinxが自動ではコピーしないファイルのコピーに使うと便利です。なお、ソースファイルの中で ``.. image::`` を使って参照しているイメージファイルは、自動的にコピーされます。

   .. You have to make sure yourself that the filenames don't collide with those of
      any automatically copied files.

   ファイルの自動コピー時に、ファイル名が衝突しないように設定する必要があります。

   .. versionadded:: 0.6


.. confval:: latex_preamble

   .. Additional LaTeX markup for the preamble.

   前書き(preamble)のLaTeXのマークアップを追加します。

   .. .. deprecated:: 0.5
         Use the ``'preamble'`` key in the :confval:`latex_elements` value.

   .. deprecated:: 0.5
      :confval:`latex_elements` の ``'papersize'`` を使用して下さい。

.. confval:: latex_paper_size

   .. The output paper size (``'letter'`` or ``'a4'``).  Default is ``'letter'``.

   出力する用紙サイズのオプションです。 ``'a4paper'`` か ``'letterpaper'`` が指定できます。デフォルトは ``'letterpaper'`` です。

   .. .. deprecated:: 0.5
         Use the ``'papersize'`` key in the :confval:`latex_elements` value.

   .. deprecated:: 0.5
      :confval:`latex_elements` の ``'papersize'`` を使用して下さい。

.. confval:: latex_font_size

   .. The font size ('10pt', '11pt' or '12pt'). Default is ``'10pt'``.

   フォントサイズです。 ``'10pt'`` か ``'11pt'``, ``'12pt'`` が指定できます。デフォルトは ``'10pt'`` です。

   .. .. deprecated:: 0.5
         Use the ``'pointsize'`` key in the :confval:`latex_elements` value.

   .. deprecated:: 0.5
      :confval:`latex_elements` の ``'pointsize'`` を使用して下さい。


.. _man-options:

manページ出力のオプション
-------------------------

.. Options for manual page output
   ------------------------------

.. These options influence manual page output.

これらのオプションは、manページ出力に影響を与えます。

.. confval:: man_pages

   .. This value determines how to group the document tree into manual pages.  It
      must be a list of tuples ``(startdocname, name, description, authors,
      section)``, where the items are:

   このオプションでは、ドキュメントツリーをどのようにグループ化してmanページに入れるか、というのを指定します。この設定は、 ``(startdocname, name, description, authors, section)`` というタプルのリストでなければなりません。それぞれの項目は次のような意味を持ちます。

   .. * *startdocname*: document name that is the "root" of the manual page.  All
        documents referenced by it in TOC trees will be included in the manual file
        too.  (If you want one master manual page, use your :confval:`master_doc`
        here.)
      * *name*: name of the manual page.  This should be a short string without
        spaces or special characters.  It is used to determine the file name as
        well as the name of the manual page (in the NAME section).
      * *description*: description of the manual page.  This is used in the NAME
        section.
      * *authors*: A list of strings with authors, or a single string.  Can be
        an empty string or list if you do not want to automatically generate
        an AUTHORS section in the manual page.
      * *section*: The manual page section.  Used for the output file name as well
        as in the manual page header.

   * *startdocname*: manページの"ルート"となるドキュメントの名前です。このファイルから参照されたすべてのドキュメントはLaTeXファイルの中のTOCツリーにも含まれるようになります。もしも1つのファイルをマスターにしたmanページにしたい場合には、 :confval:`master_doc` で設定した値をここに指定して下さい。
   * *name*: manページの名前です。これには、スペースや特別な文字を含まない、短い文字列を指定します。この項目は出力ファイル名と、manページの名前(NAMEセクション内)として使用されます。
   * *description*: manページの説明です。これはNAMEセクション内で使用されます。
   * *author*: 著者名の文字列のリスト、もしくは単一の文字列です。manページのAUTHORSセクションを自動的に生成したくない場合には、空の文字列や空の配列を指定することもできます。
   * *section*: manページのセクションです。出力ファイル名や、manページのヘッダー内で使われます。

   .. versionadded:: 1.0


.. .. rubric:: Footnotes
   .. [1] A note on available globbing syntax: you can use the standard shell
          constructs ``*``, ``?``, ``[...]`` and ``[!...]`` with the feature that
          these all don't match slashes.  A double star ``**`` can be used to match
          any sequence of characters *including* slashes.

.. rubric:: 脚注
.. [1] 使用できるglob文法: 通常のシェルで使用する ``*``, ``?``, ``[...]``, ``[!...]`` は使用できます。これらはすべてスラッシュにはマッチしません。 ``**`` を使うと、スラッシュを **含む** あらゆる文字列にマッチします。


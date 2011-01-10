.. Invocation of sphinx-build
   ==========================

.. _invocation:

sphinx-buildの起動
==================

.. The :program:`sphinx-build` script builds a Sphinx documentation set.  It is
   called like this::

     $ sphinx-build [options] sourcedir builddir [filenames]

Sphinxのドキュメント群を生成するのは、 :program:`sphinx-build` というプログラムです。これは次のように実行します::

     $ sphinx-build [オプション] ソースディレクトリ ビルドディレクトリ [ファイル名]

.. where *sourcedir* is the :term:`source directory`, and *builddir* is the
   directory in which you want to place the built documentation.  Most of the time,
   you don't need to specify any *filenames*.

**sourcedir** には :term:`ソースディレクトリ` が、 **builddir** にはビルドしたドキュメントを置きたいディレクトリを指定します。ほとんどの場合、 **ファイル名** は指定する必要はありません。

.. The :program:`sphinx-build` script has several options:

:program:`sphinx-build` スクリプトは次のようなオプションを持っています:

.. option:: -b buildername

   .. The most important option: it selects a builder.  The most common builders
      are:

   ビルダーを選択する、もっとも重要なオプションです。一般的に使用されるビルダーには次のような物があります。

   **html**
      HTMLページをビルドします。デフォルトのビルダーです。

   .. Build HTML pages.  This is the default builder.

   **dirhtml**
      HTMLページをビルドしますが、ドキュメントごとにディレクトリが生成されます。ウェブサーバで提供する場合に、 ``.html`` がURLに付かないようにして、URLが分かりやすくなります。

   .. Build HTML pages, but with a single directory per document.  Makes for
      prettier URLs (no ``.html``) if served from a webserver.

   **singlehtml**
      すべてのコンテンツが含まれる、単一のHTMLを生成します。

   .. Build a single HTML with the whole content.

   **htmlhelp**, **qthelp**, **devhelp**, **epub**
      フォーマットごとに、ドキュメントのコレクションを構築するのに必要な情報と一緒にHTMLファイルをビルドします。

   .. Build HTML files with additional information for building a documentation
      collection in one of these formats.

   **latex**
      :program:`pdflatex` を使用して、PDFドキュメントにコンパイルできるような、LaTeXのソースをビルドします。

   .. Build LaTeX sources that can be compiled to a PDF document using
      :program:`pdflatex`.

   **man**
      UNIX系システムで利用される、groffフォーマットのmanページをビルドします。

   .. Build manual pages in groff format for UNIX systems.

   **text**
      プレーンテキストファイルをビルドします。

   .. Build plain text files.

   **doctest**
      もしも :mod:`~sphinx.ext.doctest` 拡張が有効になっている場合には、ドキュメント内のすべてのdoctestを実行します。

   .. Run all doctests in the documentation, if the :mod:`~sphinx.ext.doctest`
      extension is enabled.

   **linkcheck**
      すべての外部リンク先が存在しているか確認をします。

   .. Check the integrity of all external links.

   .. See :ref:`builders` for a list of all builders shipped with Sphinx.
      Extensions can add their own builders.

   Sphinxと一緒に提供されている、すべてのビルダーのリストは :ref:`builders` を参照してください。また、新しいビルダーを追加する拡張機能もあります。

.. option:: -a

   .. If given, always write all output files.  The default is to only write output
      files for new and changed source files.  (This may not apply to all
      builders.)

   もしこのオプションが設定されると、すべての出力ファイルを書き出します。デフォルトでは新規に作成されたり、変更のあったソースファイルに関連する出力ファイルだけを出力します。このオプションはすべてのビルダーに適応するわけではありません。

.. option:: -E

   .. Don't use a saved :term:`environment` (the structure caching all
      cross-references), but rebuild it completely.  The default is to only read
      and parse source files that are new or have changed since the last run.

   保存されている :term:`環境` を使用しないで、完全に再構築する場合に利用します。環境にはクロスリファレンスの構造を保持しています。デフォルトでは新規に作成されたり、最後に実行してから変更のあったソースファイルだけを読み込んで、パースします。

.. option:: -t tag

   .. Define the tag *tag*.  This is relevant for :rst:dir:`only` directives that only
      include their content if this tag is set.

   *タグ* というタグを定義します。これは、タグが設定されているときにだけ内容を取り込むという、 :rst:dir:`only` ディレクティブと関係があります。

   .. versionadded:: 0.6

.. option:: -d path

   .. Since Sphinx has to read and parse all source files before it can write an
      output file, the parsed source files are cached as "doctree pickles".
      Normally, these files are put in a directory called :file:`.doctrees` under
      the build directory; with this option you can select a different cache
      directory (the doctrees can be shared between all builders).

   Sphinxは出力ファイルが書き込むことが可能になる前に、すべてのソースファイルを読み込むため、パースされたソースファイルは "doctree pickles"と呼ばれるディレクトリにキャッシュされます。通常は、これらのファイルはビルドディレクトリの下の :file:`.doctrees` と呼ばれるディレクトリに置かれます。このオプションを指定すると、キャッシュディレクトリを違う場所に設定できます。doctreeはすべてのビルダーで共有されます。

.. option:: -c path

   .. Don't look for the :file:`conf.py` in the source directory, but use the given
      configuration directory instead.  Note that various other files and paths
      given by configuration values are expected to be relative to the
      configuration directory, so they will have to be present at this location
      too.

   ソースディレクトリ以下の :file:`conf.py` ではなく、オプションで指定されたコンフィグレーションディレクトリ以下の設定ファイルを利用するようにします。ただし、さまざまな他のファイル、パスなど、設定値で与えられたものに関しては、コンフィグレーションディレクトリからの相対パスで探索されることになるため、その状況になってもファイルがきちんと読めるようにしておく必要があります。

   .. versionadded:: 0.3

.. option:: -C

   .. Don't look for a configuration file; only take options via the ``-D`` option.

   コンフィグファイルを無視します。設定は ``-D`` オプションを使って指定します。

   .. versionadded:: 0.5

.. option:: -D setting=value

   .. Override a configuration value set in the :file:`conf.py` file.  The value
      must be a string or dictionary value.  For the latter, supply the setting
      name and key like this: ``-D latex_elements.docclass=scrartcl``.  For boolean
      values, use ``0`` or ``1`` as the value.

   :file:`conf.py` に書かれた設定値を上書きで設定します。値は文字列か辞書の値である必要があります。後者の場合には設定名とキーは以下のように設定することができます: ``-D latex_elements.docclass=scartcl`` 。ブーリアン型の場合には、 ``0``, ``1`` を値に使用してください。

   .. .. versionchanged:: 0.6
         The value can now be a dictionary value.

   .. versionchanged:: 0.6
      値として辞書の値が使えるようになりました。

.. option:: -A name=value

   .. Make the *name* assigned to *value* in the HTML templates.

   HTMLテンプレートの中の *name* を *value* に設定します。

   .. versionadded:: 0.5

.. option:: -n

   .. Run in nit-picky mode.  Currently, this generates warnings for all missing
      references.

   エラーチェックが厳格なモードで実行されます。現在では、すべての見つからない参照に対して警告を生成するような実装になっています。

.. option:: -N

   .. Do not emit colored output.  (On Windows, colored output is disabled in any
      case.)

   出力に色づけをしないようにします。ただし、Windows上では元々どのような場合にも色を付ける機能は無効になっています。

.. option:: -q

   .. Do not output anything on standard output, only write warnings and errors to
      standard error.

   標準出力に何も出力しないようになります。警告やエラーのみが標準エラー出力に書き出されます。

.. option:: -Q

   .. Do not output anything on standard output, also suppress warnings.  Only
      errors are written to standard error.

   標準出力に何も出力しないようになります。警告も抑制されます。エラーのみが標準エラー出力に書き出されます。

.. option:: -w file

   .. Write warnings (and errors) to the given file, in addition to standard error.

   警告とエラーを指定されたファイルに書き出されます。なお、標準エラー出力にも同時に出力されます。

.. option:: -W

   .. Turn warnings into errors.  This means that the build stops at the first
      warning and ``sphinx-build`` exits with exit status 1.

   警告をエラーにします。最初の警告でビルドが中断され、 ``sphinx-build`` が終了値1を返すようになります。

.. option:: -P

   .. (Useful for debugging only.)  Run the Python debugger, :mod:`pdb`, if an
      unhandled exception occurs while building.

   (Sphinx自体のデバッグをする人用) キャッチされない例外がビルド中に発生したら、Pythonデバッガの :mod:`pdb` を実行します。

.. You can also give one or more filenames on the command line after the source and
   build directories.  Sphinx will then try to build only these output files (and
   their dependencies).

ソースディレクトリやビルドディレクトリの後ろにファイル名を1つ以上追加することができます。追加すると、指定されたファイルと、その依存ファイルだけをビルドしようとします。


.. Makefile options
   ----------------

Makefileオプション
------------------

.. The :file:`Makefile` and :file:`make.bat` files created by
   :program:`sphinx-quickstart` usually run :program:`sphinx-build` only with the
   :option:`-b` and :option:`-d` options.  However, they support the following
   variables to customize behavior:

:program:`sphinx-quickstart` を実行すると、 :file:`Makefile` と :file:`make.bat` が作成されますが、通常は :option:`-b` オプションと :option:`-d` オプションだけが設定されています。しかし、次のような変数を設定することで、動作をカスタマイズすることができます。

.. describe:: PAPER

   .. The value for :confval:`latex_paper_size`.

   :confval:`latex_paper_size` です。

.. describe:: SPHINXBUILD

   .. The command to use instead of ``sphinx-build``.

   ``sphinx-build`` の代わりに用いるコマンドです。

.. describe:: BUILDDIR

   .. The build directory to use instead of the one chosen in
      :program:`sphinx-quickstart`.

   :program:`sphinx-quickstart` で選択した以外のビルドディレクトリを使用します。

.. describe:: SPHINXOPTS

   .. Additional options for :program:`sphinx-build`.

   :program:`sphinx-build` に設定する追加オプションです。	

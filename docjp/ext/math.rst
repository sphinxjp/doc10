.. highlight:: rest

.. Math support in Sphinx
   ======================

Sphinxにおける数式のサポート
============================

.. module:: sphinx.ext.mathbase
   :synopsis: pngmath, jsmathを使用した数式のサポート

.. versionadded:: 0.5

.. :synopsis: Common math support for pngmath and jsmath.

.. Since mathematical notation isn't natively supported by HTML in any way, Sphinx
   supports math in documentation with two extensions.

HTMLでは、ネイティブでは数式の記法はサポートされていません。Sphinxでは、ドキュメントの中に数式を表現するための拡張機能を２つサポートしています。

.. The basic math support that is common to both extensions is contained in
   :mod:`sphinx.ext.mathbase`.  Other math support extensions should,
   if possible, reuse that support too.

両方の数式拡張のサポートに共通する部分は、 :mod:`sphinx.ext.mathbase` に含まれています。他に数式をサポートを行うための拡張機能を作成する場合には、使用できるのであれば、このモジュールを再利用してください。

.. note::

   :mod:`sphinx.ext.mathbase` は :confval:`extensions` の設定値に追加しないでください。追加するのは、これから説明を行う :mod:`sphinx.ext.pngmath` もしくは :mod:`sphinx.ext.jsmath` を設定してください。

.. .. note:

   :mod:`sphinx.ext.mathbase` is not meant to be added to the
   :confval:`extensions` config value, instead, use either
   :mod:`sphinx.ext.pngmath` or :mod:`sphinx.ext.jsmath` as described below.

.. The input language for mathematics is LaTeX markup.  This is the de-facto
   standard for plain-text math notation and has the added advantage that no
   further translation is necessary when building LaTeX output.

数式の入力言語としてはLaTeXのマークアップを利用します。これはプレーンテキストで数式を表現する記法としてはデファクトスタンダードになっています。また、LaTeX出力を行う場合には、変換をしないでそのまま利用できるというメリットもあります。

.. :mod:`mathbase` defines these new markup elements:

:mod:`mathbase` は以下の新しいマークアップの要素を定義しています:

.. rst:role:: math

   .. Role for inline math.  Use like this::

      Since Pythagoras, we know that :math:`a^2 + b^2 = c^2`.

   インラインの数式のロールです。以下のようにして使用します::

      ピタゴラスによって、 :math:`a^2 + b^2 = c^2` という式が成り立つことが示されました。

.. rst:directive:: math

   数式を表示するディレクティブです。この数式は１行丸ごと使って表示されます。

   このディレクティブは、複数行の等式をサポートしています。複数行に記述したい場合には、空行で区切ります::

      .. math::

         (a + b)^2 = a^2 + 2ab + b^2

         (a - b)^2 = a^2 - 2ab + b^2

   それぞれの数式は分割された環境にセットされます。もしも、複数行の等式をきれいに整列させたい場合には、 ``\\`` で区切って、 ``&`` 記号を使って整列させます::

      .. math::

         (a + b)^2  &=  (a + b)(a + b) \\
                    &=  a^2 + 2ab + b^2

   もっと詳しく知りたい場合には `AmSMath LaTeX パッケージ`_ のドキュメントを参照してください。

   数式が一行のテキストに収まる場合には、ディレクティブの引数として記述することもできます::

      .. math:: (a + b)^2 = a^2 + 2ab + b^2

   通常は数式には番号は付きません。もしも数式に対して番号をつけたくなった場合には、 ``label`` オプションを使用してください。これが指定されると、数式のラベルを選択できます。この数式のラベルを使ってクロスリファレンスを作成することができます。サンプルを見る場合には :rst:role:`eqref` を参照してください。ナンバリングの形式は出力フォーマットに依存します。

   .. There is also an option ``nowrap`` that prevents any wrapping of the given
      math in a math environment.  When you give this option, you must make sure
      yourself that the math is properly set up.  For example:

   ``nowrap`` オプションを使用することで、math環境で自動的にラッピングされるのを止めることができます。このオプションを指定した場合には、自分自身で適切な設定を行う必要があります。

   サンプル::

      .. math::
         :nowrap:

         \begin{eqnarray}
            y    & = & ax^2 + bx + c \\
            f(x) & = & x^2 + 2xy + y^2
         \end{eqnarray}

   .. Directive for displayed math (math that takes the whole line for itself).

      The directive supports multiple equations, which should be separated by a
      blank line:

      In addition, each single equation is set within a ``split`` environment,
      which means that you can have multiple aligned lines in an equation,
      aligned at ``&`` and separated by ``\\``:

         .. math::

            (a + b)^2  &=  (a + b)(a + b) \\
                       &=  a^2 + 2ab + b^2

      For more details, look into the documentation of the `AmSMath LaTeX
      package`_.

      When the math is only one line of text, it can also be given as a directive
      argument:

         .. math:: (a + b)^2 = a^2 + 2ab + b^2

      Normally, equations are not numbered.  If you want your equation to get a
      number, use the ``label`` option.  When given, it selects a label for the
      equation, by which it can be cross-referenced, and causes an equation number
      to be issued.  See :role:`eqref` for an example.  The numbering style depends
      on the output format.

      There is also an option ``nowrap`` that prevents any wrapping of the given
      math in a math environment.  When you give this option, you must make sure
      yourself that the math is properly set up.  For example::

         .. math::
            :nowrap:

            \begin{eqnarray}
               y    & = & ax^2 + bx + c \\
               f(x) & = & x^2 + 2xy + y^2
            \end{eqnarray}

.. rst:role:: eq

   数式のラベルに対する、クロスリファレンスを行うためのロールです。この機能は、現在では同じドキュメント内でのみ動作します。

   サンプル::

      .. math:: e^{i\pi} + 1 = 0
         :label: euler

         数式 :eq:`euler` にある、オイラーの恒等式は、最も美しい数学の法則に選出されました。

   .. Role for cross-referencing equations via their label.  This currently works
      only within the same document.  Example:

         .. math:: e^{i\pi} + 1 = 0
            :label: euler

         Euler's identity, equation :eq:`euler`, was elected one of the most
         beautiful mathematical formulas.


.. :mod:`sphinx.ext.pngmath` -- Render math as PNG images
   ------------------------------------------------------

:mod:`sphinx.ext.pngmath` -- 数式をPNG画像にレンダリングします
--------------------------------------------------------------

.. module:: sphinx.ext.pngmath
   :synopsis: 数式をPNG画像にレンダリング

.. :synopsis: Render math as PNG images.

.. This extension renders math via LaTeX and dvipng_ into PNG images.  This of
   course means that the computer where the docs are built must have both programs
   available.

この拡張は、LaTeXと、 dvipng_ を使用して、数式をPNG画像にレンダリングします。当然のことながら、この拡張を使ったドキュメントをビルドするマシンでは、この両方のプログラムが利用可能である必要があります。

.. There are various config values you can set to influence how the images are built:

この拡張用の設定値がいくつかあります。これらの設定値を変更することで、画像のビルドをカスタマイズしたりできます:

.. confval:: pngmath_latex

   LaTeXを呼び出す場合のコマンド名です。デフォルトでは ``'latex'`` となります。もしも ``latex`` コマンドが実行ファイルの検索パスにない場合には、フルパスを指定する必要があります。

   この設定はシステムの環境に依存するものなので、この設定はシステム間でポータブルではありません。そのため、この設定値は ``conf.py`` の中で設定するのは不便なので、 :program:`sphinx-build` の :option:`-D` オプションを使用して渡す方が望ましいでしょう。

   .. code-block:: bash

      sphinx-build -b html -D pngmath_latex=C:\tex\latex.exe . _build/html

   .. versionchanged:: 0.5.1
      この値にはLaTeXの実行ファイルのパスだけを含むようにして下さい。LaTeXに追加で渡したい引数は、こちらに入れないで、 :confval:`pngmath_latex_args` を使用してください。

.. The command name with which to invoke LaTeX.  The default is ``'latex'``; you
   may need to set this to a full path if ``latex`` is not in the executable
   search path.

   Since this setting is not portable from system to system, it is normally not
   useful to set it in ``conf.py``; rather, giving it on the
   :program:`sphinx-build` command line via the :option:`-D` option should be
   preferable, like this::

      sphinx-build -b html -D pngmath_latex=C:\tex\latex.exe . _build/html

   .. versionchanged:: 0.5.1
      This value should only contain the path to the latex executable, not
      further arguments; use :confval:`pngmath_latex_args` for that purpose.

.. confval:: pngmath_dvipng

   ``dvipng`` を呼び出す時のコマンド名です。デフォルト値は ``'dvipng'`` です。もしも ``dvipng`` が実行ファイルの検索パス外にある場合には、絶対パスを指定してください。

.. The command name with which to invoke ``dvipng``.  The default is
   ``'dvipng'``; you may need to set this to a full path if ``dvipng`` is not in
   the executable search path.

.. confval:: pngmath_latex_args

   LaTeXに渡す追加の引数です。リストで渡します。デフォルト値は空のリストになります。

   .. versionadded:: 0.5.1

.. Additional arguments to give to latex, as a list.  The default is an empty
   list.

.. confval:: pngmath_latex_preamble

   数式のコード片を変換するのに使用する、短いLaTeXファイルの中の前置きとして入れる、追加のLaTeXコードです。デフォルトでは空です。このオプションは、例えば、数式の中で使いたいコマンドのためのパッケージを追加したりするのに使用することができます。

.. Additional LaTeX code to put into the preamble of the short LaTeX files that
   are used to translate the math snippets.  This is empty by default.  Use it
   e.g. to add more packages whose commands you want to use in the math.

.. confval:: pngmath_dvipng_args

   dvipngに与える、追加の引数をリストで渡します。デフォルト値は ``['-gamma 1.5', '-D 110']`` で、画像をデフォルトよりも、多少暗く、サイズは少々大きくなります。

   追加したい引数をここで追加することができます。例えば、 ``'-bg Transparent'`` というオプションを渡すと、背景が透明なPNG画像を生成することができます。本来なら、このオプションはデフォルトで設定したいところですが、透明PNGをサポートしないバージョンのInternet Explorerもいくつか存在するために、デフォルトでは無効になっています。

   .. note::

      もしも引数を"追加"したい場合には、デフォルトの引数と同じ設定を残したい場合には、デフォルトの引数もコピーする必要があります::

         pngmath_dvipng_args = ['-gamma 1.5', '-D 110', '-bg Transparent']

.. Additional arguments to give to dvipng, as a list.  The default value is
   ``['-gamma 1.5', '-D 110']`` which makes the image a bit darker and larger
   then it is by default.

   An arguments you might want to add here is e.g. ``'-bg Transparent'``,
   which produces PNGs with a transparent background.  This is not enabled by
   default because some Internet Explorer versions don't like transparent PNGs.

   .. note:

      When you "add" an argument, you need to reproduce the default arguments if
      you want to keep them; that is, like this::

         pngmath_dvipng_args = ['-gamma 1.5', '-D 110', '-bg Transparent']

.. confval:: pngmath_use_preview

   .. ``dvipng`` has the ability to determine the "depth" of the rendered text: for
      example, when typesetting a fraction inline, the baseline of surrounding text
      should not be flush with the bottom of the image, rather the image should
      extend a bit below the baseline.  This is what TeX calls "depth".  When this
      is enabled, the images put into the HTML document will get a
      ``vertical-align`` style that correctly aligns the baselines.

   ``dvipng`` は、レンダリングされたテキストの"深さ"を決定することができます。例えば、行の文章の中に分数を写植する場合、テキストのベースラインと、生成された画像の底辺の高さが同じであってはならず、画像はベースラインよりも少し低い位置になるべでしょう。これがTeXの世界でいう"深さ"です。もしもこのオプションが有効になっていると、ベースラインからの正しいオフセット量の ``垂直揃え`` のスタイルで画像が生成され、HTMLドキュメントに入れられます。

   .. Unfortunately, this only works when the `preview-latex package`_ is
      installed.  Therefore, the default for this option is ``False``.

   残念ながら、このオプションは、 `preview-latex package`_ がインストールされていなければ動作しません。そのため、デフォルトの値は ``False`` になっています。


.. :mod:`sphinx.ext.jsmath` -- Render math via JavaScript
   ------------------------------------------------------

:mod:`sphinx.ext.jsmath` -- JavaScriptを使用して数式をレンダリングします
------------------------------------------------------------------------


.. module:: sphinx.ext.jsmath
   :synopsis: JavaScriptを使った数式のレンダリング

.. :synopsis: Render math via JavaScript.

.. This extension puts math as-is into the HTML files.  
   The JavaScript package jsMath_ is then loaded and transforms 
   the LaTeX markup to readable math live in the browser.

この拡張機能は、数式をそのままHTMLファイルに埋め込みます。JavaScriptのパッケージの jsMath_ がロードされ、LaTeXのマークアップが、ブラウザ上で動的に読める数式に変換します。

.. Because jsMath (and the necessary fonts) is very large, it is not 
   included in Sphinx.  You must install it yourself, and give Sphinx its 
   path in this config value:

jsMath(と必要なフォント)はかなり巨大です。そのため、Sphinxには含まれていません。自分でインストールを行い、設定値を使って、その置き場のパスをSphinxに知らせなければなりません:

.. confval:: jsmath_path

   .. The path to the JavaScript file to include in the HTML files in order to load
      JSMath.  There is no default.

   JavaScriptファイルをHTMLファイルに取り込み、JSMathをロードするために必要なオプションです。パスを設定します。デフォルト値はありません。

   .. The path can be absolute or relative; if it is relative, it is relative to
      the ``_static`` directory of the built docs.

   パスは絶対パスでも、相対パスでもどちらでも大丈夫です。相対パスの場合には、ビルド済みのドキュメントの ``_static`` ディレクトリからのが相対パスになります。

   .. For example, if you put JSMath into the static path of the Sphinx docs, this
      value would be ``jsMath/easy/load.js``.  If you host more than one
      Sphinx documentation set on one server, it is advisable to install jsMath in
      a shared location.

   もしもjsMathを、Sphinxのドキュメント内の静的ファイルのフォルダに置いたとしたら、この設定値は ``jsMath/easy/load.js`` になります。もしもSphinxのドキュメントをサーバ上に何セットも設置する場合には、共有の場所にjsMathをインストールするのが賢明でしょう。


.. _dvipng: http://savannah.nongnu.org/projects/dvipng/
.. _jsMath: http://www.math.union.edu/~dpvc/jsmath/
.. _preview-latex package: http://www.gnu.org/software/auctex/preview-latex.html
.. _AmSMath LaTeX パッケージ: http://www.ams.org/tex/amslatex.html
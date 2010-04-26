.. highlight:: rest

.. :mod:`sphinx.ext.autosummary` -- Generate autodoc summaries
   ===========================================================

:mod:`sphinx.ext.autosummary` -- autodocのサマリーの生成
========================================================

.. 
   .. module:: sphinx.ext.autosummary
      .. :synopsis: Generate autodoc summaries

.. module:: sphinx.ext.autosummary
   :synopsis: autodocのサマリーの生成

.. versionadded:: 0.6

.. This extension generates function/method/attribute summary lists, similar to
   those output e.g. by Epydoc and other API doc generation tools.  This is
   especially useful when your docstrings are long and detailed, and putting each
   one of them on a separate page makes them easier to read.

この拡張機能は、Epydocや他のAPIドキュメント生成ツールような、関数、メソッド、属性のサマリーのリストを生成します。この機能は、作成中のシステムのdocstringが長く、詳細まで記述されていて、読みやすくするためにページを分けて出力されている場合に便利です。

.. The :mod:`sphinx.ext.autosummary` extension does this in two parts:

:mod:`sphinx.ext.autosummary` は以下の２つの機能を持っています:

.. 1. There is an :rst:dir:`autosummary` directive for generating summary listings that
      contain links to the documented items, and short summary blurbs extracted
      from their docstrings.

   2. The convenience script :program:`sphinx-autogen` or the new
      :confval:`autosummary_generate` config value can be used to generate short
      "stub" files for the entries listed in the :rst:dir:`autosummary` directives.
      These by default contain only the corresponding :mod:`sphinx.ext.autodoc`
      directive.

1. ドキュメントが書かれた要素へのリンクと、docstringから抽出した短い概要の文を含んだサマリーのリストを生成する、 :dir:`autosummary` ディレクティブがあります。 

2. 便利なスクリプト :program:`sphinx-autogen` あるいは、新しい設定値の :confval:`autosummary_generate` を使用して、短い"スタブ"ファイルを生成することができます。このファイルは :dir:`autosummary` ディレクティブ内に書かれているエントリーが記述されます。デフォルトでは、関連する :mod:`sphinx.ext.autodoc` ディレクティブだけが含まれます。


.. directive:: autosummary

   .. Insert a table that contains links to documented items, and a short summary
      blurb (the first sentence of the docstring) for each of them.  The
      :rst:dir:`autosummary` directive can also optionally serve as a :rst:dir:`toctree`
      entry for the included items.

   ドキュメントされている項目へのリンクを含むテーブルを挿入します。この中には、それぞれに対するサマリー文(docstringの最初の文)も含まれます。 :rst:dir:`autosummary` ディレクティブはおまけとして、含まれている項目への :rst:dir:`toctree` のような働きもします。

   .. For example, :

   サンプル::

       .. currentmodule:: sphinx

       .. autosummary::

          environment.BuildEnvironment
          util.relative_uri

   .. produces a table like this:

   これは以下のようなテーブルを作成します::

       .. currentmodule:: sphinx

       .. autosummary::

          environment.BuildEnvironment
          util.relative_uri

       .. currentmodule:: sphinx.ext.autosummary

   .. Autosummary preprocesses the docstrings and signatures with the same
      :event:`autodoc-process-docstring` and :event:`autodoc-process-signature`
      hooks as :mod:`~sphinx.ext.autodoc`.

   autosummaryは、 :mod:`~sphinx.ext.autodoc` が行っているのと同様に、 :event:`autodoc-process-docstring` イベントと、 :event:`autodoc-process-signature` イベントをフックすることで、 docstringとシグニチャの前処理を行います。

   .. **Options**

   **オプション**

   .. * If you want the :rst:dir:`autosummary` table to also serve as a :rst:dir:`toctree`
       entry, use the ``toctree`` option, for example:

           .. autosummary::
              :toctree: DIRNAME

              sphinx.environment.BuildEnvironment
              sphinx.util.relative_uri

       The ``toctree`` option also signals to the :program:`sphinx-autogen` script
       that stub pages should be generated for the entries listed in this
       directive.  The option accepts a directory name as an argument;
       :program:`sphinx-autogen` will by default place its output in this
       directory. If no argument is given, output is placed in the same directory
       as the file that contains the directive.

   * :rst:dir:`autosummary` テーブルを :rst:dir:`toctree` のエントリーと同様に提供したい場合には、以下のようにします::

        .. autosummary::
           :toctree: ディレクトリ名

           sphinx.environment.BuildEnvironment
           sphinx.util.relative_uri

     ``toctree`` オプションは、このディレクティブに含まれるエントリーのリストに対するスタブのページを作成する、 :program:`sphinx-autogen` スクリプトにも伝えられます。このオプションは、ディレクトリ名を引数として受け取ります。デフォルトでは :program:`sphinx-autogen` はこのディレクトリに出力します。もしも引数が与えられなかった場合には、そのディレクティブが含まれているファイルがある、同じディレクトリに出力します。

   .. * If you don't want the :rst:dir:`autosummary` to show function signatures in the
        listing, include the ``nosignatures`` option:

   * 関数のシグネチャを、:rst:dir:`autosummary` が出力するリストの中に入れたくない場合には、 ``nosignatures`` オプションを設定します::

         .. autosummary::
            :nosignatures:

            sphinx.environment.BuildEnvironment
            sphinx.util.relative_uri

   .. * You can specify a custom template with the ``template`` option.
        For example, :

   * ``template`` オプションを使用することで、カスタムのテンプレートを指定することができます

     サンプル::

         .. autosummary::
            :template: mytemplate.rst

            sphinx.environment.BuildEnvironment

     このサンプルのコードをビルドすると、 :confval:`templates_path` に含まれる、 :file:`mytemplate.rst` という名前のテンプレートファイルを使用して、エントリーのすべてのリストのページを生成します。詳しくは `テンプレートのカスタマイズ`_ を参照してください。

     .. versionadded:: 1.0

   ..  would use the template :file:`mytemplate.rst` in your
       :confval:`templates_path` to generate the pages for all entries
       listed. See `Customizing templates`_ below.

       .. versionadded:: 1.0

.. :program:`sphinx-autogen` -- generate autodoc stub pages
   --------------------------------------------------------

:program:`sphinx-autogen` -- autodocのスタブページを生成
--------------------------------------------------------

.. The :program:`sphinx-autogen` script can be used to conveniently generate stub
   documentation pages for items included in :rst:dir:`autosummary` listings.

:program:`sphinx-autogen` スクリプトは :rst:dir:`autosummary` にリストアップされた要素のためのドキュメントページのスタブを簡単に生成するのに使用されます。

.. For example, the command :

以下のようにコマンドを起動したとします::

    $ sphinx-autogen -o generated *.rst

.. will read all :rst:dir:`autosummary` tables in the :file:`*.rst` files that have the
   ``:toctree:`` option set, and output corresponding stub pages in directory
   ``generated`` for all documented items.  The generated pages by default contain
   text of the form:

このコマンドを実行すると、 :file:`*.rst` にマッチして、なおかつ ``:toctree:`` オプションを持つすべてのファイルを読み込み、その中に定義されているすべての :rst:dir:`autosummary` テーブルを読み込みます。読み込んだ後はすべてのドキュメント付けされた要素に関連するスタブページを ``generated`` ディレクトリに出力します。デフォルトでは、以下のようなテキストを含むページが生成されます::

    sphinx.util.relative_uri
    ========================

    .. autofunction:: sphinx.util.relative_uri

.. If the ``-o`` option is not given, the script will place the output files in the
   directories specified in the ``:toctree:`` options.

もしも ``-o`` オプションが指定されなかった場合には、 ``:toctree:`` オプションで設定されたディレクトリにファイルを出力します。


.. Generating stub pages automatically
   -----------------------------------

スタブページの自動作成
----------------------

.. If you do not want to create stub pages with :program:`sphinx-autogen`, you can
   also use this new config value:

   もしも、 :program:`sphinx-autogen` を使用してスタブページを作成したくない場合は、以下の設定値を使用することもできます:

.. confval:: autosummary_generate

   .. Boolean indicating whether to scan all found documents for autosummary
      directives, and to generate stub pages for each.

   ブーリアン値で、autosummaryディレクティブのために書かれたドキュメントをすべてスキャン   して、それぞれのスタブページを作成するかどうか決定します。

   .. Can also be a list of documents for which stub pages should be generated.

   スタブページを作成すべきドキュメントをリスト表示するのにも使用することができます。

   .. The new files will be placed in the directories specified in the
      ``:toctree:`` options of the directives.

   ディレクティブの ``:toctree:`` オプションで指定されたディレクトリに新しいファイルを配置します。

.. Customizing templates
   ---------------------

テンプレートのカスタマイズ
--------------------------

.. versionadded:: 1.0

.. You can customize the stub page templates, in a similar way as the HTML Jinja
   templates, see :ref:`templating`. (:class:`~sphinx.application.TemplateBridge`
   is not supported.)

:ref:`templating` のセクションで説明しているのと同じ、Sphinxの標準的なHTMLのJinjaテンプレートを使って、スタブページのテンプレートをカスタマイズすることができます。ただし、 :class:`~sphinx.application.TemplateBridge` はサポートしていません。

.. note::

   もしも、スタブのテンプレートをカスタマイズするのに長い時間をかけているということが分かった場合には、autosummaryによる自動生成をやめて、自分でスタブを書いていく方がいいかもしれません。

.. If you find yourself spending much time tailoring the stub templates, this
   may indicate that it's a better idea to write custom narrative documentation
   instead.

.. Autosummary uses the following template files:

autosummaryは以下のテンプレートファイルを使用します:

.. - :file:`autosummary/base.rst` -- fallback template
   - :file:`autosummary/module.rst` -- template for modules
   - :file:`autosummary/class.rst` -- template for classes
   - :file:`autosummary/function.rst` -- template for functions
   - :file:`autosummary/attribute.rst` -- template for class attributes
   - :file:`autosummary/method.rst` -- template for class methods

- :file:`autosummary/base.rst` -- 代替のテンプレート
- :file:`autosummary/module.rst` -- モジュールのためのテンプレート
- :file:`autosummary/class.rst` -- クラスのためのテンプレート
- :file:`autosummary/function.rst` -- 関数のためのテンプレート
- :file:`autosummary/attribute.rst` -- クラス属性のためのテンプレート
- :file:`autosummary/method.rst` -- クラスメソッドのためのテンプレート

.. The following variables available in the templates:

テンプレートの中では以下の変数名が利用可能です:

.. currentmodule:: None

.. data:: name

   ドキュメントの対象となっているオブジェクトの名前です。モジュールなやクラス名の部分は含まれません。

   .. Name of the documented object, excluding the module and class parts.

.. data:: objname

   ドキュメント対象となっているオブジェクトの名前です。モジュール名の部分は含まれません。

   .. Name of the documented object, excluding the module parts.

.. data:: fullname

   ドキュメント対象となっているオブジェクトの名前です。モジュール名、クラス名も含みます。

   .. Full name of the documented object, including module and class parts.

.. data:: module

   ドキュメント対象のオブジェクトが属しているモジュールの名前です。

   .. Name of the module the documented object belongs to.

.. data:: class

   ドキュメント対象のオブジェクトが属すクラスの名前です。メソッドと属性が対象の場合だけ利用できます。

   .. Name of the class the documented object belongs to.  Only available for
      methods and attributes.

.. data:: underline

   ``len(full_name) * '='`` の実行結果です。

   .. A string containing ``len(full_name) * '='``.

.. data:: members

   モジュールやクラスに属す、すべてのメンバーの名前のリストです。モジュールとクラスが対象の場合のみ利用できます。

   .. List containing names of all members of the module or class.  Only available
      for modules and classes.

.. data:: functions

   .. List containing names of "public" functions in the module.  Here, "public"
      here means that the name does not start with an underscore. Only available
      for modules.

   モジュールの"公開"関数の名前を含むリストです。ここでの"公開"は、名前の最初の文字がアンダースコア以外のものを意味しています。対象がモジュールの場合のみ利用できます。

.. data:: classes

   モジュールの"公開"クラスの名前を含むリストです。対象がモジュールの場合のみ利用できます。

   .. List containing names of "public" classes in the module.  Only available for
      modules.

.. data:: exceptions

   モジュールの"公開"例外クラスの名前を含むリストです。対象がモジュールの場合のみ利用できます。

   .. List containing names of "public" exceptions in the module.  Only available
      for modules.

.. data:: methods

   クラスの"公開"メソッドの名前を含むリストです。対象がクラスの場合のみ利用できます。

   .. List containing names of "public" methods in the class.  Only available for
      classes.

.. data:: attributes

   クラスの"公開"属性の名前を含むリストです。対象がクラスの場合のみ利用できます。

   .. List containing names of "public" attributes in the class.  Only available
      for classes.

.. note::
   
   :rst:dir:`autosummay` ディレクティブは、スタブページの中でも使用することができます。スタブページは、これらのディレクティブを元に生成されます。

   .. You can use the :rst:dir:`autosummary` directive in the stub pages.
      Stub pages are generated also based on these directives.

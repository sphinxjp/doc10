.. highlight:: rest

.. Module-specific markup
.. ----------------------

モジュール用のマークアップ
--------------------------

.. The markup described in this section is used to provide information about a module being documented.  Normally this markup appears after a title heading; a typical module section might start like this

このセクションで説明するマークアップはドキュメントの書かれているモジュールに対して情報を提供するものです。


..   :mod:`parrot` -- Dead parrot access
     ===================================

..   .. module:: parrot
        :platform: Unix, Windows
        :synopsis: Analyze and reanimate dead parrots.
     .. moduleauthor:: Eric Cleese <eric@python.invalid>
     .. moduleauthor:: John Idle <john@python.invalid>

   :mod:`parrot` -- 死んだオウムへアクセス
   ======================================

   .. module:: parrot
      :platform: Unix, Windows
      :synopsis: 死んだオウムの解析と蘇生
   .. moduleauthor:: Eric Cleese <eric@python.invalid>
   .. moduleauthor:: John Idle <john@python.invalid>

.. The directives you can use for module declarations are:

それでは、モジュールのドキュメンテーションに利用できるディレクティブの説明をします:

.. .. directive:: .. module:: name

..   This directive marks the beginning of the description of a module (or package submodule, in which case the name should be fully qualified, including the package name).  It does not create content (like e.g. :dir:`class` does).

..   This directive will also cause an entry in the global module index.

..   The ``platform`` option, if present, is a comma-separated list of the platforms on which the module is available (if it is available on all platforms, the option should be omitted).  The keys are short identifiers; examples that are in use include "IRIX", "Mac", "Windows", and "Unix".  It is important to use a key which has already been used when applicable.

..   The ``synopsis`` option should consist of one sentence describing the module's purpose -- it is currently only used in the Global Module Index.

..   The ``deprecated`` option can be given (with no value) to mark a module as deprecated; it will be designated as such in various locations then.

.. directive:: .. module:: 名前

   このディレクティブはモジュールの説明の開始時に使用します。パッケージやサブモジュールにも使用できますが、この場合はパッケージ名を含む、完全な名前を指定してください。この ディレクティブは :dir:`class` ディレクティブのようなコンテンツを作成することはできません。

   このディレクティブを使用すると、グローバルモジュールインデックスに項目が追加されます。

   ``platform`` オプションが存在していれば、そのモジュールが利用可能なモジュールをカンマ区切りで指定します。もしすべてのプラットフォームで利用可能であれば、このオプションは使用しないようにしましょう。プラットフォーム名としては、短い識別子、例えば、"IRIX", "Mac", "Windows", "Unix"などから利用してください。もし適用時点ですでに使用されているキーがあれば、それを使用してください。

   ``synopsis`` オプションには、モジュールの目的を説明する文章を書くことができます。現在のバージョンでは、これはグローバルモジュールインデックスの中でのみ使用されます。

   ``deprecated`` オプションを使用すると、このモジュールが古くて、使用するのを推奨しない、ということを示すことができます。オプションは取りません。このディレクティブは様々な場所で使用されるでしょう。

.. .. directive:: .. currentmodule:: name

   This directive tells Sphinx that the classes, functions etc. documented from
   here are in the given module (like :dir:`module`), but it will not create
   index entries, an entry in the Global Module Index, or a link target for
   :role:`mod`.  This is helpful in situations where documentation for things in
   a module is spread over multiple files or sections -- one location has the
   :dir:`module` directive, the others only :dir:`currentmodule`.

.. directive:: .. currentmodule:: 名前

   このディレクティブはSphinxに対して、この行以降のクラスや関数などが、指定された与えられたモジュール ( :dir:`module` のように)の中にある、ということを通知します。これを使用しても、インデックスのエントリーは作成されません。 :role:`mod` へのリンクターゲットも作成されません。このディレクティブは、モジュールに含まれる項目へのドキュメントが様々なファイルやセクションに分割されている場合に便利です。この場合には一カ所だけ :dir:`module` ディレクティブを使用して、他の箇所で :dir:`currentmodule` を使用するようにします。

.. .. directive:: .. moduleauthor:: name <email>

   The ``moduleauthor`` directive, which can appear multiple times, names the
   authors of the module code, just like ``sectionauthor`` names the author(s)
   of a piece of documentation.  It too only produces output if the
   :confval:`show_authors` configuration value is True.

.. directive:: .. moduleauthor:: 名前 <Eメール>

   ``moduleauthor`` ディレクティブは何度も書くことができます。 ``sectionauthor`` でドキュメントの一部に対して著者の名前を何人も指定できるように、モジュールコードの著者の名前を指定できます。これも :confval:`show_authors` 設定値をTrueにすると出力されます。

.. note::

   .. It is important to make the section title of a module-describing file
      meaningful since that value will be inserted in the table-of-contents trees
      in overview files.

   これは概要ファイルの目次のツリーに挿入されるようになります。モジュール説明ファイルのセクションタイトルの情報が増えるため、重要です。

.. _Desc-units:


.. Object description units
.. ------------------------

オブジェクト説明のためのディレクティブ
--------------------------------------

.. There are a number of directives used to describe specific features provided by
   modules.  Each directive requires one or more signatures to provide basic
   information about what is being described, and the content should be the
   description.  The basic version makes entries in the general index; if no index
   entry is desired, you can give the directive option flag ``:noindex:``.  The
   following example shows all of the features of this directive type::

モジュールに含まれる機能を説明するのに使用するディレクティブもいくつもあります。それぞれのディレクティブは、説明対象に関する基本情報を記述するためのシグニチャが１つ以上あります。基本バージョンは全体インデックスにエントリーを追加します。インデックスのエントリーに追加する必要がなければ ``:noindex:`` フラグをディレクティブのオプションすれば回避することができます。以下の例はこのディレクティブのすべての機能を表すサンプルです::

    .. function:: spam(eggs)
                  ham(eggs)
       :noindex:

       説明..

..       Spam or ham the foo.

.. The signatures of object methods or data attributes should always include the
   type name (``.. method:: FileInput.input(...)``), even if it is obvious from the
   context which type they belong to; this is to enable consistent
   cross-references.  If you describe methods belonging to an abstract protocol,
   such as "context managers", include a (pseudo-)type name too to make the
   index entries more informative.

   オブジェクトのメソッドのシグニチャ, データ属性には型名 (``.. method:: FileInput.input(...)``) を含める必要があります。それがそれらが属する場所の情報から明確であっても入れなければなりません。これはクロスリファレンスを間違いなく生成するために必要になります。"コンテキストマネージャ"のような抽象的なプロトコルを持つメソッドを説明する場合には、(仮の)型名を含めて、インデックスエントリーの情報を増やすようにするします。

.. The directives are:

ディレクティブには以下のものがあります。

.. .. directive:: .. cfunction:: type name(signature)

   Describes a C function. The signature should be given as in C, e.g.::

      .. cfunction:: PyObject* PyType_GenericAlloc(PyTypeObject *type, Py_ssize_t nitems)

   This is also used to describe function-like preprocessor macros.  The names
   of the arguments should be given so they may be used in the description.

   Note that you don't have to backslash-escape asterisks in the signature,
   as it is not parsed by the reST inliner.


.. directive:: .. cfunction:: 型 名前(シグニチャ)

   Cの関数の説明に使用します。シグニチャはC言語内で書かれる様に記述します。例えば以下のように書きます::

      .. cfunction:: PyObject* PyType_GenericAlloc(PyTypeObject *type, Py_ssize_t nitems)

   これは、関数のようなプリプロセッサマクロにも使用することができます。引き数名も書く必要があります。説明の中で使用されることもあります。

   シグネチャ内のアスタリスクはバックスラッシュでエスケープする必要はありません。この中はreSTの行内のテキスト処理のパーサは実行されず、専用のパーサで処理されます。

.. .. directive:: .. cmember:: type name

   Describes a C struct member. Example signature::

      .. cmember:: PyObject* PyTypeObject.tp_bases

   The text of the description should include the range of values allowed, how
   the value should be interpreted, and whether the value can be changed.
   References to structure members in text should use the ``member`` role.

.. directive:: .. cmember:: 型 名前

   Cの構造体メンバーの説明をします。以下のように記述します::

      .. cmember:: PyObject* PyTypeObject.tp_bases

   説明のテキストには受け入れ可能な値の範囲、値がどのように解釈されるべきか、値が変更可能かどうかという情報を入れるべきです。関数のメンバーへの参照をテキストの中で書きたい場合には、 ``member`` ロールを使用すべきです。

.. .. directive:: .. cmacro:: name

   Describes a "simple" C macro.  Simple macros are macros which are used
   for code expansion, but which do not take arguments so cannot be described as
   functions.  This is not to be used for simple constant definitions.  Examples
   of its use in the Python documentation include :cmacro:`PyObject_HEAD` and
   :cmacro:`Py_BEGIN_ALLOW_THREADS`.

.. directive:: .. cmacro:: 名前

   "シンプルな"C言語のマクロの説明をします。シンプルなマクロというのは、単純なコード展開だけをするもので、引数を取ることはできません。また、単純な定数定義にも使用してはいけません。このディレクティブのサンプルを見るには、Pythonドキュメントの :cmacro:`PyObject_HEAD`, :cmacro:`Py_BEGIN_ALLOW_THREADS` を参照してください。

.. .. directive:: .. ctype:: name

   Describes a C type. The signature should just be the type name.

.. directive:: .. ctype:: 名前

   C言語の型を説明します。シグニチャには型名を指定します。

.. .. directive:: .. cvar:: type name

   Describes a global C variable.  The signature should include the type, such
   as::

      .. cvar:: PyObject* PyClass_Type

.. directive:: .. cvar:: 型 名前

   グローバルなC言語の変数について説明します。シグニチャは型を含む必要があります。以下のように記述します。

      .. cvar:: PyObject* PyClass_Type

.. .. directive:: .. data:: name

   Describes global data in a module, including both variables and values used
   as "defined constants."  Class and object attributes are not documented
   using this environment.

.. directive:: .. data:: 名前

   モジュール内のグローバルなデータの説明をします。変数も値も"定義された定数"として取り込むことができます。クラスとオブジェクトの属性はこの環境を使用してドキュメントを書くことはできません。

.. .. directive:: .. exception:: name

   Describes an exception class.  The signature can, but need not include
   parentheses with constructor arguments.

.. directive:: .. exception:: 名前

   例外クラスの説明をします。シグニチャには、コンストラクタの引数を括弧付きで含めることもできますが、しなくてもかまいません。

.. .. directive:: .. function:: name(signature)

   Describes a module-level function.  The signature should include the
   parameters, enclosing optional parameters in brackets.  Default values can be
   given if it enhances clarity; see :ref:`signatures`.  For example::

      .. function:: Timer.repeat([repeat=3[, number=1000000]])

   Object methods are not documented using this directive. Bound object methods
   placed in the module namespace as part of the public interface of the module
   are documented using this, as they are equivalent to normal functions for
   most purposes.

   The description should include information about the parameters required and
   how they are used (especially whether mutable objects passed as parameters
   are modified), side effects, and possible exceptions.  A small example may be
   provided.

.. directive:: .. function:: 名前(シグニチャ)

   モジュールレベル関数の説明です。シグニチャはパラメータを含めます。オプションのパラメータに対してはカッコでくくります。分かりやすさを上げる目的でデフォルト値を入れることもできます。 :ref:`signatures` の説明も参照してください。例::

      .. function:: Timer.repeat([repeat=3[, number=1000000]])

   オブジェクトのメソッドはこのディレクティブではドキュメントを記述することはできません。モジュールの名前空間にあり、モジュールの公開インタフェースとして作成されているメソッドに限って使用することができます。これらは通常の関数とほぼ同じようにしようできます。

   説明にはパラメータに必要な関する情報と、それらがどのように使用されるのか(変更可能なオブジェクトが渡されたときに、変更されるのかどうか)、副作用、投げられる可能性のある例外の情報を含まなければなりません。小さいサンプルが提供されるでしょう。

.. .. directive:: .. class:: name[(signature)]

   Describes a class.  The signature can include parentheses with parameters
   which will be shown as the constructor arguments.  See also
   :ref:`signatures`.

   Methods and attributes belonging to the class should be placed in this
   directive's body.  If they are placed outside, the supplied name should
   contain the class name so that cross-references still work.  Example::

      .. class:: Foo
         .. method:: quux()

      -- or --

      .. class:: Bar

      .. method:: Bar.quux()

   The first way is the preferred one.

   .. versionadded:: 0.4
      The standard reST directive ``class`` is now provided by Sphinx under
      the name ``cssclass``.

.. directive:: .. class:: クラス名[(シグニチャ)]

   クラスについて説明します。シグニチャにはコンストラクタ引数になるパラメータも含めることができます。 :ref:`signatures` も参照してください。

   このクラスに属する属性とメソッドのディレクティブはこのディレクティブの本体の中に記述します。このクラスの外に書いた場合は、提供された名前にクラス名が含まれていれば、クロスリファレンスは動作します。サンプル::

      .. class:: Foo
         .. method:: quux()

      -- あるいは --

      .. class:: Bar

      .. method:: Bar.quux()

   最初の書き方が推奨です。

   .. versionadded:: 0.4
      標準のreSTのディレクティブの ``class`` は、現在のSphinxでは ``cssclass`` という名前で提供されています。

.. .. directive:: .. attribute:: name

   Describes an object data attribute.  The description should include
   information about the type of the data to be expected and whether it may be
   changed directly.

.. directive:: .. attribute:: 名前 

   オブジェクトの属性のデータの説明をします。この説明には期待されるデータの型、値を直接変更することができるかどうか、という情報を含めます。

.. .. directive:: .. method:: name(signature)

   Describes an object method.  The parameters should not include the ``self``
   parameter.  The description should include similar information to that
   described for ``function``.  See also :ref:`signatures`.

.. directive:: .. method:: 名前(シグニチャ)

   オブジェクトのメソッドの説明をします。パラメータからは ``self`` パラメータははずします。この説明には ``function`` と同じ情報を記述するようにします。 :ref:`signatures` も参照してください。

.. .. directive:: .. staticmethod:: name(Like)

   :dir:`method`, but indicates that the method is a static method.

   .. versionadded:: 0.4

.. directive:: .. staticmethod:: 名前(シグニチャ)

   :dir:`method` とほぼ一緒ですが、メソッドがスタティックメソッドであるということを表明します。

   .. versionadded:: 0.4

.. .. directive:: .. classmethod:: name(signature)

   Like :dir:`method`, but indicates that the method is a class method.

   .. versionadded:: 0.6

.. directive:: .. classmethod:: 名前(シグニチャ)

   :dir:`method` とほぼ一緒ですが、メソッドがクラスメソッドであるということを表明します。

   .. versionadded:: 0.6


.. Signatures
.. ~~~~~~~~~~

.. _signatures:

シグニチャ
~~~~~~~~~~

.. Signatures of functions, methods and class constructors can be given like they
   would be written in Python, with the exception that optional parameters can be
   indicated by brackets::

   .. function:: compile(source[, filename[, symbol]])

関数やメソッド、クラスのコンストラクタのシグニチャは、オプションパラメータにカッコを使うのを除いて、Pythonで書くように記述することができます::

   .. function:: compile(source[, filename[, symbol]])

.. It is customary to put the opening bracket before the comma.  In addition to
   this "nested" bracket style, a "flat" style can also be used, due to the fact
   that most optional parameters can be given independently::

このような省略可能な引数を表す場合には、慣習的にカンマの前に開きカッコを置きます。省略できる引数が二つ以上ある場合には、カッコを入れ子にするスタイルと、フラットにするスタイルの両方があります。このような場合にはほとんどの場合、オプションの引数は個別に与えることができます。

   .. function:: compile(source[, filename, symbol])

.. Default values for optional arguments can be given (but if they contain commas,
   they will confuse the signature parser).  Python 3-style argument annotations
   can also be given as well as return type annotations::

オプション引数のデフォルト値を与えることもできます。ただし、値にカンマが含まれると、シグニチャのパーサはうまく動作しません。Pythonの３つのスタイルの引数のアノテーションと同様に、返り値の型も記述することができます。

   .. function:: compile(source : string[, filename, symbol]) -> ast object


.. Info field lists
.. ~~~~~~~~~~~~~~~~

詳細情報フィールドのリスト
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 0.4

.. Inside description unit directives, reST field lists with these fields are
   recognized and formatted nicely:

オブジェクト説明のためのディレクティブの内側には、適切に情報が明示されたreSTフィールドを配置することができます。

.. * ``param``, ``parameter``, ``arg``, ``argument``, ``key``, ``keyword``:
     Description of a parameter.
   * ``type``: Type of a parameter.
   * ``raises``, ``raise``, ``except``, ``exception``: That (and when) a specific
     exception is raised.
   * ``var``, ``ivar``, ``cvar``: Description of a variable.
   * ``returns``, ``return``: Description of the return value.
   * ``rtype``: Return type.

* ``param``, ``parameter``, ``arg``, ``argument``, ``key``, ``keyword``: 引数の説明です。
* ``type``: 引数のタイプです
* ``raises``, ``raise``, ``except``, ``exception``: この中から投げられる例外(いつ投げられるか？も)を定義します
* ``var``, ``ivar``, ``cvar``: 変数の説明をします
* ``returns``, ``return``: 返り値の値について説明をします
* ``rtype``: 返り値の型です。

.. The field names must consist of one of these keywords and an argument (except
   for ``returns`` and ``rtype``, which do not need an argument).  This is best
   explained by an example::

フィールドは、 ``return``, ``rtype`` 以外の場合は、上記のキーワードのうち、どれかと、引数を一つが引数として設定されています。 ``return``, ``rtype`` だけは引数を取りません。サンプルを見ていただくのが一番でしょう::

   .. function:: format_exception(etype, value, tb[, limit=None])

      トレースバック付きで、例外を人の読める形式にフォーマットします。

      :param etype: 例外のタイプ
      :param value: 例外オブジェクト
      :param tb: トレースバックオブジェクト
      :param limit: 表示するスタックフレームの数の最大数
      :type limit: 数値 or None
      :rtype: 文字列のリスト

..   .. function:: format_exception(etype, value, tb[, limit=None])

      Format the exception with a traceback.

      :param etype: exception type
      :param value: exception value
      :param tb: traceback object
      :param limit: maximum number of stack frames to show
      :type limit: integer or None
      :rtype: list of strings

.. This will render like this:

これは以下のようにレンダリングされます:

   .. function:: format_exception(etype, value, tb[, limit=None])
      :noindex:

      トレースバック付きで、例外を人の読める形式にフォーマットします。

      :param etype: 例外のタイプ
      :param value: 例外オブジェクト
      :param tb: トレースバックオブジェクト
      :param limit: 表示するスタックフレームの数の最大数
      :type limit: 数値 or None
      :rtype: 文字列のリスト


.. Command-line program markup
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンドラインのプログラムのマークアップ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. There is a set of directives allowing documenting command-line programs:

コマンドラインのプログラムの説明を行うためのディレクティブについて紹介します:

.. .. directive:: .. cmdoption:: name args, name args, ...

   Describes a command line option or switch.  Option argument names should be
   enclosed in angle brackets.  Example::

      .. cmdoption:: -m <module>, --module <module>

         Run a module as a script.

   The directive will create a cross-reference target named after the *first*
   option, referencable by :role:`option` (in the example case, you'd use
   something like ``:option:`-m```).

.. directive:: .. cmdoption:: 名前 引数, 名前 引数, ...

   コマンドラインオプション、もしくはスイッチについて説明をします。オプションの引き数名は不等号でくくる必要があります::

      .. cmdoption:: -m <モジュール>, --module <モジュール>

         モジュールをスクリプトとみなして実行します

   このディレクティブは *最初* のオプションを名前付きのターゲットとみなして、クロスリファレンスを作成します。これは :role:`option` にて参照可能です。このサンプルの場合は、 ``:option:`-m``` という形式でリンクを張ることができます。

.. .. directive:: .. envvar:: name

   Describes an environment variable that the documented code or program uses or
   defines.

.. directive:: .. envvar:: 名前

   現在ドキュメントの対象ととなっているコードやプログラムが使用したり、定義する環境変数について説明します。

.. .. directive:: .. program:: name

   Like :dir:`currentmodule`, this directive produces no output.  Instead, it
   serves to notify Sphinx that all following :dir:`cmdoption` directives
   document options for the program called *name*.

   If you use :dir:`program`, you have to qualify the references in your
   :role:`option` roles by the program name, so if you have the following
   situation ::

      .. program:: rm

      .. cmdoption:: -r

         Work recursively.

      .. program:: svn

      .. cmdoption:: -r revision

         Specify the revision to work upon.

   then ``:option:`rm -r``` would refer to the first option, while
   ``:option:`svn -r``` would refer to the second one.

   The program name may contain spaces (in case you want to document subcommands
   like ``svn add`` and ``svn commit`` separately).

   .. versionadded:: 0.5

.. directive:: .. program:: 名前

   :dir:`currentmodule` と同様に、このディレクティブ何も出力しません。その代わりにこのディレクティブを定義すると、Sphinxはこの後に定義される :dir:`cmdoption` ディレクティブが説明するオプションが、ここで指定された *名前* を持つプログラムに属するということを認識できるようになります。

   :dir:`program` を使用する場合には、 :role:`option` ロールとプログラム名を適合させる必要があります。以下のような状況について見てみます::

      .. program:: rm

      .. cmdoption:: -r

         再帰的に動作するようになります

      .. program:: svn

      .. cmdoption:: -r revision

         作業中のワークに対してリビジョンを設定します

   この場合、 ``option`rm -r``` 最初のオプションを示し、 ``option:`svn -r``` は２番目のオプションを示します。

   プログラム名はスペースを含むこともできます。そのため、 ``svn add`` や、 ``svn commit`` などのサブコマンドを個別に取り扱いたい、というケースにも対応できます。

   .. versionadded:: 0.5


.. Custom description units
   ~~~~~~~~~~~~~~~~~~~~~~~~

説明のためのディレクティブのカスタマイズ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. There is also a generic version of these directives:

汎用的なバージョンのディレクティブも存在します:

.. .. directive:: .. describe:: text

   This directive produces the same formatting as the specific ones explained
   above but does not create index entries or cross-referencing targets.  It is
   used, for example, to describe the directives in this document. Example::

      .. describe:: opcode

         Describes a Python bytecode instruction.

.. directive:: .. describe:: テキスト

   このディレクティブは上記で説明してきたようなディレクティブを使ったのと、同じ形式にフォーマットされたテキストを生成します。その代わり、インデックスのエントリーや、クロスリファレンスのターゲットは作成されません。これを使用するケースとしては、 ちょうどこのドキュメントで行っているように( ``ソースコードを表示`` を参照)、ディレクティブ自身の説明を行いたい場合などに使用します::


      .. describe:: opcode

         Pythonバイトコードの命令を説明します

..  Extensions may add more directives like that, using the
    :func:`~sphinx.application.Sphinx.add_description_unit` method.

拡張機能を使うと、このようなディレクティブを追加できます。詳しくは、 :func:`~sphinx.application.Sphinx.add_description_unit` メソッドのドキュメントをご覧ください。

.. highlight:: rst

.. _domains:

Sphinxドメイン
==============

.. Sphinx Domains
   ==============

.. versionadded:: 1.0

.. What is a Domain?
   -----------------

ドメインとは何か？
------------------

.. Originally, Sphinx was conceived for a single project, the documentation of the
   Python language.  Shortly afterwards, it was made available for everyone as a
   documentation tool, but the documentation of Python modules remained deeply
   built in -- the most fundamental directives, like ``function``, were designed
   for Python objects.  Since Sphinx has become somewhat popular, interest
   developed in using it for many different purposes: C/C++ projects, JavaScript,
   or even reStructuredText markup (like in this documentation).

当初、Sphinxは一つのプロジェクトと、Pythonの言語のドキュメントのために作られました。その後少し経って、汎用的なドキュメントツールとして作り直されましたが、Pythonモジュールのドキュメントのため、という部分はツールの奥深くまで根を伸ばしたままでした。 ``function`` などのもっとも基本的なディレクティブは、Pythonのオブジェクトのために設計されました。しばらくたって、Sphinxはいくらか人気が出てきて、C/C++のプロジェクト、JavaScript, reStructuredText(このドキュメントのように)など、さまざまな異なる目的で使用したい、という要求が出てきました。

.. While this was always possible, it is now much easier to easily support
   documentation of projects using different programming languages or even ones not
   supported by the main Sphinx distribution, by providing a **domain** for every
   such purpose.

今までも書けないことはありませんでしたが、1.0からは、もっと簡単に、Sphinxでサポートしていない異なるプログラミング言語を使用したプロジェクトのドキュメントでも使える用になりました。 **ドメイン** という機能がこれを可能にします。

.. A domain is a collection of markup (reStructuredText :term:`directive`\ s and
   :term:`role`\ s) to describe and link to :term:`object`\ s belonging together,
   e.g. elements of a programming language.  Directive and role names in a domain
   have names like ``domain:name``, e.g. ``py:function``.  Domains can also provide
   custom indices (like the Python Module Index).

ドメインというのは、説明のためのマークアップ(reStructuredTextの :term:`ディレクティブ` と :term:`ロール`)と、プログラミング言語の構成部品と関連する :term:`オブジェクト` へのリンクによってできています。ドメインに属するディレクティブとロール名は ``py:function`` などのように、 ``ドメイン:名前:`` という名前を持ちます。ドメインを使って、Pythonのモジュール索引のような、専用の索引を作成することもできます。

.. Having domains means that there are no naming problems when one set of
   documentation wants to refer to e.g. C++ and Python classes.  It also means that
   extensions that support the documentation of whole new languages are much easier
   to write.

ドメインがあるということは、C++とPythonの両方のクラスに言及したいようなドキュメントを書く場合でも、名前が衝突する問題がない、ということです。まったく新しい言語のドキュメントをサポートするのも簡単になります。

.. This section describes what the domains that come with Sphinx provide.  The
   domain API is documented as well, in the section :ref:`domain-api`.

このセクションでは、Sphinxのドメインが何を提供するのか、ということを説明していきます。ドキュメントAPIの説明は :ref:`domain-api` で説明します。

.. _basic-domain-markup:

マークアップの基礎
------------------

.. Basic Markup
   ------------

.. Most domains provide a number of :dfn:`object description directives`, used to
   describe specific objects provided by modules.  Each directive requires one or
   more signatures to provide basic information about what is being described, and
   the content should be the description.  The basic version makes entries in the
   general index; if no index entry is desired, you can give the directive option
   flag ``:noindex:``.  An example using a Python domain directive:


ほとんどのドメインは、いくつかの :dfn:`object description directives` を提供しています。これを使って、モジュールが提供する特定のオブジェクトについて説明をしていきます。それぞれのディレクティブでは、何について説明しているか、説明すべき内容などの基本情報のためのフォーマットや統一のルールを定めています。基本的なスタイルのディレクティブは、全体の索引に、説明対象へのリンクを追加しますが、もし索引に追加したくなければ、ディレクティブのオプションフラグに ``:noindex:`` を追加します。例えば、Pythonのドメインのディレクティブの場合には、次のようになります::

   .. py:function:: spam(eggs)
                    ham(eggs)
      :noindex:
  
      Spam or ham the foo.

.. The domains also provide roles that link back to these object descriptions.  For
   example, to link to one of the functions described in the example above, you
   could say :

      The function :py:func:`spam` does a similar thing.

ドメインは、オブジェクトへのリンクを張るためのロールも提供します。例えば先ほどのサンプルの関数説明にリンクを張るためには、次のように書きます::

   関数 :py:func:`spam` は同じ処理を行います。

.. As you can see, both directive and role names contain the domain name and the
   directive name.

このように、ディレクティブとロール名の両方とも、ドメイン名とディレクティブ名の２つから構成されています。

.. .. rubric:: Default Domain

.. rubric:: デフォルトドメイン

.. To avoid having to writing the domain name all the time when you e.g. only
   describe Python objects, a default domain can be selected with either the config
   value :confval:`default_domain` or this directive:

もし、Pythonしか登場しないプロジェクトで、Pythonオブジェクトの説明しか書かない場合に、ドメイン名を毎回書かなくても良いようにする機能が提供されています。 :confval:`default_domain` 設定値と、専用のディレクティブの2つの方法で、デフォルトのドメインを指定できるようになっています。

.. rst:directive:: .. default-domain:: name

   .. Select a new default domain.  While the :confval:`default_domain` selects a
      global default, this only has an effect within the same file.

   新しいデフォルトのドメインを設定します。 :confval:`default_domain` はプロジェクト全体のデフォルトを決定しますが、このディレクティブは同じファイル内にのみ影響を与えます。n

.. If no other default is selected, the Python domain (named ``py``) is the default
   one, mostly for compatibility with documentation written for older versions of
   Sphinx.

もしもデフォルトが設定されないと、Pythonドメイン(``py``)がデフォルトになります。これは、過去のバージョンのSphinxで書かれたドキュメントと互換性があります。

.. Directives and roles that belong to the default domain can be mentioned without
   giving the domain name, i.e. ::

      .. function:: pyfunc()
 
         Describes a Python function.
  
      Reference to :func:`pyfunc`.

デフォルトドメインに属するディレクティブとロールを書く場合には、ドメイン名を入れる必要はありません::

   .. function:: pyfunc()

      Pythonの関数の説明

   :func:`pyfunc` への参照。


.. Cross-referencing syntax
   ~~~~~~~~~~~~~~~~~~~~~~~~

クロスリファレンス文法
~~~~~~~~~~~~~~~~~~~~~~

.. For cross-reference roles provided by domains, the same facilities exist as for
   general cross-references.  See :ref:`xref-syntax`.

汎用的なクロスリファレンスのために使用されるのと同じような機能を持つ、クロスリファレンスのためのロールが、ドメインによって提供されます。詳しくは :ref:`xref-syntax` を参照してください。n

.. In short:

簡単に説明すると:

.. * You may supply an explicit title and reference target: ``:rst:role:`title
    <target>``` will refer to *target*, but the link text will be *title*.

* 明示的なリンク名と、リンクターゲットを指定できます。 ``:rst:role:`タイトル <ターゲット>``` と書くと、 **ターゲット** を参照しますが、リンクテキストは **タイトル** になります。

.. * If you prefix the content with ``!``, no reference/hyperlink will be created.

* もしも先頭に ``!`` が付けられると、ハイパーリンクや参照は作成されません。

.. * If you prefix the content with ``~``, the link text will only be the last
     component of the target.  For example, ``:py:meth:`~Queue.Queue.get``` will
     refer to ``Queue.Queue.get`` but only display ``get`` as the link text.

* もし、先頭に ``~`` が付けられると、ターゲットの最後の項目だけがリンクテキストになります。例えば、 ``:py:meth:`~Queue.Queue.get``` と書かれると、 ``Queue.Queue.get`` を参照しますが、リンクテキストとして表示されるのは、 ``get`` だけになります。


.. The Python Domain
   -----------------

Pythonドメイン
--------------

.. The Python domain (name **py**) provides the following directives for module
   declarations:

Pythonドメイン(**py**)では、モジュールの説明のために、次のようなディレクティブを提供しています:

.. .. rst:directive:: .. py:module:: name

.. rst:directive:: .. py:module:: 名前

   .. This directive marks the beginning of the description of a module (or package
      submodule, in which case the name should be fully qualified, including the
      package name).  It does not create content (like e.g. :rst:dir:`py:class` does).

   このディレクティブはモジュールの説明の開始時に使用します。パッケージやサブモジュールにも使用できますが、この場合はパッケージ名を含む、完全な名前を指定してください。この ディレクティブは :rst:dir:`py:class` ディレクティブのようなコンテンツを作成することはできません。

   .. This directive will also cause an entry in the global module index.

   このディレクティブを使用すると、グローバルなモジュール索引に項目が追加されます。

   .. The ``platform`` option, if present, is a comma-separated list of the
      platforms on which the module is available (if it is available on all
      platforms, the option should be omitted).  The keys are short identifiers;
      examples that are in use include "IRIX", "Mac", "Windows", and "Unix".  It is
      important to use a key which has already been used when applicable.

   ``platform`` オプションが存在していれば、そのモジュールが利用可能なモジュールをカンマ区切りで指定します。もしすべてのプラットフォームで利用可能であれば、このオプションは使用しないようにしましょう。プラットフォーム名としては、短い識別子、例えば、"IRIX", "Mac", "Windows", "Unix"などから利用してください。もし適用時点ですでに使用されているキーがあれば、それを使用してください。

   .. The ``synopsis`` option should consist of one sentence describing the
      module's purpose -- it is currently only used in the Global Module Index.

   ``synopsis`` オプションには、モジュールの目的を説明する文章を書くことができます。現在のバージョンでは、これはグローバルモジュールインデックスの中でのみ使用されます。

   .. The ``deprecated`` option can be given (with no value) to mark a module as
      deprecated; it will be designated as such in various locations then.

   ``deprecated`` オプションを使用すると、このモジュールが古くて、使用するのを推奨しない、ということを示すことができます。オプションは取りません。このディレクティブは様々な場所で使用されるでしょう。


.. .. rst:directive:: .. py:currentmodule:: name

.. rst:directive:: .. py:currentmodule:: 名前

   .. This directive tells Sphinx that the classes, functions etc. documented from
      here are in the given module (like :rst:dir:`py:module`), but it will not create
      index entries, an entry in the Global Module Index, or a link target for
      :rst:role:`mod`.  This is helpful in situations where documentation for things in
      a module is spread over multiple files or sections -- one location has the
      :rst:dir:`py:module` directive, the others only :rst:dir:`py:currentmodule`.

   このディレクティブはSphinxに対して、この行以降のクラスや関数などが、指定された与えられたモジュール (:rst:dir:`py:module` のように)の中にある、ということを通知します。これを使用しても、索引のエントリーは作成されません。 :rst:role:`mod` へのリンクターゲットも作成されません。このディレクティブは、モジュールに含まれる項目へのドキュメントが様々なファイルやセクションに分割されている場合に便利です。この場合には一カ所だけ :rst:dir:`py:module` ディレクティブを使用して、他の箇所で :rst:dir:`py:currentmodule` を使用するようにします。


.. The following directives are provided for module and class contents:

モジュールとクラスの中の構成要素を記述するために、次のようなディレクティブが提供されています:


.. .. rst:directive:: .. py:data:: name

.. rst:directive:: .. py:data:: データ名

   .. Describes global data in a module, including both variables and values used
      as "defined constants."  Class and object attributes are not documented
      using this environment.

   モジュール内のグローバルなデータの説明をします。変数も値も"定義された定数"として取り込むことができます。クラスとオブジェクトの属性はこの環境を使用してドキュメントを書くことはできません。


.. .. rst:directive:: .. py:exception:: name

.. rst:directive:: .. py:exception:: 例外名

   .. Describes an exception class.  The signature can, but need not include
      parentheses with constructor arguments.

   例外クラスの説明をします。シグニチャには、コンストラクタの引数を括弧付きで含めることもできますが、しなくてもかまいません。


.. .. rst:directive:: .. py:function:: name(signature)

.. rst:directive:: .. py:function:: 関数名(シグニチャ)

   .. Describes a module-level function.  The signature should include the
      parameters, enclosing optional parameters in brackets.  Default values can be
      given if it enhances clarity; see :ref:`signatures`.  For example::

   モジュールレベル関数の説明です。シグニチャはパラメータを含めます。オプションのパラメータに対してはカッコでくくります。分かりやすさを上げる目的でデフォルト値を入れることもできます。 :ref:`signatures` の説明も参照してください。サンプル::

      .. py:function:: Timer.repeat([repeat=3[, number=1000000]])

   .. Object methods are not documented using this directive. Bound object methods
      placed in the module namespace as part of the public interface of the module
      are documented using this, as they are equivalent to normal functions for
      most purposes.

   オブジェクトのメソッドはこのディレクティブではドキュメントを記述することはできません。モジュールの名前空間にあり、モジュールの公開インタフェースとして作成されているメソッドに限って使用することができます。これらは通常の関数とほぼ同じように使用できます。

   .. The description should include information about the parameters required and
      how they are used (especially whether mutable objects passed as parameters
      are modified), side effects, and possible exceptions.  A small example may be
      provided.

   説明にはパラメータに必要な関する情報と、それらがどのように使用されるのか(変更可能なオブジェクトが渡されたときに、変更されるのかどうか)、副作用、投げられる可能性のある例外の情報を含まなければなりません。小さいサンプルが提供されるでしょう。


.. .. rst:directive:: .. py:class:: name[(signature)]

.. rst:directive:: .. py:class:: クラス名[(シグニチャ)]

   .. Describes a class.  The signature can include parentheses with parameters
      which will be shown as the constructor arguments.  See also
      :ref:`signatures`.

   クラスについて説明します。シグニチャにはコンストラクタ引数になるパラメータも含めることができます。 :ref:`signatures` も参照してください。

   .. Methods and attributes belonging to the class should be placed in this
      directive's body.  If they are placed outside, the supplied name should
      contain the class name so that cross-references still work.  Example::

      .. py:class:: Foo
         .. py:method:: quux()

      -- or --

      .. py:class:: Bar

      .. py:method:: Bar.quux()

   このクラスに属する属性とメソッドのディレクティブはこのディレクティブの本体の中に記述します。このクラスの外に書いた場合は、提供された名前にクラス名が含まれていれば、クロスリファレンスは動作します。サンプル::

      .. class:: Foo
         .. method:: quux()

      -- あるいは --

      .. class:: Bar

      .. method:: Bar.quux()

   .. The first way is the preferred one.

   最初の書き方が推奨です。


.. .. rst:directive:: .. py:attribute:: name

.. rst:directive:: .. py:attribute:: 属性名

   .. Describes an object data attribute.  The description should include
      information about the type of the data to be expected and whether it may be
      changed directly.

   オブジェクトの属性のデータの説明をします。この説明には期待されるデータの型、値を直接変更することができるかどうか、という情報を含めます。


.. .. rst:directive:: .. py:method:: name(signature)

.. rst:directive:: .. py:method:: メソッド名(シグニチャ)

   .. Describes an object method.  The parameters should not include the ``self``
      parameter.  The description should include similar information to that
      described for ``function``.  See also :ref:`signatures`.

   オブジェクトのメソッドの説明をします。パラメータからは ``self`` パラメータははずします。この説明には ``function`` と同じ情報を記述するようにします。 :ref:`signatures` も参照してください。


.. 
   .. rst:directive:: .. py:staticmethod:: name(signature)

.. rst:directive:: .. py:staticmethod:: メソッド名(シグニチャ)

   :rst:dir:`py:method` とほぼ一緒ですが、メソッドがスタティックメソッドであるということを表します。

   .. Like :rst:dir:`py:method`, but indicates that the method is a static method.


   .. versionadded:: 0.4


.. .. rst:directive:: .. py:classmethod:: name(signature)

.. rst:directive:: .. py:classmethod:: メソッド名(シグニチャ)

   .. Like :rst:dir:`py:method`, but indicates that the method is a static method.

   :rst:dir:`py:method` とほぼ一緒ですが、メソッドがクラスメソッドであるということを表します。

   .. versionadded:: 0.6


.. _signatures:

Pythonシグニチャ
~~~~~~~~~~~~~~~~

.. Python Signatures
   ~~~~~~~~~~~~~~~~~

.. Signatures of functions, methods and class constructors can be given like they
   would be written in Python, with the exception that optional parameters can be
   indicated by brackets:

関数やメソッド、クラスのコンストラクタのシグニチャは、オプションパラメータにカッコを使うのを除き、Pythonで書くように記述することができます::

   .. py:function:: compile(source[, filename[, symbol]])

.. It is customary to put the opening bracket before the comma.  In addition to
   this "nested" bracket style, a "flat" style can also be used, due to the fact
   that most optional parameters can be given independently:

このような省略可能な引数を表す場合には、慣習的にカンマの前に開きカッコを置きます。省略できる引数が二つ以上ある場合には、カッコを入れ子にするスタイルと、フラットにするスタイルの両方があります。このような場合にはほとんどの場合、オプションの引数は個別に与えることができます::

   .. py:function:: compile(source[, filename, symbol])

.. Default values for optional arguments can be given (but if they contain commas,
   they will confuse the signature parser).  Python 3-style argument annotations
   can also be given as well as return type annotations:

オプション引数のデフォルト値を与えることもできます。ただし、値にカンマが含まれると、シグニチャのパーサはうまく動作しません。Pythonの３つのスタイルの引数のアノテーションと同様に、返り値の型も記述することができます::

   .. py:function:: compile(source : string[, filename, symbol]) -> ast object


.. Info field lists
   ~~~~~~~~~~~~~~~~

詳細情報フィールドのリスト
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 0.4

.. Inside Python object description directives, reST field lists with these fields
   are recognized and formatted nicely:

Pythonのオブジェクト説明のためのディレクティブの内側には、適切に情報が明示されて、決まったルールに従ったreSTフィールドを配置することができます:

.. * ``param``, ``parameter``, ``arg``, ``argument``, ``key``, ``keyword``:
     Description of a parameter.
   * ``type``: Type of a parameter.
   * ``raises``, ``raise``, ``except``, ``exception``: That (and when) a specific
     exception is raised.
   * ``var``, ``ivar``, ``cvar``: Description of a variable.
   * ``returns``, ``return``: Description of the return value.
   * ``rtype``: Return type.

*  ``param``, ``parameter``, ``arg``, ``argument``, ``key``, ``keyword``: 引数の説明です。
* ``type``: 引数のタイプです
* ``raises``, ``raise``, ``except``, ``exception``: この中から投げられる例外(いつ投げられるか？)を定義します
* ``var``, ``ivar``, ``cvar``: 変数の説明をします
* ``returns``, ``return``: 返り値の値について説明をします
* ``rtype``: 返り値の型です。

.. The field names must consist of one of these keywords and an argument (except
   for ``returns`` and ``rtype``, which do not need an argument).  This is best
   explained by an example:

   .. py:function:: format_exception(etype, value, tb[, limit=None])

      Format the exception with a traceback.

      :param etype: exception type
      :param value: exception value
      :param tb: traceback object
      :param limit: maximum number of stack frames to show
      :type limit: integer or None
      :rtype: list of strings

フィールドは、 ``return``, ``rtype`` 以外の場合は、上記のキーワードのうち、どれかと、引数を一つが引数として設定されています。 ``return``, ``rtype`` だけは引数を取りません。サンプルを見ていただくのが一番でしょう::

   .. function:: format_exception(etype, value, tb[, limit=None])

      トレースバック付きで、例外を人の読める形式にフォーマットします。

      :param etype: 例外のタイプ
      :param value: 例外オブジェクト
      :param tb: トレースバックオブジェクト
      :param limit: 表示するスタックフレームの数の最大数
      :type limit: 数値 or None
      :rtype: 文字列のリスト


.. It is also possible to combine parameter type and description, if the type is a
   single word, like this::

   :param integer limit: maximum number of stack frames to show

型情報が一語で表せる場合には、属性の型と説明をひとつにまとめることもできます::

   :param integer limit: 表示するスタックフレームの数の最大数

.. This will render like this:

   .. py:function:: format_exception(etype, value, tb[, limit=None])
      :noindex:

      Format the exception with a traceback.

      :param etype: exception type
      :param value: exception value
      :param tb: traceback object
      :param limit: maximum number of stack frames to show
      :type limit: integer or None
      :rtype: list of strings


これは次のようにレンダリングされます:

   .. function:: format_exception(etype, value, tb[, limit=None])
      :noindex:

      トレースバック付きで、例外を人の読める形式にフォーマットします。

      :param etype: 例外のタイプ
      :param value: 例外オブジェクト
      :param tb: トレースバックオブジェクト
      :param limit: 表示するスタックフレームの数の最大数
      :type limit: 数値 or None
      :rtype: 文字列のリスト


.. Cross-referencing Python objects
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pythonオブジェクトのクロススリファンレス
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. The following roles refer to objects in modules and are possibly hyperlinked if
   a matching identifier is found:

以下のロールを使用すると、モジュール内のオブジェクトを参照することができます。一致する識別子が見つかれば、ハイパーリンクが作成されます:


.. rst:role:: py:mod

   .. Reference a module; a dotted name may be used.  This should also be used for
      package names.

   モジュールへの参照です。ドットで区切られた名前も使用できます。これはパッケージ名としても利用可能です。


.. rst:role:: py:func

   .. Reference a Python function; dotted names may be used.  The role text needs
      not include trailing parentheses to enhance readability; they will be added
      automatically by Sphinx if the :confval:`add_function_parentheses` config
      value is true (the default).

   Pythonの関数への参照です。ドットで区切られた名前も使用できます。ロールのテキストは読みやすさのために括弧を後ろに含める必要はありません。 :confval:`add_function_parentheses` 設定値をtrue(デフォルト)にしておくと、Sphinxが自動で括弧を追加します。


.. rst:role:: py:data

   .. Reference a module-level variable.

   モジュール変数を参照します。


.. rst:role:: py:const

   .. Reference a "defined" constant.  This may be a C-language ``#define`` or a
      Python variable that is not intended to be changed.

   定義済みの定数への参照です。これはC言語の ``#define`` や、 Pythonで変更されることのない変数に使います。


.. rst:role:: py:class

   .. Reference a class; a dotted name may be used.

   クラス名です。ドットで区切られた名前も使用できます。

.. rst:role:: py:meth

   .. Reference a method of an object.  The role text can include the type name and
      the method name; if it occurs within the description of a type, the type name
      can be omitted.  A dotted name may be used.

   オブジェクトのメソッドへの参照です。ロールのテキストには型名とメソッド名を含めなければなりません。ただし、型の記述中に書く場合には省略することもできます。ドットで区切られた名前も使用できます。


.. rst:role:: py:attr

   .. Reference a data attribute of an object.

   オブジェクトの属性への参照です。

.. rst:role:: py:exc

   .. Reference an exception.  A dotted name may be used.

   例外への参照です。ドットで区切られた名前も使用できます。

.. rst:role:: py:obj

   .. Reference an object of unspecified type.  Useful e.g. as the
      :confval:`default_role`.

   型が指定されていないオブジェクトの名前です。 :confval:`default_role` 一緒に使用すると便利です。

   .. versionadded:: 0.4

.. The name enclosed in this markup can include a module name and/or a class name.
   For example, ``:py:func:`filter``` could refer to a function named ``filter`` in
   the current module, or the built-in function of that name.  In contrast,
   ``:py:func:`foo.filter``` clearly refers to the ``filter`` function in the
   ``foo`` module.

このマークアップの中の名前には、モジュール名, クラス名なども含めることができます。例えば、 ``:py:func:`filter``` は現在のモジュールに定義されている ``filter`` という名前の関数か、その名前を持つ組み込み関数をあらわします。 ``:py:func:`foo.filter``` と明示的に書くと、 ``foo`` モジュールの中の ``filter`` 関数を表します。

.. Normally, names in these roles are searched first without any further
   qualification, then with the current module name prepended, then with the
   current module and class name (if any) prepended.  If you prefix the name with a
   dot, this order is reversed.  For example, in the documentation of Python's
   :mod:`codecs` module, ``:py:func:`open``` always refers to the built-in
   function, while ``:py:func:`.open``` refers to :func:`codecs.open`.

通常、これらのロールで使用される名前は、最初は修飾子なしで検索されます。次に現在のモジュール名を前に付けて検索されます。その次に現在のモジュール名とクラス名(あれば)を付けて検索されます。もし、ドットが先頭についた名前が指定された場合には、この探索順は逆になります。例えば、 :mod:`codecs` というPythonモジュールの定義の中で ``:py:func:`open``` が定義されると、常に組み込み関数を参照しますが、 ``:py:func:`.open``` と書かれると、 :func:`codecs.open` を参照するようになります。

.. A similar heuristic is used to determine whether the name is an attribute of the
   currently documented class.

属性名が、現在のクラスのものかどうかを決定するのにも、同様の名前検索の仕組みが使用されます。


.. The C Domain
   ------------

C言語ドメイン
---------------

.. The C domain (name **c**) is suited for documentation of C API.

C言語ドメイン(**c**)はC言語のAPIのドキュメントを書くのに適しています。

..
   .. rst:directive:: .. c:function:: type name(signature)

.. rst:directive:: .. c:function:: 型 関数名(シグニチャ)

   .. Describes a C function. The signature should be given as in C, e.g.:

   Cの関数の説明に使用します。シグニチャはC言語内で書かれる様に記述します。例えば以下のように書きます::

      .. c:function:: PyObject* PyType_GenericAlloc(PyTypeObject *type, Py_ssize_t nitems)

   .. This is also used to describe function-like preprocessor macros.  The names
      of the arguments should be given so they may be used in the description.

   これは、関数のようなプリプロセッサマクロにも使用することができます。説明の中で使用されることもあるため、引数名も書く必要があります。

   .. Note that you don't have to backslash-escape asterisks in the signature, as
      it is not parsed by the reST inliner.

   シグネチャ内のアスタリスクはバックスラッシュでエスケープする必要はありません。この中はreSTの行内のテキスト処理のパーサは実行されず、専用のパーサで処理されます。

..
  .. rst:directive:: .. c:member:: type name

.. rst:directive:: .. c:member:: 型 構造体メンバー名

   .. Describes a C struct member. Example signature:

   C言語の構造体メンバーの説明をします。以下のように記述します::

      .. c:member:: PyObject* PyTypeObject.tp_bases

   .. The text of the description should include the range of values allowed, how
      the value should be interpreted, and whether the value can be changed.
      References to structure members in text should use the ``member`` role.

   説明のテキストには受け入れ可能な値の範囲、値がどのように解釈されるべきか、値が変更可能かどうかという情報を入れるべきです。構造体のメンバーへの参照をテキストの中で書きたい場合には、 ``member`` ロールを使用すべきです。


..
  .. rst:directive:: .. c:macro:: name

.. rst:directive:: .. c:macro:: マクロ名

   .. Describes a "simple" C macro.  Simple macros are macros which are used for
      code expansion, but which do not take arguments so cannot be described as
      functions.  This is not to be used for simple constant definitions.  Examples
      of its use in the Python documentation include :c:macro:`PyObject_HEAD` and
      :c:macro:`Py_BEGIN_ALLOW_THREADS`.

   シンプルなC言語のマクロの説明をします。シンプルなマクロというのは、単純なコード展開だけをするもので、引数を取らないものです。また、単純な定数定義にも使用しません。このディレクティブのサンプルを見るには、Pythonドキュメントの :c:macro:`PyObject_HEAD`, :c:macro:`Py_BEGIN_ALLOW_THREADS` を参照してください。


.. 
   .. rst:directive:: .. c:type:: name

.. rst:directive:: .. c:type:: 型名

   .. Describes a C type (whether defined by a typedef or struct). The signature
      should just be the type name.

   C言語の型名を説明します。型というのは、typedefかstructで定義されるものです。シグニチャには型名を指定します。


..
   .. rst:directive:: .. c:var:: type name

.. rst:directive:: .. c:var:: 型 変数名

   .. Describes a global C variable.  The signature should include the type, such
      as:

   グローバルなC言語の変数について説明します。シグニチャは型を含む必要があります。次のように記述します::

      .. c:var:: PyObject* PyClass_Type


.. Cross-referencing C constructs
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

C言語の要素へのクロスリファレンス
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. The following roles create cross-references to C-language constructs if they are
   defined in the documentation:

以下のロールは、もしドキュメントの中に定義の説明があれば、C言語の要素へのクロスリファレンスを作成します:

.. rst:role:: c:data

   .. Reference a C-language variable.

   C言語の変数への参照です。

.. rst:role:: c:func

   .. Reference a C-language function. Should include trailing parentheses.

   C言語の関数への参照です。カッコを省略することはできません。

.. rst:role:: c:macro

   .. Reference a "simple" C macro, as defined above.

   前の説明で述べた、シンプルなC言語のマクロへの参照です。

.. rst:role:: c:type

   .. Reference a C-language type.

   C言語の型への参照です。


.. The C++ Domain
   --------------

C++ドメイン
-----------

.. The C++ domain (name **cpp**) supports documenting C++ projects.

C++ドメインは(**cpp**)は、C++プロジェクトのドキュメント作成をサポートします。

.. The following directives are available:

次のようなディレクティブが利用可能です:

..
   .. rst:directive:: .. cpp:class:: signatures
                  .. cpp:function:: signatures
                  .. cpp:member:: signatures
                  .. cpp:type:: signatures

.. rst:directive:: .. cpp:class:: シグニチャ
               .. cpp:function:: シグニチャ
               .. cpp:member:: シグニチャ
               .. cpp:type:: シグニチャ

   .. Describe a C++ object.  Full signature specification is supported -- give the
      signature as you would in the declaration.  Example:

      .. cpp:function:: const int IntArray::operator[]

         Describes the indexing operator of IntArrays.

   C++オブジェクトの説明をします。完全なシグニチャ定義をサポートしています。C++の宣言部で使用するようにシグニチャを書くことができます::

      .. cpp:function:: const int IntArray::operator[]

         IntArrayクラスの配列演算子の説明・・・

.. 
   .. rst:directive:: .. cpp:namespace:: namespace

.. rst:directive:: .. cpp:namespace:: 名前空間

   .. Select the current C++ namespace for the following objects.

   ドキュメントの中で、この行以降で説明するオブジェクトが所属するC++の名前空間を選択します。

.. These roles link to the given object types:

このドメインは次のようなオブジェクトの種類へのロールを提供しています:

.. rst:role:: cpp:class
          cpp:func
          cpp:member
          cpp:type

   .. Reference a C++ object.  You can give the full signature (and need to, for
      overloaded functions.)

   C++オブジェクトへの参照です。完全なシグニチャを指定することができます。オーバーロードされた関数へのリンクを張る場合には、完全なシグニチャを指定する必要があります。


.. The Standard Domain
   -------------------

標準ドメイン
------------

.. The so-called "standard" domain collects all markup that doesn't warrant a
   domain of its own.  Its directives and roles are not prefixed with a domain
   name.

標準ドメインには、固有のドメインを作るまでもないすべてのマークアップが含まれます。これらのディレクティブやロールには、ドメイン名のプリフィックスは付きません。

.. The standard domain is also where custom object descriptions, added using the
   :func:`~sphinx.application.Sphinx.add_object_type` API, are placed.

標準ドメインには、 :func:`~sphinx.application.Sphinx.add_object_type` APIを使って追加されたカスタムの説明ディレクティブ、ロールも含まれます。

.. There is a set of directives allowing documenting command-line programs:

現在は、コマンドラインのプログラムを説明するためのディレクティブ群が提供されています:

..
   .. rst:directive:: .. option:: name args, name args, ...

.. rst:directive:: .. option:: 名前 引数, 名前 引数, ...

   .. Describes a command line option or switch.  Option argument names should be
      enclosed in angle brackets.  Example:

         .. option:: -m <module>, --module <module>

            Run a module as a script.

   コマンドラインオプションやスイッチの説明をします。オプションの引数名は不等号でくくる必要があります::

      .. option:: -m <モジュール>, --module <モジュール>

         モジュールをスクリプトとみなして実行します

   .. The directive will create a cross-reference target named after the *first*
      option, referencable by :rst:role:`option` (in the example case, you'd use
      something like ``:option:`-m```).

   このディレクティブは *最初* のオプションを名前付きのターゲットとみなして、クロスリファレンスを作成します。これは :rst:role:`option` にて参照可能です。このサンプルの場合は、 ``:option:`-m``` という形式でリンクを張ることができます。


..
   .. rst:directive:: .. envvar:: name

.. rst:directive:: .. envvar:: 名前

   .. Describes an environment variable that the documented code or program uses or
      defines.  Referencable by :rst:role:`envvar`.

   現在ドキュメントの対象ととなっているコードやプログラムが使用したり、定義する環境変数について説明します。 :rst:role:`envvar` というロールを使って参照することができます。


..
   .. rst:directive:: .. program:: name

.. rst:directive:: .. program:: 名前

   .. Like :rst:dir:`py:currentmodule`, this directive produces no output.  Instead, it
      serves to notify Sphinx that all following :rst:dir:`option` directives
      document options for the program called *name*.

   :rst:dir:`py:currentmodule` と同様に、このディレクティブは何も出力しません。その代わりにこのディレクティブを定義すると、Sphinxはこの後に定義される :rst:dir:`option` ディレクティブが説明するオプションが、ここで指定された *名前* を持つプログラムに属するということを認識できるようになります。

   .. If you use :rst:dir:`program`, you have to qualify the references in your
      :rst:role:`option` roles by the program name, so if you have the following
      situation :

      .. program:: rm

      .. option:: -r

         Work recursively.

      .. program:: svn

      .. option:: -r revision

         Specify the revision to work upon.

   :rst:dir:`program` を使用する場合には、 :rst:role:`option` ロールとプログラム名を適合させる必要があります。以下のような状況について見てみます::

      .. program:: rm

      .. option:: -r

         再帰的に動作するようになります

      .. program:: svn

      .. option:: -r revision

         作業中のワークに対してリビジョンを設定します

   .. then ``:option:`rm -r``` would refer to the first option, while
      ``:option:`svn -r``` would refer to the second one.

   この場合、 ``option`rm -r``` 最初のオプションを示し、 ``option:`svn -r``` は２番目のオプションを示します。

   .. The program name may contain spaces (in case you want to document subcommands
      like ``svn add`` and ``svn commit`` separately).

   プログラム名はスペースを含むこともできます。そのため、 ``svn add`` や、 ``svn commit`` などのサブコマンドを個別に取り扱いたい、というケースにも対応できます。

   .. versionadded:: 0.5


.. There is also a very generic object description directive, which is not tied to
   any domain:

どこのドメインにも俗さ名様な、非常に汎用的なオブジェクトの説明用のディレクティブも存在します:


.. .. rst:directive:: .. describe:: text
                  .. object:: text

.. rst:directive:: .. describe:: テキスト
               .. object:: テキスト

   .. This directive produces the same formatting as the specific ones provided by
      domains, but does not create index entries or cross-referencing targets.
      Example:

      .. describe:: PAPER

         You can set this variable to select a paper size.

   このディレクティブはドメインで提供されているディレクティブを使ったのと、同じ形式にフォーマットされたテキストを生成します。その代わり、インデックスのエントリーや、クロスリファレンスのターゲットは作成されません::

      .. describe:: PAPER

         この変数を定義すると、用紙サイズを変更することができます。


.. The JavaScript Domain
   ---------------------

JavaScriptドメイン
------------------

.. The JavaScript domain (name **js**) provides the following directives:

JavaScriptドメイン(**js**)は次のようなディレクティブを提供します:

..
   .. rst:directive:: .. js:function:: name(signature)

.. rst:directive:: .. js:function:: 名前(シグニチャ)

   .. Describes a JavaScript function, method or constructor.  If you want to
      describe arguments as optional use square brackets as :ref:`documented
      <signatures>` for Python signatures.

   JavaScriptの関数、メソッド、コンストラクタの説明をします。オプショナルな引数を説明したい場合には、Pythonシグニチャのために :ref:`説明したように <signatures>` 角カッコを使用します。

   .. You can use fields to give more details about arguments and their expected
      types, errors which may be thrown by the function, and the value being
      returned:

      .. js:function:: $.getJSON(href, callback[, errback])

         :param string href: An URI to the location of the resource.
         :param callback: Get's called with the object.
         :param errback:
             Get's called in case the request fails. And a lot of other
             text so we need multiple lines
         :throws SomeError: For whatever reason in that case.
         :returns: Something

   引数や期待される型、関数から投げられるエラー、returnで返される値などのフィールド情報の詳細を書くこともできます::

      .. js:function:: $.getJSON(href, callback[, errback])

         :param string href: リソースのある場所を示すURI
         :param callback: GETの応答が帰ってきたときに呼ばれるオブジェクトを受け取るコールバック
         :param errback:
             リクエストにエラーが発生したときに、呼ばれるコールバック。
             このように多くの情報が必要なら複数行にかけて書くこともできます。
         :throws SomeError: エラーが発生する理由
         :returns: 何か

   .. This is rendered as:

      .. js:function:: $.getJSON(href, callback[, errback])

        :param string href: An URI to the location of the resource.
        :param callback: Get's called with the object.
        :param errback:
            Get's called in case the request fails. And a lot of other
            text so we need multiple lines.
        :throws SomeError: For whatever reason in that case.
        :returns: Something

   次のようにレンダリングされます:

      .. js:function:: $.getJSON(href, callback[, errback])

        :param string href: リソースのある場所を示すURI
        :param callback: GETの応答が帰ってきたときに呼ばれるオブジェクトを受け取るコールバック
        :param errback:
             リクエストにエラーが発生したときに、呼ばれるコールバック。
             このように多くの情報が必要なら複数行にかけて書くこともできます。
        :throws SomeError: エラーが発生する理由
        :returns: 何か


..
   .. rst:directive:: .. js:data:: name

.. rst:directive:: .. js:data:: 名前

   .. Describes a global variable or constant.

   グローバル変数や定数の説明です。

..
   .. rst:directive:: .. js:attribute:: object.name

.. rst:directive:: .. js:attribute:: オブジェクト.属性名

   .. Describes the attribute *name* of *object*.

   **オブジェクト** の持つ **属性名** を説明します。

.. These roles are provided to refer to the described objects:

このドメインでは、オブジェクトの説明を参照する、次のようなロールが提供されています:

.. rst:role:: js:func
              js:data
              js:attr


.. The reStructuredText domain
   ---------------------------

reStructuredTextドメイン
------------------------

.. The reStructuredText domain (name **rst**) provides the following directives:

reStructuredTextドメイン(**rst**)は、次のようなディレクティブを提供します:

.. rst:directive:: .. rst:directive:: name

   .. Describes a reST directive.  The *name* can be a single directive name or
      actual directive syntax (`..` prefix and `::` suffix) with arguments that
      will be rendered differently. 

   reSTディレクティブの説明をします。 *name* には単独のディレクティブ名か、引数付きの実際のディレクティブの文法(`..` を前に付けたり、後ろに `::` を付けたり)で記述をします。

   .. For example

      .. rst:directive:: foo

         Foo description.

      .. rst:directive:: .. bar:: baz

         Bar description.

   サンプル::

      .. rst:directive:: foo

         Fooの説明

      .. rst:directive:: .. bar:: baz

         Barの説明

   .. will be rendered as:

   これは次のようにレンダリングされます

      .. rst:directive:: foo

         Fooの説明

      .. rst:directive:: .. bar:: baz

         Barの説明

   .. .. rst:directive:: foo

         Foo description.

      .. rst:directive:: .. bar:: baz

         Bar description.



.. rst:directive:: .. rst:role:: name

   .. Describes a reST role.  

   reSTのロールの説明をします。

   .. For example:

      .. rst:role:: foo

         Foo description.

   サンプル::

      .. rst:role:: foo

         Fooの説明

   .. will be rendered as:

   次のようにレンダリングされます:

      .. rst:role:: foo

         Fooの説明

   .. 
      .. rst:role:: foo

         Foo description.

.. These roles are provided to refer to the described objects:

説明したオブジェクトを参照するために、次のようなロールが提供されます:

.. rst:role:: rst:dir
              rst:role

.. highlight:: rest

.. :mod:`sphinx.ext.autodoc` -- Include documentation from docstrings

:mod:`sphinx.ext.autodoc` -- docstringからのドキュメントの取り込み
==================================================================

.. 
   module:: sphinx.ext.autodoc
   :synopsis: Include documentation from docstrings.

.. module:: sphinx.ext.autodoc
   :synopsis: docstringからのドキュメントの取り込み

..
  .. index:: pair: automatic; documentation
           single: docstring

.. index:: pair: 自動;ドキュメンテーション
           single: docstring

.. This extension can import the modules you are documenting, and pull in
   documentation from docstrings in a semi-automatic way.

この拡張機能は、docstringでドキュメントが書かれているモジュールをインポートして、そのdocstringから、半自動的にドキュメントを取り込みます。

.. note
   For Sphinx (actually, the Python interpreter that executes Sphinx) to find
   your module, it must be importable.  That means that the module or the
   package must be in one of the directories on :data:`sys.path` -- adapt your
   :data:`sys.path` in the configuration file accordingly.


.. note::
   Sphinx(実際にはSphinxを実行しているPythonインタプリタ)がモジュールを見つけられるためには、そのモジュールはインポート可能になっていなければなりません。これは、インポートしたいモジュールやパッケージが\ :data:`sys.path`\ で設定されているディレクトリのどれかに入っている必要があるということです。設定ファイル内で、適宜\ :data:`sys.path`\ を調整してください。

.. For this to work, the docstrings must of course be written in correct
   reStructuredText.  You can then use all of the usual Sphinx markup in the
   docstrings, and it will end up correctly in the documentation.  Together with
   hand-written documentation, this technique eases the pain of having to maintain
   two locations for documentation, while at the same time avoiding
   auto-generated-looking pure API documentation.

この機能がうまく働くためには、docstringは正しいreStructuredTextのフォーマットに従って記述されている必要があります。また、すべてのSphinxのマークアップをdocstringの中に書くことができ、最終的に正しくドキュメンテーションされます。手書きのドキュメントと一緒にモジュールのドキュメントを作成する場合には、純粋なAPIのドキュメントを同時に自動生成できるため、この機能を使うと両方を同時に管理しなければならないという痛みを和らげることができます。

.. :mod:`autodoc` provides several directives that are versions of the usual
   :dir:`module`, :dir:`class` and so forth.  On parsing time, they import the
   corresponding module and extract the docstring of the given objects, inserting
   them into the page source under a suitable :dir:`module`, :dir:`class` etc.
   directive.

:mod:`autodoc`は通常の\ :rst:dir:`module`, :rst:dir:`class`\ などのディレクティブに似た別バージョンのディレクティブを提供します。ドキュメントのパース時に指定されたモジュールを読み込んで、docstringを抽出して、その内容を通常の\ :dir:`module`, :dir:`class`\ ディレクティブと一緒に差込みます。

.. note
   Just as :rst:dir:`class` respects the current :rst:dir:`module`, :rst:dir:`autoclass`
   will also do so, and likewise with :rst:dir:`method` and :rst:dir:`class`.

.. note::

   :rst:dir:`class`\ を宣言したときに、既に定義されている\ :rst:dir:`module`\ の中に配置されるのと同様に、\ :rst:dir:`autoclass`\ も同じように振舞います。\ :rst:dir:`method`\  と\ :rst:dir:`class`\ についても同様です。


.. rst:directive:: automodule
                   autoclass
                   autoexception

   .. Document a module, class or exception.  All three directives will by default
      only insert the docstring of the object itself::

   モジュール、クラス、例外のドキュメントを作成します。これらのディレクティブは、デフォルトでは指定されたオブジェクトのdocstringだけを読み込みます::

      .. autoclass:: Noodle

   .. will produce source like this:

      .. class:: Noodle

         Noodle's docstring.

   これを実行すると以下のようなreSTのソースコードが生成されます::

      .. class:: Noodle

         Noodleのdocstring.

   .. The "auto" directives can also contain content of their own, it will be
      inserted into the resulting non-auto directive source after the docstring
      (but before any automatic member documentation).

   "auto"ディレクティブは、取り込むだけでなく、自分自身のコンテンツを書くことができます。自動取り込みされたドキュメントの後に挿入されます。

   .. Therefore, you can also mix automatic and non-automatic member documentation,
      like so:

      .. autoclass:: Noodle
         :members: eat, slurp

         .. method:: boil(time=10)

            Boil the noodle *time* minutes.

   そのため、以下のサンプルのように、自動のドキュメントと、手動で書いたメンバーのドキュメントを混ぜてかくこともできます::

      .. autoclass:: Noodle
         :members: eat, slurp

         .. method:: boil(time=10)

            *time* 分だけ、麺をゆでます。

   .. **Options and advanced usage**

   **オプション/進んだ使い方**

   .. * If you want to automatically document members, there's a ``members``
        option::

           .. automodule:: noodle
              :members:
  
        will document all module members (recursively), and ::

           .. autoclass:: Noodle
              :members:

        will document all non-private member functions and properties (that is,
        those whose name doesn't start with ``_``).

        You can also give an explicit list of members; only these will then be
        documented::

           .. autoclass:: Noodle
              :members: eat, slurp

   * もしも自動的にメンバーの関数やプロパティのドキュメントも取り込みたい場合には、\ ``members``\ オプションを使用します::

        .. automodule:: noodle
           :members:

     このように書くと、すべてのモジュールのメンバーを再帰的にドキュメントにしていきます。そして::

        .. autoclass:: Noodle
           :members:

     これをビルドすると、すべての非プライベートの関数とプロパティ(名前が\ ``_``\ 以外から始まる)のドキュメントが取り込まれます。

     また、ドキュメントを出力したいメンバーのリストを明示的に書くと、それらの指定されたメンバーのドキュメントが生成されます::

        .. autoclass:: Noodle
           :members: eat, slurp

   .. * If you want to make the ``members`` option the default, see
        :confval:`autodoc_default_flags`.

   * もしも、デフォルトでmembersオプションを有効にしたい場合には、 :confval:`autodoc_default_flags` を参照してください。

   .. * Members without docstrings will be left out, unless you give the
        ``undoc-members`` flag option::

   * ``undoc-members``\ フラグオプションを指定しないと、docstringの付いていないメンバーは省略されます::

        .. automodule:: noodle
           :members:
           :undoc-members:

   .. * For classes and exceptions, members inherited from base classes will be
        left out, unless you give the ``inherited-members`` flag option, in
        addition to ``members``::

           .. autoclass:: Noodle
              :members:
              :inherited-members:

        This can be combined with ``undoc-members`` to document *all* available
        members of the class or module.

        Note: this will lead to markup errors if the inherited members come from a
        module whose docstrings are not reST formatted.

   * クラスと例外で、\ ``members``\ と一緒に\ ``inherited-members``\ フラグオプションが指定されていない場合には、ベースクラスで定義されているメンバーは省略されます。を指定しないと、docstringの付いていないメンバーは省略されます::

        .. autoclass:: Noodle
           :members:
           :inherited-members:

     このフラグと\ ``undoc-members``\ を同時に適用すると、クラスとモジュールの持っている、\ **すべての**\ 利用可能なメンバーのドキュメントが作成されるようになります。

     注意: もしもdocstringがreST形式でないモジュールで定義されたメンバーがあると、マークアップエラーになるでしょう。

     .. versionadded:: 0.3

   .. * It's possible to override the signature for explicitly documented callable
        objects (functions, methods, classes) with the regular syntax that will
        override the signature gained from introspection::

           .. autoclass:: Noodle(type)

              .. automethod:: eat(persona)

        This is useful if the signature from the method is hidden by a decorator.

   * 通常は内省機能を使って情報を取得しますが、明示的にドキュメントを書くことで、通常の文法で定義された呼び出し可能なオブジェクト(関数、メソッド、クラス)の呼び出し規約(変数名など)を上書きすることができます::

        .. autoclass:: Noodle(type)

           .. automethod:: eat(persona)

     この機能はデコレータなどによって、メソッドの呼び出し規約が内省機能で取れない状態になっている場合に便利です。

     .. versionadded:: 0.4

   .. * The :rst:dir:`automodule`, :rst:dir:`autoclass` and :rst:dir:`autoexception` directives
        also support a flag option called ``show-inheritance``.  When given, a list
        of base classes will be inserted just below the class signature (when used
        with :rst:dir:`automodule`, this will be inserted for every class that is
        documented in the module).

        .. versionadded:: 0.4

   * :rst:dir:`automodule`\ と、\ :rst:dir:`autocalss`\ 、\ :rst:dir:`autoexception`\ ディレクティブは\ ``show-inheritance``\ というオプションをサポートしています。これが設定されると、クラスのシグニチャの直前に、継承しているベースクラスのリストが表示されるようになります。\ :rst:dir:`automodule`\ に対して使用されると、モジュール内でドキュメントが記述されているすべてのクラスのベースクラスが表示されるようになります。

   .. * All autodoc directives support the ``noindex`` flag option that has the
        same effect as for standard :rst:dir:`function` etc. directives: no index
        entries are generated for the documented object (and all autodocumented
        members).

        .. versionadded:: 0.4

   * autodocのすべてのディレクティブは\ ``noindex``\ というフラグオプションをサポートしています。これは標準の\ :rst:dir:`function`\ などと同様の効果があります。ドキュメントが生成されるオブジェクトと、それに含まれるメンバーに対する索引が生成されなくなります。

     .. versionadded:: 0.4

   .. * :rst:dir:`automodule` also recognizes the ``synopsis``, ``platform`` and
        ``deprecated`` options that the standard :rst:dir:`module` directive supports.

   * :rst:dir:`automodule`\ は標準の\ :rst:dir:`module`\ ディレクティブがサポートしている\ ``synopsis``, ``platform``, ``deprecated``\ オプションをサポートしています。

     .. versionadded:: 0.5

   * :dir:`automodule` and :dir:`autoclass` also has an ``member-order`` option
     that can be used to override the global value of
     :confval:`autodoc_member_order` for one directive.

  * :dir:`automodule`\ と\ :dir:`autoclass`\ は\ ``member-order``\ というオプションを持っています。これを設定すると、このディレクティブの中でのみグローバルな\ :confval:`autodoc_member_order`\ という設定をオーバーライドすることができます。

     .. versionadded:: 0.6

  .. * The directives supporting member documentation also have a
       ``exclude-members`` option that can be used to exclude single member names
       from documentation, if all members are to be documented.

       .. versionadded:: 0.6

      .. note::
  
         In an :rst:dir:`automodule` directive with the ``members`` option set, only
         module members whose ``__module__`` attribute is equal to the module name
         as given to ``automodule`` will be documented.  This is to prevent
         documentation of imported classes or functions.

  * メンバーのドキュメント生成をサポートしているディレクティブは\ ``exclude-members``\ というオプションも持っています。これはすべてのドキュメントを生成する場合に、除外したいメンバーの名前をひとつだけ追加するのに使用します。

    .. versionadded:: 0.6

   .. note::

      ``members``\ オプションが設定されている\ :rst:dir:`automodule`\ ディレクティブの中では、\ ``__module__``\ 属性が\ ``automodule``\ で与えられたモジュール名と等しいメンバーのみのドキュメントが生成されます。これはインポートされたクラスや関数のドキュメントまで生成しないための措置です。



.. rst:directive:: autofunction
                   autodata
                   automethod
                   autoattribute

   .. These work exactly like :rst:dir:`autoclass` etc., but do not offer the options
      used for automatic member documentation.

   これらのディレクティブは\ :rst:dir:`autoclass`\ などと同じように動作しますが、メンバー内のドキュメント生成のオプションはありません。

   .. For module data members and class attributes, documentation can either be put
      into a special-formatted comment *before* the attribute definition, or in a
      docstring *after* the definition.  This means that in the following class
      definition, both attributes can be autodocumented::

      class Foo:
          """Docstring for class Foo."""

          #: Doc comment for attribute Foo.bar.
          bar = 1

          baz = 2
          """Docstring for attribute Foo.baz."""

   モジュールのデータメンバーとクラスの属性は、属性定義の\ **前の**\ 行の特別な書式のコメント、もしくは、定義の\ **後の**\ docstringのドキュメントのどちらかを参照してドキュメントを生成します。そのため、以下のサンプルではどちらの属性もドキュメントが生成されます::

      class Foo:
          """Fooクラスに関するdocstring"""

          #: Foo.bar属性に関するdocコメント
          bar = 1

          baz = 2
          """Foo.baz属性に関するdocstring"""

   ..
      .. versionchanged:: 0.6
         :rst:dir:`autodata` and :rst:dir:`autoattribute` can now extract docstrings.

   .. versionchanged:: 0.6
      :rst:dir:`autodata`\ と\ :rst:dir:`autoattribute`\  がdocstringにも対応しました。

   ..
      .. note::

         If you document decorated functions or methods, keep in mind that autodoc
         retrieves its docstrings by importing the module and inspecting the
         ``__doc__`` attribute of the given function or method.  That means that if
         a decorator replaces the decorated function with another, it must copy the
         original ``__doc__`` to the new function.

         From Python 2.5, :func:`functools.wraps` can be used to create
         well-behaved decorating functions.

   .. note::

      もしもデコレータのついた関数やメソッドのドキュメントを生成する場合には、autodocが、実際にモジュールをインポートして、指定された関数やメソッドの\ ``__doc__``\ 属性を見てドキュメントを生成しているということに注意してください。これは、もしデコレートされた関数が他のものに置き換えられる場合には、元の\ ``__doc__``\ の内容を新しい関数にもコピーしなければ動作しないということを意味しています。

      Python 2.5以降であれば、\ :func:`functools.wraps`\ を使用することで、このあたりまできちんと面倒を見てくれます。


.. There are also new config values that you can set:

autodoc拡張には、新しい設定値がいくつかあります。

.. confval:: autoclass_content

   .. This value selects what content will be inserted into the main body of an
      :rst:dir:`autoclass` directive.  The possible values are:

   この値を指定することで、本体の\ :rst:dir:`autoclass`\ ディレクティブにどの内容を追加するのかを選択することができます。指定可能な値は以下の通りです:

   .. ``"class"``
         Only the class' docstring is inserted.  This is the default.  You can
         still document ``__init__`` as a separate method using :dir:`automethod`
         or the ``members`` option to :dir:`autoclass`.
      ``"both"``
         Both the class' and the ``__init__`` method's docstring are concatenated
         and inserted.
      ``"init"``
         Only the ``__init__`` method's docstring is inserted.

   ``"class"``
      クラスのdocstringだけが挿入されます。これがデフォルトの動作になります。\ :dir:`automethod`\ を使用するか、\ :dir:`autoclass`\ に対して\ ``members``\ オプションを設定することで、\ ``__init__``\ の内容は別のメソッドとしてドキュメント化することができます。
   ``"both"``
      クラスのdocstringと、\ ``__init__``\ メソッドのdocstringの両方が結合されて挿入されます。
   ``"init"``
      ``__init__``\ メソッドのdocstringだけが挿入されます。

   .. versionadded:: 0.3


.. confval:: autodoc_member_order

   .. This value selects if automatically documented members are sorted
      alphabetical (value ``'alphabetical'``), by member type (value
      ``'groupwise'``) or by source order (value ``'bysource'``).  The default is
      alphabetical.

   これの設定を変更することで、ドキュメントのついたメンバーをアルファベット順にソートするか(``'alphabetical'``)、もしくはメンバーのタイプによって(``'groupwise'``)ソートするか、ソースコードの定義順(``'bysource'``)にソートするかを変更することができます。デフォルトはアルファベット順です。

   .. Note that for source order, the module must be a Python module with the
      source code available.

   ソースコードの定義順を指定する場合には、対象のモジュールはPythonモジュールで、ソースコードが利用できるようになっていなければなりません。

   .. versionadded:: 0.6

   ..
      .. versionchanged:: 1.0
      Support for ``'bysource'``.

   .. versionchanged:: 1.0
      ``'bysource'`` がサポートされました。


.. confval:: autodoc_default_flags

   .. This value is a list of autodoc directive flags that should be automatically
      applied to all autodoc directives.  The supported flags are ``'members'``,
      ``'undoc-members'``, ``'inherited-members'`` and ``'show-inheritance'``.

   この値には、すべてのautodocディレクティブに対して、自動で適用したいフラグのリストを設定します。設定できるフラグは、
   ``'members'``, ``'undoc-members'``, ``'inherited-members'``, ``'show-inheritance'`` です。

   .. If you set one of these flags in this config value, you can use a negated
      form, :samp:`'no-{flag}'`, in an autodoc directive, to disable it once.
      For example, if ``autodoc_default_flags`` is set to ``['members',
      'undoc-members']``, and you write a directive like this::

   これらのフラグの一つをこの設定値に設定した場合、否定形の :samp:`'no-{flag}'` をautodocディレクティブの中で指定することで、個別に機能をオフにすることができます。例えば、 ``autodoc_default_flags`` に ``['members', 'undoc-members']`` と指定した場合::

     .. automodule:: foo
        :no-undoc-members:

   .. the directive will be interpreted as if only ``:members:`` was given.

   このように記述すると、 ``:members:`` だけが指定されているという解釈がされます。

   .. versionadded:: 1.0


.. Docstring preprocessing

Docstringのプリプロセス
-----------------------

.. autodoc provides the following additional events:

autodocは以下のイベントを追加で提供します:

.. event:: autodoc-process-docstring (app, what, name, obj, options, lines)

   .. versionadded:: 0.4

   .. Emitted when autodoc has read and processed a docstring.  *lines* is a list
      of strings -- the lines of the processed docstring -- that the event handler
      can modify **in place** to change what Sphinx puts into the output.

   autodocがdocstringを読み込んで処理をするタイミングで呼び出されます。\ *lines*\ は処理されたdocstringが入っている、文字列のリストです。このリストはイベントハンドラの中で変更することができ、この結果を利用します。

   .. :param app: the Sphinx application object
      :param what: the type of the object which the docstring belongs to (one of
         ``"module"``, ``"class"``, ``"exception"``, ``"function"``, ``"method"``,
         ``"attribute"``)
      :param name: the fully qualified name of the object
      :param obj: the object itself
      :param options: the options given to the directive: an object with attributes
         ``inherited_members``, ``undoc_members``, ``show_inheritance`` and
         ``noindex`` that are true if the flag option of same name was given to the
         auto directive
      :param lines: the lines of the docstring, see above

   :param app: Sphinxのアプリケーションオブジェクトです
   :param what: docstringが所属しているオブジェクトのタイプです。\ ``"module"``, ``"class"``, ``"exception"``, ``"function"``, ``"method"``,
      ``"attribute"``\ のどれかになります。
   :param name: 装飾名が完全についているオブジェクトの名前です
   :param obj: オブジェクトそのものです
   :param options: ディレクティブに与えられたオプションです。\ ``inherited_members``, ``undoc_members``, ``show_inheritance``, ``noindex``\ などの属性をもったオブジェクトです。同じ名前のフラグオプションが渡されるとtrueになります。
   :param lines: docstringの行の配列です。上記の説明を参照。


.. event:: autodoc-process-signature (app, what, name, obj, options, signature, return_annotation)

   .. versionadded:: 0.5

   .. Emitted when autodoc has formatted a signature for an object. The event
      handler can return a new tuple ``(signature, return_annotation)`` to change
      what Sphinx puts into the output.

   autodocがオブジェクトのシグニチャをフォーマットしているときに呼び出されます。イベントハンドラは新しいタプル\ ``(signature, return_annotation)``\ を返すことができ、Sphinxはこの出力を使ってドキュメントを生成します。

   .. :param app: the Sphinx application object
      :param what: the type of the object which the docstring belongs to (one of
         ``"module"``, ``"class"``, ``"exception"``, ``"function"``, ``"method"``,
         ``"attribute"``)
      :param name: the fully qualified name of the object
      :param obj: the object itself
      :param options: the options given to the directive: an object with attributes
         ``inherited_members``, ``undoc_members``, ``show_inheritance`` and
         ``noindex`` that are true if the flag option of same name was given to the
         auto directive
      :param signature: function signature, as a string of the form
         ``"(parameter_1, parameter_2)"``, or ``None`` if introspection didn't succeed
         and signature wasn't specified in the directive.
      :param return_annotation: function return annotation as a string of the form
         ``" -> annotation"``, or ``None`` if there is no return annotation

   :param app: Sphinxのアプリケーションオブジェクトです
   :param what: docstringが所属しているオブジェクトのタイプです。\ ``"module"``, ``"class"``, ``"exception"``, ``"function"``, ``"method"``,
      ``"attribute"``\ のどれかになります。
   :param name: 装飾名が完全についているオブジェクトの名前です
   :param obj: オブジェクトそのものです
   :param options: ディレクティブに与えられたオプションです。\ ``inherited_members``, ``undoc_members``, ``show_inheritance``, ``noindex``\ などの属性をもったオブジェクトです。同じ名前のフラグオプションが渡されるとtrueになります。
   :param signature: function signature, as a string of the form
      ``"(parameter_1, parameter_2)"``\ という文字列の形式の関数のシグニチャです。あるいは、内部情報の取得に失敗して、なおかつディレクティブで指定されなかった場合には\ ``None``\ となります。
   :param return_annotation: 返り値が指定されると、\ ``" -> annotation"``\ という形式の文字列になります。もしも指定されていない場合には\ ``None``\ となります。


.. The :mod:`sphinx.ext.autodoc` module provides factory functions for commonly
   needed docstring processing in event :event:`autodoc-process-docstring`:

:mod:`sphinx.ext.autodoc`\ モジュールでは\ :event:`autodoc-process-docstring`\ イベント内でdocstringを処理する上で一般的に必要とされるようなファクトリー関数をいくつか提供しています:


.. function:: cut_lines(pre, post=0, what=None)

   .. Return a listener that removes the first pre and last post lines of every 
      docstring. If what is a sequence of strings, only docstrings of a type in 
      what will be processed.

   全てのdocstringの最初の **pre** 行と、最後の **post** 行を削除するリスナーを返します。 **what** として文字列の配列が渡されると、この **what** に含まれているタイプのdocstringだけが処理されます。

   .. Use like this (e.g. in the setup() function of conf.py):

   この関数は :file:`conf.py` の中の :func:`setup()` などで、以下のように使用します。

   .. code-block:: python

      from sphinx.ext.autodoc import cut_lines
      app.connect('autodoc-process-docstring', cut_lines(4, what=['module']))


.. function:: between(marker, what=None, keepempty=False)

   .. Return a listener that only keeps lines between lines that match the marker regular expression. If no line matches, the resulting docstring would be empty, so no change will be made unless keepempty is true.

   **marker** の正規表現にマッチしている行の間だけを保持するリスナーを返します。もしも一行もマッチしない場合には、docstringが空になる可能性がありますが、 **keepempty** がtrueでない場合には、変更されません。

   .. If what is a sequence of strings, only docstrings of a type in what will be processed.

   もしも **what** として、文字列の配列が渡されると、この **what** に含まれているタイプのdocstringだけが処理されます。

 
.. Skipping members

メンバーのスキップ
------------------

.. autodoc allows the user to define a custom method for determining whether a
   member should be included in the documentation by using the following event:

autodocでは以下のイベントを発行することで、指定されたメンバーをドキュメントに含めるかどうかをユーザが決定できるようになっています:

.. event:: autodoc-skip-member (app, what, name, obj, skip, options)

   .. versionadded:: 0.5

   .. Emitted when autodoc has to decide whether a member should be included in the
      documentation.  The member is excluded if a handler returns ``True``.  It is
      included if the handler returns ``False``.

   autodocがメンバーをドキュメントに含めるかどうかを決定するときに呼ばれます。もしもこのハンドラーが\ ``True``\ を返すとメンバーのドキュメントは外されます。\ ``False``\ を返すと含まれるようになります。

   .. :param app: the Sphinx application object
      :param what: the type of the object which the docstring belongs to (one of
         ``"module"``, ``"class"``, ``"exception"``, ``"function"``, ``"method"``,
         ``"attribute"``)
      :param name: the fully qualified name of the object
      :param obj: the object itself
      :param skip: a boolean indicating if autodoc will skip this member if the user
         handler does not override the decision
      :param options: the options given to the directive: an object with attributes
         ``inherited_members``, ``undoc_members``, ``show_inheritance`` and
         ``noindex`` that are true if the flag option of same name was given to the
         auto directive

   :param app: Sphinxのアプリケーションオブジェクトです
   :param what: docstringが所属しているオブジェクトのタイプです。\ ``"module"``, ``"class"``, ``"exception"``, ``"function"``, ``"method"``,
      ``"attribute"``\ のどれかになります。
   :param name: 装飾名が完全についているオブジェクトの名前です
   :param obj: オブジェクトそのものです
   :param skip: もしもユーザが作為を入れようとしなかった場合に、Sphinxがスキップをするかどうかについて決断した結果です
   :param options: ディレクティブに与えられたオプションです。\ ``inherited_members``, ``undoc_members``, ``show_inheritance``, ``noindex``\ などの属性をもったオブジェクトです。同じ名前のフラグオプションが渡されるとtrueになります。








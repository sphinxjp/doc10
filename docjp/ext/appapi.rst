.. highlight:: rest

.. Extension API
   =============

拡張API
=======

.. currentmodule:: sphinx.application

.. Each Sphinx extension is a Python module with at least a :func:`setup` function.
   This function is called at initialization time with one argument, the
   application object representing the Sphinx process.  This application object has
   the following public API:

それぞれのsphinx拡張は、最低でも :func:`setup` 関数を一つ持っている、Pythonモジュールです。この関数は初期化時に一つの引数を伴って呼び出されます。この引数はapplicationオブジェクトで、Sphinxのプロセスに関する情報を持っています。このapplicationオブジェクトは、以下のような公開APIを持っています:

.. method:: Sphinx.setup_extension(name)

   .. Load the extension given by the module *name*.  Use this if your extension
      needs the features provided by another extension.

   *name* に与えられた名前を持っている拡張機能をロードします。もしも、作成中の拡張機能が、他の拡張の機能を利用している場合に、このメソッドを使用してください。


.. method:: Sphinx.add_builder(builder)

   .. Register a new builder.  *builder* must be a class that inherits from
      :class:`~sphinx.builders.Builder`.

   新しいビルダーを登録します。 *builder* 引数は :class:`~sphinx.builders.Builder` クラスを継承してクラスでなければなりません。


.. method:: Sphinx.add_config_value(name, default, rebuild)

   .. Register a configuration value.  This is necessary for Sphinx to recognize
      new values and set default values accordingly.  The *name* should be prefixed
      with the extension name, to avoid clashes.  The *default* value can be any
      Python object.  The string value *rebuild* must be one of those values:

   新しい設定値を登録します。Sphinxが新しい設定値を認識して、関連するデフォルト値を設定するのに必要になります。名前の衝突を回避するために、 *name* には必ず、拡張機能名を最初に入れてください。 *default* 値には、Pythonであれば自由に設定することが可能です。 *rebuild* の値は文字列で、以下の値のうちの一つを取ります。

   .. * ``'env'`` if a change in the setting only takes effect when a document is
        parsed -- this means that the whole environment must be rebuilt.
      * ``'html'`` if a change in the setting needs a full rebuild of HTML
        documents.
      * ``''`` if a change in the setting will not need any special rebuild.

   * ``'env'`` 設定を変更してからビルドをかけると、環境全体が再ビルドされます。
   * ``'html'`` この設定を変更してからビルドをかけた場合、出力がHTMLの時にフル再ビルドされます。
   * ``''`` 設定を変更してもなにも再ビルドに関しては影響を与えません。

   .. .. versionchanged:: 0.4
         If the *default* value is a callable, it will be called with the config
         object as its argument in order to get the default value.  This can be
         used to implement config values whose default depends on other values.

   .. versionchanged:: 0.4
      もしも *default* の値が呼び出し可能オブジェクトの場合には、設定オブジェクトを引数に渡して呼び出しを行い、デフォルト値を取得します。これは、他の値に依存してデフォルト値を変更したい場合に使用することができます。

   .. .. versionchanged:: 0.6
         Changed *rebuild* from a simple boolean (equivalent to ``''`` or
         ``'env'``) to a string.  However, booleans are still accepted and
         converted internally.

   .. versionchanged:: 0.6
      *rebuild* が単純なブーリアン型(``''``, ``'env'`` に相当)から文字列に変更されました。後方互換性のために、ブーリアン型も受け取ることが可能で、その場合には内部で変換されます。


.. method:: Sphinx.add_domain(domain)

   .. Make the given *domain* (which must be a class; more precisely, a subclass of
      :class:`~sphinx.domains.Domain`) known to Sphinx.

   与えられた *domain*(クラスです。おそらく :class:`~sphinx.domains.Domain` のサブクラスになるでしょう)をSphinxに知らせます。

   .. versionadded:: 1.0


.. method:: Sphinx.override_domain(domain)

   .. Make the given *domain* class known to Sphinx, assuming that there is already
      a domain with its ``.name``.  The new domain must be a subclass of the
      existing one.

   与えられた *domain* クラスをSphinxに知らせますが、指定されたクラスの ``.name`` 属性がすでに登録されている場合に使用します。新しい *domain* クラスは、既存のクラスのサブクラスでなければなりません。

   .. versionadded:: 1.0


.. method:: Sphinx.add_index_to_domain(domain, index)

   .. Add a custom *index* class to the domain named *domain*.  *index* must be a
      subclass of :class:`~sphinx.domains.Index`.

   カスタムの *index* クラスを、 *domain* で指定されたドメイン名に追加します。 *index* は :class:`~sphinx.domains.Index` のサブクラスでなければなりません。

   .. versionadded:: 1.0


.. method:: Sphinx.add_event(name)

   .. Register an event called *name*.  This is needed to be able to emit it.

   *name* で指定された名前を持つイベントを登録します。イベントを発行するためには、登録しなければなりません。


.. method:: Sphinx.add_node(node, **kwds)

   .. Register a Docutils node class.  This is necessary for Docutils internals.
      It may also be used in the future to validate nodes in the parsed documents.

   Docutilsのノードクラスを登録します。これはDocutils内部で使用するために必要です。将来的にはパースされたドキュメントにおける、ノード検証に使用されるかもしれません。

   .. Node visitor functions for the Sphinx HTML, LaTeX, text and manpage writers
      can be given as keyword arguments: the keyword must be one or more of
      ``'html'``, ``'latex'``, ``'text'``, ``'man'``, the value a 2-tuple of
      ``(visit, depart)`` methods.  ``depart`` can be ``None`` if the ``visit``
      function raises :exc:`docutils.nodes.SkipNode`.  Example:

   キーワード引数を使用することで、SphinxのHTMLや、LaTeX、テキスト、manページなど、出力形式ごとにノードのビジター関数を与えることができます。キーワードは ``'html'``, ``'latex'``, ``'text'``, ``'man'`` のうちの一つ以上で、値としては、ノードに入ったときと出力したときのメソッドをそれぞれ１つずつ含む２要素のタプルを指定します。 ``depart`` には、 ``None`` を指定可能ですが、この場合は、 ``visit`` 関数は :exc:`docutils.nodes.SkipNode` 例外を発生させます:

   .. code-block:: python

      class math(docutils.nodes.Element): pass

      def visit_math_html(self, node):
          self.body.append(self.starttag(node, 'math'))
      def depart_math_html(self, node):
          self.body.append('</math>')

      app.add_node(math, html=(visit_math_html, depart_math_html))
   
   .. Obviously, translators for which you don't specify visitor methods will choke
      on the node when encountered in a document to translate.

   もちろん、ビジターメソッドを定義しないトランスレータで実行していて、変換すべきドキュメントに遭遇するとビジターメソッドは沈黙します。

   .. .. versionchanged:: 0.5
         Added the support for keyword arguments giving visit functions.

   .. versionchanged:: 0.5
      ビジター関数を、キーワード引数を使って渡すことができるようになりました。


.. method:: Sphinx.add_directive(name, func, content, arguments, **options)
            Sphinx.add_directive(name, directiveclass)

   .. Register a Docutils directive.  *name* must be the prospective directive
      name.  There are two possible ways to write a directive:

   Docutilsのディレクティブを登録します。 *name* は、ディレクティブ名として今後使っていく名前を設定します。ディレクティブを書く方法には、以下の２通りあります:

   .. * In the docutils 0.4 style, *obj* is the directive function.  *content*,
        *arguments* and *options* are set as attributes on the function and
        determine whether the directive has content, arguments and options,
        respectively.  **This style is deprecated.**

   * docutils 0.4スタイル: *obj* がディレクティブ関数で、 *content*, *arguments, *options* は関数の属性として設定されます。そして、ディレクティブがコンテンツや引数、オプションを持っているか、それぞれ決定されます。 **このスタイルは古いです。**

   .. * In the docutils 0.5 style, *directiveclass* is the directive class.  It
        must already have attributes named *has_content*, *required_arguments*,
        *optional_arguments*, *final_argument_whitespace* and *option_spec* that
        correspond to the options for the function way.  See `the Docutils docs
        <http://docutils.sourceforge.net/docs/howto/rst-directives.html>`_ for
        details.

        The directive class normally must inherit from the class
        ``docutils.parsers.rst.Directive``.  When writing a directive for usage in
        a Sphinx extension, you inherit from ``sphinx.util.compat.Directive``
        instead which does the right thing even on docutils 0.4 (which doesn't
        support directive classes otherwise).

   * docutils 0.5スタイル: *has_content*, *required_arguments*, *optional_arguments*, *final_argument_whitespace*, *option_spec* という、必要な属性を初めから持った、 **directiveclass** という、ディレクティブのためのクラスで定義します。これらの属性は、関数で登録する方法と同じ役割を持っています。詳しくは、 `Docutilsのドキュメント <http://docutils.sourceforge.net/docs/howto/rst-directives.html>`_ をご覧ください。

     ディレクティブクラスは通常、\ ``docutils.parsers.rst.Directive``\ クラスを継承しなければなりません。Sphinxの拡張機能を作成するために、ディレクティブを書く場合は、\ ``sphinx.util.compat.Directive``\ クラスを継承してください。こちらのクラスであれば、ディレクティブクラスをサポートしていない、Docutils 0.4でも正しく動作します。

   .. For example, the (already existing) :rst:dir:`literalinclude` directive would be
      added like this:

   例えば、 :rst:dir:`literalinclude` というディレクティブを追加する場合には(既に存在していますが)、以下のように書きます:

   .. code-block:: python

      from docutils.parsers.rst import directives
      add_directive('literalinclude', literalinclude_directive,
                    content = 0, arguments = (1, 0, 0),
                    linenos = directives.flag,
                    language = direcitves.unchanged,
                    encoding = directives.encoding)

   .. .. versionchanged:: 0.6
         Docutils 0.5-style directive classes are now supported.

   .. versionchanged:: 0.6
      Docutils 0.5スタイルのディレクティブクラスがサポートされました。


.. method:: Sphinx.add_directive_to_domain(domain, name, func, content, arguments, **options)
            Sphinx.add_directive_to_domain(domain, name, directiveclass)

   .. Like :meth:`add_directive`, but the directive is added to the domain named
      *domain*.

   :meth:`add_directive` と似ていますが、ディレクティブを、 *domain* で指定されたドメインにのみ追加します。

   .. versionadded:: 1.0


.. method:: Sphinx.add_role(name, role)

   .. Register a Docutils role.  *name* must be the role name that occurs in the
      source, *role* the role function (see the `Docutils documentation
      <http://docutils.sourceforge.net/docs/howto/rst-roles.html>`_ on details).

   Docutilsのロールを登録します。 *name* はドキュメントのソースに表示されるロール名でなければなりません。 *role* はロールの関数を指定します。詳しくは `Docutilsのドキュメント
   <http://docutils.sourceforge.net/docs/howto/rst-roles.html>`_ を参照してください。


.. method:: Sphinx.add_role_to_domain(domain, name, role)

   .. Like :meth:`add_role`, but the role is added to the domain named *domain*.

   :meth:`add_role` に似ていますが、 *domain* で指定されたドメインに、新しいロールを追加します。

   .. versionadded:: 1.0


.. method:: Sphinx.add_generic_role(name, nodeclass)

   Docutilsのロールを登録します。このロールは特に何もしませんが、与えられた *nodeclass* を使ってラップされるようになります。

   .. versionadded:: 0.6

.. Register a Docutils role that does nothing but wrap its contents in the
   node given by *nodeclass*.

.. method:: Sphinx.add_object_type(directivename, rolename, indextemplate='', parse_node=None, ref_nodeclass=None, objname='')

   .. This method is a very convenient way to add a new :term:`object` type that
      can be cross-referenced.  It will do this:
 
   このメソッドは、クロスリファレンスを作成することができる、新しい情報のタイプを追加することができる便利なメソッドです。このメソッドは以下のことを行います:

   .. * Create a new directive (called *directivename*) for documenting an object.
        It will automatically add index entries if *indextemplate* is nonempty; if
        given, it must contain exactly one instance of ``%s``.  See the example
        below for how the template will be interpreted.
      * Create a new role (called *rolename*) to cross-reference to these
        object descriptions.
      * If you provide *parse_node*, it must be a function that takes a string and
        a docutils node, and it must populate the node with children parsed from
        the string.  It must then return the name of the item to be used in
        cross-referencing and index entries.  See the :file:`conf.py` file in the
        source for this documentation for an example.
      * The *objname* (if not given, will default to *directivename*) names the
        type of object.  It is used when listing objects, e.g. in search results.

   * 新しいオブジェクトのための、 *directivename* で指定された名前を持つ、新しいディレクティブを作成します。もしも *indextemplate* が空でなければ、自動的に索引のエントリーに追加されます。指定されるばあいには、 ``%s`` が一つだけ含まれていなければなりません。このテンプレートがどのように解釈されるかについては、この後のサンプルを参照してください。
   * *rolename* で指定された名前を持つ、新しいロールが作成されます。これを使用すると、これらのオブジェクトの説明に対して、クロスリファレンスを張ることができるようになります。
   * *parse_node* を指定する場合には、文字列と、docutilsのノードを受け取る関数を指定しなければなりません。ノードは、その文字列をパースして得られた子供のノードを受け取ります。この関数はクロスリファレンスと索引のエントリーで使用される名前を返さなければなりません。ここの説明のサンプルを見たい場合には、Sphinxのソースコードの :file:`conf.py` を参照してください。
   * *objname*(もし与えられなければ、デフォルトでは *directivename* と同値になります)は、オブジェクトのタイプ名の名前を付けます。これは、検索結果など、オブジェクトを一覧表示する場合に使用されます。

   .. For example, if you have this call in a custom Sphinx extension:

   以下のような関数呼び出しが、カスタムのSphinx拡張の中で行われたとすると:

   .. code-block:: python

      app.add_object_type('directive', 'dir', 'pair: %s; directive')

   .. you can use this markup in your documents:

   ドキュメント内で次のようなマークアップが使用できるようになります:

   ..
      .. rst:directive:: function

         Document a function.

      <...>

      See also the :rst:dir:`function` directive.

   .. code-block:: rst

      .. rst:directive:: function

         functionの説明。

      <...>

      :rst:dir:`function` ディレクティブも参照してください

   .. For the directive, an index entry will be generated as if you had prepended:

   また、このディレクティブを使用すると、以下のようにindexディレクティブを書いたのと同じ索引が作成されます:

   .. code-block:: rst

      .. index:: pair: function; directive

   .. The reference node will be of class ``literal`` (so it will be rendered in a
      proportional font, as appropriate for code) unless you give the *ref_nodeclass*
      argument, which must be a docutils node class (most useful are
      ``docutils.nodes.emphasis`` or ``docutils.nodes.strong`` -- you can also use
      ``docutils.nodes.generated`` if you want no further text decoration).

   リファレンスノードのクラスは、 **参照ノードクラス** を指定しない場合には ``literal`` になります。このクラスはコードの記述に適したプロポーショナルフォントでレンダリングされます。クラスは、docutilsのノードクラスを設定する必要があります。docutilsのクラスの中で頻繁に使用されるのは ``docutils.nodes.emphasis`` あるいは ``docutils.nodes.strong`` です。もしも装飾が不要であれば、 ``docutils.nodes.generated`` を使用することもできます。

   .. For the role content, you have the same syntactical possibilities as for
      standard Sphinx roles (see :ref:`xref-syntax`).

   ロールの中身に関しては、標準のSphinxのロールと同じ構文を使用することができます(:ref:`xref-syntax` 参照)。

   .. This method is also available under the deprecated alias
      :meth:`add_description_unit`.

   このメソッドは旧名の　:meth:`add_description_unit` という名前でも呼び出すことができます。


.. method:: Sphinx.add_crossref_type(directivename, rolename, indextemplate='', ref_nodeclass=None, objname='')

   .. This method is very similar to :meth:`add_description_unit` except that the
      directive it generates must be empty, and will produce no output.

   このメソッドは ディレクティブの出力が必ず空になることを除けば、 :meth:`add_object_type` と非常に良く似ています。

   .. That means that you can add semantic targets to your sources, and refer to
      them using custom roles instead of generic ones (like :rst:role:`ref`).  Example
      call:

   これは、セマンティックのターゲットをソースに追加して、カスタムのロールを使用して参照することができるということを意味しています。ただし、 :rst:role:`ref` のような一般的なものは使用することができません。

   サンプル::

      app.add_crossref_type('topic', 'topic', 'single: %s', docutils.nodes.emphasis)

   .. Example usage:

         .. topic:: application API

         The application API
         -------------------

         <...>

         See also :topic:`this section <application API>`.

   使用例::

      .. topic:: application API

      アプリケーション API
      -------------------

      <...>

      :topic:`このセクション <application API>` を参照してください。

   .. (Of course, the element following the ``topic`` directive needn't be a
      section.)

   もちろん、 ``topic`` ディレクティブに続く要素はセクションでなくてもかまいません。


.. method:: Sphinx.add_transform(transform)

   標準のDocutilsの :class:`Transform` のサブクラスの *transform* をtransformのリストに追加します。これはSphinxがreST形式のドキュメントをパースした後に適用されます。

.. Add the standard docutils :class:`Transform` subclass *transform* to the list
   of transforms that are applied after Sphinx parses a reST document.


.. method:: Sphinx.add_javascript(filename)

   .. Add *filename* to the list of JavaScript files that the default HTML template
      will include.  The filename must be relative to the HTML static path, see
      :confval:`the docs for the config value <html_static_path>`.

   JavaScriptのファイルのリストに、指定された *filename* のファイルを追加します。ここで指定されたファイルは、デフォルトのHTMLテンプレートの中にインクルードされます。ファイル名はHTMLの静的パスへの相対パスでなければなりません。詳しくは :confval:`設定値のドキュメント <html_static_path>` を参照してください。

   .. versionadded:: 0.5


.. method:: Sphinx.add_stylesheet(filename)

   .. Add *filename* to the list of CSS files that the default HTML template will
      include.  Like for :meth:`add_javascript`, the filename must be relative to
      the HTML static path.

   CSSのファイルのリストに、指定された *filename* のファイルを追加します。ここで指定されたファイルは、デフォルトのHTMLテンプレートの中にインクルードされます。 :meth:`add_javascript` と同様に、ファイル名はHTMLの静的パスへの相対パスでなければなりません。

   .. versionadded:: 1.0


.. method:: Sphinx.add_lexer(alias, lexer)

   .. Use *lexer*, which must be an instance of a Pygments lexer class, to
      highlight code blocks with the given language *alias*.

   *alias* で指定された言語で書かれたコードブロックのハイライトを行う、Pygmentsのレキサークラスのインスタンス *lexer* を設定します。

   .. versionadded:: 0.6


.. method:: Sphinx.add_autodocumenter(cls)

   .. Add *cls* as a new documenter class for the :mod:`sphinx.ext.autodoc`
      extension.  It must be a subclass of :class:`sphinx.ext.autodoc.Documenter`.
      This allows to auto-document new types of objects.  See the source of the
      autodoc module for examples on how to subclass :class:`Documenter`.

   :mod:`sphinx.ext.autodoc` 拡張のための新しいドキュメンタークラスとして、 *cls* クラスを追加します。この引数は :class:`sphinx.ext.autodoc.Documenter` のサブクラスでなければなりません。これによって、新しいタイプのオブジェクトの自動ドキュメントが可能になります。どのように :class:`Documenter` のサブクラスを作ればいいのか、というサンプルを参照したい場合には、autodocモジュールのソースコードを参照してください。

   .. versionadded:: 0.6


.. method:: Sphinx.add_autodoc_attrgetter(type, getter)

   .. Add *getter*, which must be a function with an interface compatible to the
      :func:`getattr` builtin, as the autodoc attribute getter for objects that are
      instances of *type*.  All cases where autodoc needs to get an attribute of a
      type are then handled by this function instead of :func:`getattr`.

   組み込みの :func:`getattr` 関数と互換性のあるインタフェースを持つ、 **getter** 関数を追加します。これは **type** 型のインスタンスのオブジェクトから、自動的に属性を取得してドキュメントを作成するのに使用されます。autodocが型の属性を取得する必要がある場面では、標準の :func:`getattr` 関数の代わりに、ここで指定された関数が呼ばれます。

   .. versionadded:: 0.6


.. method:: Sphinx.connect(event, callback)

   .. Register *callback* to be called when *event* is emitted.  For details on
      available core events and the arguments of callback functions, please see
      :ref:`events`.

   **event** が発行されたときに呼ばれる、 **callback** を登録します。利用可能なコアイベントと、コールバック関数の引数の詳細情報に関しては :ref:`events` を参照してください。

   .. The method returns a "listener ID" that can be used as an argument to
      :meth:`disconnect`.

   このメソッドは "リスナーID" を返します。これは :meth:`disconnect` を呼んで削除する場合の引き数に使用します。


.. method:: Sphinx.disconnect(listener_id)

   .. Unregister callback *listener_id*.

   **listener_id** で指定されたコールバックの登録を解除します。


.. method:: Sphinx.emit(event, *arguments)

   .. Emit *event* and pass *arguments* to the callback functions.  Return the
      return values of all callbacks as a list.  Do not emit core Sphinx events
      in extensions!

  **event** を発行します。コールバック関数には **arguments** が渡されます。返り値は、すべてのコールバックの返り値がリストに格納されて返されます。拡張機能の中からは、Sphinxのコアのイベントを発行しないでください。


.. method:: Sphinx.emit_firstresult(event, *arguments)

   .. Emit *event* and pass *arguments* to the callback functions.  Return the
      result of the first callback that doesn't return ``None``.

   **event** を発行します。コールバック関数には **arguments** が渡されます。最初に ``None`` 以外を返したコールバックの返り値を返します。

   .. versionadded:: 0.5


.. method:: Sphinx.require_sphinx(version)

   *version* (``'1.1'`` のような、 ``メジャー.マイナー`` 形式のバージョン文字列)と、実行しているSphinxのバージョンを比較して、古すぎる場合にはビルドを中断します。

   .. versionadded:: 1.0

.. Compare *version* (which must be a ``major.minor`` version string,
   e.g. ``'1.1'``) with the version of the running Sphinx, and abort the build
   when it is too old.

   .. versionadded:: 1.0

.. exception:: ExtensionError

   ここで説明したすべての関数は、もし拡張APIの中で何か想定外のことが発生した時には、この例外を投げます。

.. All these functions raise this exception if something went wrong with the
   extension API.

.. Examples of using the Sphinx extension API can be seen in the 
   :mod:`sphinx.ext` package.

Sphinx拡張APIの使用法に関するサンプルは、Sphinx標準の :mod:`sphinx.ext` のパッケージの中を見てください。

.. Sphinx core events
   ------------------

.. _events:

Sphinxコアイベント
------------------

.. These events are known to the core.  The arguments shown are given to the
   registered event handlers.

これから説明するイベントがコアイベントです。ここで示した引数は、登録されたイベントハンドラに渡されます。

.. event:: builder-inited (app)

   ビルダーオブジェクトが作成された時に発行されます。ビルダーオブジェクトは ``app.builder`` とすることで参照できます。

.. Emitted when the builder object has been created.  It is available as
   ``app.builder``.

.. event:: env-purge-doc (app, env, docname)

   ソースファイルが削除されたり、新たに読み込まる場合など、環境の中に含まれるソースファイルの関連情報をクリアすべき状況になった場合に発行されます。環境の属性の中に情報をキャッシュしておくような拡張機能ためのイベントです。

   例えば、環境の中にすべてのモジュールのキャッシュが存在してる場合、ソースファイルが変更されると、ファイルからモジュール宣言から削除されてから、そのファイルに関するキャッシュのエントリーはクリアされます。

   .. versionadded:: 0.5

.. Emitted when all traces of a source file should be cleaned from the
   environment, that is, if the source file is removed or before it is freshly
   read.  This is for extensions that keep their own caches in attributes of the
   environment.

   For example, there is a cache of all modules on the environment.  When a
   source file has been changed, the cache's entries for the file are cleared,
   since the module declarations could have been removed from the file.

.. event:: source-read (app, docname, source)

   ソースファイルが読み込まれる時に発行されます。 **source** 引数はリストで、ひとつの要素はソースファイルのコンテンツを表します。コンテンツに関する処理を行ったり、要素に関してソースレベルでの変換を実装したりすることができます。

   もしも、LaTeXと同じように、 ``$`` 記号を、インラインの数式の区切り文字にしたい場合には、このイベントハンドラの中で、正規表現を使用して ``$...$`` を ``:math:`...``` に置き換えることで実現することができます。

   .. versionadded:: 0.5

.. Emitted when a source file has been read.  The *source* argument is a list
   whose single element is the contents of the source file.  You can process the
   contents and replace this item to implement source-level transformations.

   For example, if you want to use ``$`` signs to delimit inline math, like in
   LaTeX, you can use a regular expression to replace ``$...$`` by
   ``:math:`...```.

   .. versionadded:: 0.5

.. event:: doctree-read (app, doctree)

   doctreeがパースされ、環境から読み込まれ、pickle化される時に発行されます。 **doctree** をその場で変更することができます。

.. Emitted when a doctree has been parsed and read by the environment, and is
   about to be pickled.  The *doctree* can be modified in-place.

.. event:: missing-reference (app, env, node, contnode)

   Pythonモジュールやオブジェクトへの相互参照が解決できないときに発行されます。もしも参照の問題を解決できる場合には、 **node** の代わりにドキュメントツリーに挿入される、新しいdocutilsのノードを返すことで、イベントハンドラ側で解決を行うことができます。通常このノードは、 **contnode** を子供として含む :class:`reference` ノードです。

   :param env: ビルド環境(``app.builder.env``)
   :param node: 未解決の、解決すべき :class:`pending_xref` ノードです。このノードは、参照を解決するために、 ``reftype``, ``reftarget``, ``modname``, ``classname`` といった、型とターゲットに関する情報を属性として持ちます。
   :param contnode: このノードは、将来の参照が持つ、テキストとフォーマット情報を持ちます。これは返される参照ノードの子供にならなければなりません。

.. Emitted when a cross-reference to a Python module or object cannot be
   resolved.  If the event handler can resolve the reference, it should return a
   new docutils node to be inserted in the document tree in place of the node
   *node*.  Usually this node is a :class:`reference` node containing *contnode*
   as a child.

   :param env: The build environment (``app.builder.env``).
   :param node: The :class:`pending_xref` node to be resolved.  Its attributes
      ``reftype``, ``reftarget``, ``modname`` and ``classname`` attributes
      determine the type and target of the reference.
   :param contnode: The node that carries the text and formatting inside the
      future reference and should be a child of the returned reference node.

.. event:: doctree-resolved (app, doctree, docname)

   環境がdoctreeに関して"resolved(解決)"と判断したときに発行されます。これは、すべての参照が解決され、目次が挿入された時、ということになります。 **doctree** はこのイベントハンドラないで操作することができます。

   このイベントは、ライタークラスにビジターメソッドが存在しない、カスタムのノードを置換して処理するのに使用することができます。もしもここで設定しない場合、未知のノードを見つけると、ライターはエラーを出しますが、設定することでエラーが出なくなります。

.. Emitted when a doctree has been "resolved" by the environment, that is, all
   references have been resolved and TOCs have been inserted.  The *doctree* can
   be modified in place.

   Here is the place to replace custom nodes that don't have visitor methods in
   the writers, so that they don't cause errors when the writers encounter them.

.. event:: env-updated (app, env)

   ビルダーの :meth:`update` メソッドの実行が完了し、環境とすべてのdoctreeが最新になった時に発行されます。

   .. versionadded:: 0.5

.. Emitted when the :meth:`update` method of the build environment has
   completed, that is, the environment and all doctrees are now up-to-date.

.. event:: html-collect-pages (app)

   .. Emitted when the HTML builder is starting to write non-document pages.  You
      can add pages to write by returning an iterable from this event consisting of
      ``(pagename, context, templatename)``.

   HTMLビルダーが、ドキュメント以外のページの書き込みを開始するときに発行されます。 ``(ページ名, コンテキスト, テンプレート名)`` という構成の要素を含むシーケンスを返すと、ページを追加することができます。

   .. versionadded:: 1.0


.. event:: html-page-context (app, pagename, templatename, context, doctree)

   .. Emitted when the HTML builder has created a context dictionary to render a
      template with -- this can be used to add custom elements to the context.

   HTMLビルダーがコンテキストの辞書を作り、テンプレートを使用してレンダリングを行う時に発行されます。このイベントは、追加のカスタムの要素をコンテキストに追加する場合に使用することができます。

   .. The *pagename* argument is the canonical name of the page being rendered,
      that is, without ``.html`` suffix and using slashes as path separators.  The
      *templatename* is the name of the template to render, this will be
      ``'page.html'`` for all pages from reST documents.

   **pagename** 引数はレンダリングされるページの、規範に則った名前です。規範というのは、 ``.html`` が付かず、パス区切りとしてスラッシュ(/)が使われている状態です。 **templatename** はレンダリングに使用するテンプレートの名前です。 reSTドキュメントのページのレンダリング時には、必ず ``'page.html'`` となります。

   .. The *context* argument is a dictionary of values that are given to the
      template engine to render the page and can be modified to include custom
      values.  Keys must be strings.

   **context** 引数はテンプレートエンジンがページをレンダリングする際に与えられる値の辞書になります。カスタムの値を持つように、変更することが可能です。キーは必ず文字列です。

   .. The *doctree* argument will be a doctree when the page is created from a reST
      documents; it will be ``None`` when the page is created from an HTML template
      alone.

   **doctree** 引数はreSTドキュメントから作成する場合にはdoctreeとなります。もしもHTMLテンプレートからのみ作成されるページの場合には、 ``None`` となります。

   .. versionadded:: 0.4


.. event:: build-finished (app, exception)

   .. Emitted when a build has finished, before Sphinx exits, usually used for
      cleanup.  This event is emitted even when the build process raised an
      exception, given as the *exception* argument.  The exception is reraised in
      the application after the event handlers have run.  If the build process
      raised no exception, *exception* will be ``None``.  This allows to customize
      cleanup actions depending on the exception status.

   ビルドが完了し、Sphinxが終了する際に発行されます。通常はクリーンアップに使用されます。このイベントは、ビルドプロセスが例外を上げたときにも発行されます。その場合には、 **exception** 引数が渡されます。アプリケーションの中で発生した例外は、このイベントハンドラが終了した段階で、再度投げられます。もしもビルドプロセスが例外を発生しなかった場合には、 **exception** は ``None`` になります。これによって、例外の種類ごとの、クリーンアップの処理をカスタム化できます。

   .. versionadded:: 0.5

.. The template bridge
.. -------------------

.. _template-bridge:

テンプレートブリッジ
--------------------

.. class:: TemplateBridge

   .. This class defines the interface for a “template bridge”, that is, a class that renders 
      templates given a template name and a context.

   このクラスは、"テンプレートへのブリッジ"をっ定義しています。テンプレートブリッジというのは、与えられたテンプレート名と、コンテキストを利用して、テンプレートをレンダリングするクラスのことです。

   .. method:: init(builder, theme=None, dirs=None)

      .. Called by the builder to initialize the template system.

      テンプレートのシステムの初期化を行うために、ビルダーから呼ばれます。

      .. builder is the builder object; you’ll probably want to look at the 
         value of builder.config.templates_path.

      **builder** はビルダーオブジェクトで、 ``builder.config.templates_path`` の値を使用することになるでしょう。

      .. theme is a sphinx.theming.Theme object or None; in the latter case, 
         dirs can be list of fixed directories to look for templates.

      **theme** は :class:`sphinx.theming.Theme` オブジェクト、あるいは ``None`` になります。後者の場合には、 **dirs** に固定ディレクトリのパスが入ったリストが渡され、この中からテンプレートを探します。

   .. method:: newest_template_mtime()

      .. Called by the builder to determine if output files are outdated because of template changes. 
         Return the mtime of the newest template file that was changed. The default implementation returns 0.

      このメソッドはビルダーから呼ばれます。テンプレートが変更されたことで、出力ファイルを再レンダリングする必要があるかどうかの判断をするために使用されます。変更された、最新のテンプレートのmtimeを返します。デフォルトの実装ではゼロを返します。

   .. method:: render(template, context)

      .. Called by the builder to render a template given as a filename with a 
         specified context (a Python dictionary).

      指定された **context** (Python辞書)を使用して、 **template** で指定されたファイル名のテンプレートのレンダリングを行います。ビルダーから呼ばれます。

   .. method:: render_string(template, context)

      .. Called by the builder to render a template given as a string 
         with a specified context (a Python dictionary).

      指定された **context** (Python辞書)を使用して、 **template** で指定された文字列形式のテンプレートのレンダリングを行います。ビルダーから呼ばれます。


.. _domain-api:

.. Domain API
   ----------

ドメインAPI
-----------

.. module:: sphinx.domains

.. class:: Domain

   .. A Domain is meant to be a group of "object" description directives for
      objects of a similar nature, and corresponding roles to create references to
      them.  Examples would be Python modules, classes, functions etc., elements
      of a templating language, Sphinx roles and directives, etc.

   ドメインというのは、似たような特性を持つオブジェクトごとに用意された「オブジェクト」説明ディレクティブと、それらに対応してリファレンスを作成するロールを集めたものです。例えば、Pythonのモジュール、クラス、関数、テンプレート言語であればエレメント、Sphinxであればロールとディレクティブなどです。

   .. Each domain has a separate storage for information about existing objects
      and how to reference them in `self.data`, which must be a dictionary.  It
      also must implement several functions that expose the object information in
      a uniform way to parts of Sphinx that allow the user to reference or search
      for objects in a domain-agnostic way.

   ドメインごとに、既存のオブジェクトの情報や、それらへの参照の仕方などを個別の領域に保存します。保存先は `self.data` で、辞書でなければなりません。また、Sphinxの一部として決まったフォーマットでオブジェクトの情報を公開するための関数や、ユーザが参照できるようにしたり、ドメインごとの方法でオブジェクトを探索したりする関数をいくつか実装する必要があります。

   .. About `self.data`: since all object and cross-referencing information is
      stored on a BuildEnvironment instance, the `domain.data` object is also
      stored in the `env.domaindata` dict under the key `domain.name`.  Before the
      build process starts, every active domain is instantiated and given the
      environment object; the `domaindata` dict must then either be nonexistent or
      a dictionary whose 'version' key is equal to the domain class'
      :attr:`data_version` attribute.  Otherwise, `IOError` is raised and the
      pickled environment is discarded.

   `self.data` に関しては、すべてのオブジェクトとクロスリファレンス情報はBuildEnvironmentインスタンスに保存しておくために、 `domain.data` オブジェクトも、 `domain.name` をキーにして `env.domaindata` 辞書に格納します。ビルドプロセスが始まるまえに、すべてのアクティブなドメインがインスタンス化され、環境オブジェクトが与えられます。 `domaindata` 辞書は、空にしておくか、もしくは'version'というキーがドメインクラスの :attr:`data_version` 属性と同じ値を格納しておく必要があります。そうでない場合には `IOError` が発生し、既存のpickle化された環境が破棄されます。

   .. method:: clear_doc(docname)

      .. Remove traces of a document in the domain-specific inventories.

      ドメインに特化した領域から、指定されたドキュメントの情報を削除します。

   .. method:: directive(name)

      .. Return a directive adapter class that always gives the registered
         directive its full name ('domain:name') as ``self.name``.

      ``self.name`` で指定されたドメイン付きで、完全な名前('ドメイン:名前')で登録されたディレクティブ
      を与える、ディレクティブアダプタークラスを返します。

   .. method:: get_objects()

        .. Return an iterable of "object descriptions", which are tuples with
           five items:

        次のような項目を持つ、「オブジェクトの説明」のタプルを返す、繰り返し可能オブジェクトを返します。

        .. * `name`     -- fully qualified name
           * `type`     -- object type, a key in ``self.object_types``
           * `docname`  -- the document where it is to be found
           * `anchor`   -- the anchor name for the object
           * `priority` -- how "important" the object is (determines placement
             in search results)

             - 1: default priority (placed before full-text matches)
             - 0: object is important (placed before default-priority objects)
             - 2: object is unimportant (placed after full-text matches)
             - -1: object should not show up in search at all

         * `name`     -- 完全な修飾付きの名前
         * `type`     -- オブジェクトの種類。 ``self.object_types`` のキー
         * `docname`  -- そのオブジェクトが発見されたドキュメント名
         * `anchor`   -- そのオブジェクトのアンカー名
         * `priority` -- そのオブジェクトがどれだけ重要か？(検索結果の決定に利用される)

           - 1: デフォルトの優先順位(全文検索マッチの前に置かれる)
           - 0: 重要なオブジェクト(出フィルとの優先順位のオブジェクトの前に置かれる)
           - 2: 重要でないオブジェクト(全文検索マッチの後に置かれる)
           - -1: 検索結果に出すべきではないオブジェクト

   .. method:: resolve_xref(env, fromdocname, builder, typ, target, node, contnode)

      .. Resolve the ``pending_xref`` *node* with the given *typ* and *target*.

      *typ* 型と、 *target* を持つ、 ``pending_xref`` (未解決のクロスリファレンス) *node* の参照先の解決を行います。

      .. This method should return a new node, to replace the xref node,
         containing the *contnode* which is the markup content of the
         cross-reference.

      このメソッドは、xrefノードと置き換えるための、新しいノードを返さなければなりません。また、この新しいノードには、クロスリファレンスのマークアップのコンテンツである、 *contnode* を含めます。

      .. If no resolution can be found, None can be returned; the xref node will
         then given to the 'missing-reference' event, and if that yields no
         resolution, replaced by *contnode*.

      もし、参照先を見つけることができなければ、Noneを返すことができます。xrefノードは'missing-reference'イベントを発行し、それでも解決しなければ、 *contnode* に置き換えられます。

      .. The method can also raise :exc:`sphinx.environment.NoUri` to suppress
         the 'missing-reference' event being emitted.

      また、このメソッド内で :exc:`sphinx.environment.NoUri` 例外を発生させると、'missing-reference'が発行されるのを押さえることができます。

   .. method:: role(name)

      .. Return a role adapter function that always gives the registered
         role its full name ('domain:name') as the first argument.

      登録された完全な名前を持つロール('ドメイン:名前')を最初の引数として与える、ロールアダプター関数を返します。

   .. attribute:: data_version

      .. data version, bump this when the format of `self.data` changes

      データのバージョンです。もしも `self.data` 内のフォーマットを変更したときには、この数字を上げてください。

   .. attribute:: directives

      .. directive name -> directive class

      ディレクティブ名→ディレクティブのクラスとなる辞書です。

   .. attribute:: indices

      .. a list of Index subclasses

      Indexのサブクラスが格納されたリストです。

   .. attribute:: initial_data

      .. data value for a fresh environment

      新しい環境に入れる値です。

   .. attribute:: label

      .. domain label: longer, more descriptive (used in messages)

      ドメインのラベルです。 ``name`` よりも長く、説明的な名前です。メッセージ内で利用されます。

   .. attribute:: name

      .. domain name: should be short, but unique

      ドメイン名です。なるべく短く、重複のない名前にする必要があります。

   .. method:: object_types

      .. type (usually directive) name -> ObjType instance

      型(通常はディレクティブ)名→ObjTypeのインスタンスとなる辞書です。

   .. method:: roles

      .. role name -> role callable

      ロール名→ロールの呼び出し可能オブジェクトとなる辞書です。

.. class:: ObjType

   .. An ObjType is the description for a type of object that a domain can
      document.  In the object_types attribute of Domain subclasses, object type
      names are mapped to instances of this class.

   ObjTypeは、そのドメインでドキュメントを書くことができる、オブジェクトの種類に対する説明ユニットです。Domainのサブクラスの **object_types** の辞書の中に、オブジェクト名と、このクラスのインスタンスのマッピングが保持されます。

   .. Constructor arguments:

   コンストラクタ引数

   .. - *lname*: localized name of the type
      - *roles*: all the roles that can refer to an object of this type
      - *attrs*: object attributes -- currently only "searchprio" is known,
        which defines the object's priority in the full-text search index,
        see :meth:`Domain.get_objects()`.

   - *lname*: ローカライズされた型名
   - *roles*: この型を参照することができる、すべてのロール
   - *attrs*: オブジェクトの属性。現在では、全文検索インデックス内での、オブジェクトの優先順位(:meth:`Domain.get_objects()` 参照)のみが定義されています。


.. class:: Index

   .. An Index is the description for a domain-specific index.  To add an index to
      a domain, subclass Index, overriding the three name attributes:

   Indexは、ドメインに特化した索引のための説明を行うクラスです。ドメインに対する索引を追加する場合には、Indexのサブクラスを作り、3つの名前属性をオーバーライドします:

   .. * `name` is an identifier used for generating file names.
      * `localname` is the section title for the index.
      * `shortname` is a short name for the index, for use in the relation bar in
        HTML output.  Can be empty to disable entries in the relation bar.

   * `name` はファイル名を生成する際に使用される、識別子です。
   * `localname` は索引のセクションタイトルです。
   * `shortname` は索引に対する短い名前です。これは、HTML出力のリレーションバーで使用されます。もしも空であれば、リレーションバーのエントリーは無効化されます。

   .. and providing a :meth:`generate()` method.  Then, add the index class to
      your domain's `indices` list.  Extensions can add indices to existing
      domains using :meth:`~sphinx.application.Sphinx.add_index_to_domain()`.

   次に、 :meth:`generate()` メソッドを提供するようにします。最後に、自分の作ったドメインのDomainクラスが持つ、 `indices` リストに追加します。拡張機能の中で :meth:`~sphinx.application.Sphinx.add_index_to_domain()` メソッドを呼ぶと、既存のドメインに対して、索引を追加することもできます。

   .. method:: generate(docnames=None)

      .. Return entries for the index given by *name*.  If *docnames* is given,
         restrict to entries referring to these docnames.

      *name* が与えられた索引に対する索引のエントリーを返します。もしも *docnames* が与えられた場合には、これらのdocnameに関連する要素だけを返します。

      .. The return value is a tuple of ``(content, collapse)``, where *collapse*
         is a boolean that determines if sub-entries should start collapsed (for
         output formats that support collapsing sub-entries).

      返り値は ``(content, collapse)`` というタプルです。 *collapse* はブーリアン型で、サブエントリーが折りたたまれて始まるべきかどうかを決定します。(出力フォーマットが折りたたまれたサブエントリーをサポートしている場合)。

      .. *content* is a sequence of ``(letter, entries)`` tuples, where *letter*
         is the "heading" for the given *entries*, usually the starting letter.

      *content* は ``(etter, entries)`` というタプルです。 *letter* は与えられた *entries* の見出しで、通常は初めの文字を表します。

      .. *entries* is a sequence of single entries, where a single entry is a
         sequence ``[name, subtype, docname, anchor, extra, qualifier, descr]``.
         The items in this sequence have the following meaning:

      *entries* は単独のエントリーのシーケンスで、それぞれのエントリーは、 ``[name, subtype, docname, anchor, extra, qualifier, descr]`` という要素で構成されます。このシーケンスの要素はそれぞれ次のような意味を持っています。

      .. - `name` -- the name of the index entry to be displayed
         - `subtype` -- sub-entry related type:
           0 -- normal entry
           1 -- entry with sub-entries
           2 -- sub-entry
         - `docname` -- docname where the entry is located
         - `anchor` -- anchor for the entry within `docname`
         - `extra` -- extra info for the entry
         - `qualifier` -- qualifier for the description
         - `descr` -- description for the entry

      - `name` -- 索引のエントリーの、表示される名前
      - `subtype` -- サブエントリーの種類
           0 -- 通常のエントリー
           1 -- サブエントリー付きのエントリーentry with sub-entries
           2 -- サブエントリー
         - `docname` -- エントリーが置かれているドキュメント名
         - `anchor` -- `docname` 内の、エントリーへのアンカー
         - `extra` -- エントリーに関する追加情報extra info for the entry
         - `qualifier` -- 説明の修飾子qualifier for the description
         - `descr` -- エントリーの説明

      .. Qualifier and description are not rendered e.g. in LaTeX output.

      修飾子と説明はLaTeX出力などではレンダリングされません。

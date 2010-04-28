.. _exttut:

チュートリアル: シンプルな拡張を作成
====================================

.. Tutorial: Writing a simple extension
   ====================================

.. This section is intended as a walkthrough for the creation of custom extensions.
   It covers the basics of writing and activating an extensions, as well as
   commonly used features of extensions.

このセクションではカスタムの拡張の作成について一通り説明していきたいと思います。
ここの説明でカバーするのは、拡張の基本的な書き方と登録の仕方、あとは拡張を作成するのに使用される一般的な機能などです。

.. As an example, we will cover a "todo" extension that adds capabilities to
   include todo entries in the documentation, and collecting these in a central
   place.  (A similar "todo" extension is distributed with Sphinx.)

サンプルとしては、ドキュメントの中にToDoを書くことができるようになり、指定された場所にすべてのToDoの一覧を出力する、"todo"拡張を扱おうと思います。Sphinxの配布物に含まれる"todo"拡張とほぼ同じものになります。

.. Build Phases

ビルド・フェーズ
----------------

.. One thing that is vital in order to understand extension mechanisms is the way
   in which a Sphinx project is built: this works in several phases.

Sphinxのプロジェクトがビルドされる過程で、拡張機能がどのように実行されるのかということを理解することは、拡張機能の開発をするうえで必要不可欠です。この作業は以下のいくつかのフェーズから構成されています。

.. **Phase 0: Initialization**

   In this phase, almost nothing interesting for us happens.  The source
   directory is searched for source files, and extensions are initialized.
   Should a stored build environment exist, it is loaded, otherwise a new one is
   created.

**フェーズ 0: 初期化**

   このフェーズでは拡張作成者にとって面白いものは何もありません。
   ソースディレクトリ内のソースファイルを探索し、拡張機能を初期化します。
   保存されたビルド環境があればそれをロードし、なければ新しいビルド環境を作成します。

.. **Phase 1: Reading**

   In Phase 1, all source files (and on subsequent builds, those that are new or
   changed) are read and parsed.  This is the phase where directives and roles
   are encountered by the docutils, and the corresponding functions are called.
   The output of this phase is a *doctree* for each source files, that is a tree
   of docutils nodes.  For document elements that aren't fully known until all
   existing files are read, temporary nodes are created.

   During reading, the build environment is updated with all meta- and cross
   reference data of the read documents, such as labels, the names of headings,
   described Python objects and index entries.  This will later be used to
   replace the temporary nodes.

   The parsed doctrees are stored on the disk, because it is not possible to
   hold all of them in memory.

**フェーズ 1: 読み込み**

   フェーズ 1ではすべてのソースファイルが読み込まれ、パースされます。なお、この後のフェーズは新規のファイルか変更されたファイルに対して実行されます。このフェーズではdocutilsによってディレクティブやロールが処理され、それに対応する関数が呼ばれます。このフェーズの出力は、ソースファイルごとの\ **DOCツリー**\ です。これは、docutilsのノードがツリー上に構成されているものです。すべてのファイルを読み込むまでは完全に解釈できないドキュメントの要素に関しては、一時的なノードが作られます。

   ソースを読み込んでいる間は、ラベルや見出し命、説明されているPythonオブジェクト、索引のエントリーなどのめたな情報やクロスファンレスの情報がビルド環境に出力されます。これらの情報は、後で一時的なノードと置き換えられます。

   パースされたDOCツリーはすべてのメモリ上で保存しておくことができないため、ディスク上に保存されます。

.. **Phase 2: Consistency checks**

   Some checking is done to ensure no surprises in the built documents.


**フェーズ 2: 一貫性チェック**

   ビルドされたドキュメントの中に、びっくりするようなものがないか、いくつかのチェックを行います。

.. **Phase 3: Resolving**

.. Now that the metadata and cross-reference data of all existing documents is
   known, all temporary nodes are replaced by nodes that can be converted into
   output.  For example, links are created for object references that exist, and
   simple literal nodes are created for those that don't.

**フェーズ 3: 解決**

   読み込まれたすべてのドキュメントから収集されたメタデータ、およびクロスリファレンスのデータを使って、一時的なノードを、出力可能なノードに置き換えていきます。例えば、存在するオブジェクトへの参照があればリンクが作成されます。リンク先が存在しないものはシンプルなリテラル(等幅)のノードが作成されます。

.. **Phase 4: Writing**

   This phase converts the resolved doctrees to the desired output format, such
   as HTML or LaTeX.  This happens via a so-called docutils writer that visits
   the individual nodes of each doctree and produces some output in the process.

**フェーズ 4: 書き出し**

   このフェーズでは参照が解決されたDOCツリーを、HTMLやLaTeXなどの指定された出力フォーマットに変換します。このプロセス中では、docutilsのライターと呼ばれるものがDOCツリーの個々のノードをたどって、出力を行っていきます。

.. .. note::

   Some builders deviate from this general build plan, for example, the builder
   that checks external links does not need anything more than the parsed
   doctrees and therefore does not have phases 2--4.

.. note::

   いくつかのビルダーの中には、この一般的なビルド計画から外れているものもあります。
   例えば、外部リンクチェックのビルダーはdoctreeのパースをする以上の情報は不要なので、フェーズ2～4を行いません。


.. Extension Design

拡張のデザイン
----------------

.. We want the extension to add the following to Sphinx:

以下のような拡張機能をSphinxに追加したいと考えているとします:

.. * A "todo" directive, containing some content that is marked with "TODO", and
     only shown in the output if a new config value is set.  (Todo entries should
     not be in the output by default.)

* "todo"ディレクティブは、"TODO"としてやらなければならないことをコンテンツとして持ち、新しい設定値で表示するように指定されたときだけ表示します。デフォルトではtodoのエントリーは表示されないようにします。

.. * A "todolist" directive that creates a list of all todo entries throughout the
     documentation.

* "todolist"ディレクティブがあると、全ドキュメントに含まれるTodoの項目を集めて、リストを作成します。

.. For that, we will need to add the following elements to Sphinx:

これを実現するためには、Sphinxに以下の項目を追加する必要があるでしょう:

.. * New directives, called ``todo`` and ``todolist``.
   * New document tree nodes to represent these directives, conventionally also
     called ``todo`` and ``todolist``.  We wouldn't need new nodes if the new
     directives only produced some content representable by existing nodes.
   * A new config value ``todo_include_todos`` (config value names should start
     with the extension name, in order to stay unique) that controls whether todo
     entries make it into the output.
   * New event handlers: one for the :event:`doctree-resolved` event, to replace
     the todo and todolist nodes, and one for :event:`env-purge-doc` (the reason
     for that will be covered later).

* ``todo``, ``todolist``\ と呼ばれる新しいディレクティブ
* ``todo``, ``todolist``\ というディレクティブが使用された場合に、それを表現する慣習的な新しいドキュメントツリーのノード。もしも、新しいディレクティブが、既存のノードで表現可能なものだけを生成するのであれば、新しいノードを作成する必要はありません。
* ``todo_include_todos``\ という新しい設定値。設定値の名前は、一意性を保つために拡張名から始まる名前にしてください。この設定値はtodoのエントリーが、出力を行うかどうかを判断します
* 新しいイベントハンドラ。一つはtodoとtodolistのノードを置き換えるための :event:`doctree-resolved` イベントハンドラで、もう一つは  :event:`env-purge-doc` (理由は後で説明します)です。

.. The Setup Function

setup関数
------------------

.. currentmodule:: sphinx.application

.. The new elements are added in the extension's setup function.  Let us create a
   new Python module called :file:`todo.py` and add the setup function:

新しい要素は、拡張の中のsetup関数の中で追加していきます。まずは :file:`todo.py` という新しいPythonのモジュールを作成して、以下のようなsetup関数を追加しましょう::

   def setup(app):
       app.add_config_value('todo_include_todos', False, False)

       app.add_node(todolist)
       app.add_node(todo,
                    html=(visit_todo_node, depart_todo_node),
                    latex=(visit_todo_node, depart_todo_node),
                    text=(visit_todo_node, depart_todo_node))

       app.add_directive('todo', TodoDirective)
       app.add_directive('todolist', TodolistDirective)
       app.connect('doctree-resolved', process_todo_nodes)
       app.connect('env-purge-doc', purge_todos)

.. The calls in this function refer to classes and functions not yet written.  What
   the individual calls do is the following:

この関数の中で参照されているクラスと関数の中には、まだ説明していないものもあります。呼ばれているものが個々に何をしているか、というのを順番に説明していきます:

.. * :meth:`~Sphinx.add_config_value` lets Sphinx know that it should recognize the
     new *config value* ``todo_include_todos``, whose default value should be
     ``False`` (this also tells Sphinx that it is a boolean value).

     If the third argument was ``True``, all documents would be re-read if the
     config value changed its value.  This is needed for config values that
     influence reading (build phase 1).

* :meth:`~Sphinx.add_config_value` メソッドはSphinxに対して新しい\ **設定値**\ である\  ``todo_include_todos``\ を追加するように指示して、 :file:`conf.py` の中に書けるようにします。このオプションのデフォルト値は\ ``False``\ になります。また、この設定値がブーリアンの値を取るということもSphinxに知らせます。

  もしも3番目の引数が\ ``True``\ の場合には、設定値が変更された場合にすべてのドキュメントが再読み込みされます。この引数は、設定値がフェーズ.1の読み込みに対して影響を与えるかどうかを指定するのに必要です。

.. * :meth:`~Sphinx.add_node` adds a new *node class* to the build system.  It also
     can specify visitor functions for each supported output format.  These visitor
     functions are needed when the new nodes stay until phase 4 -- since the
     ``todolist`` node is always replaced in phase 3, it doesn't need any.

     We need to create the two node classes ``todo`` and ``todolist`` later.

* :meth:`~Sphinx.add_node` メソッドは、ビルドシステムに対して新しい\ **ノードクラス**\ を追加します。このメソッドはサポートする出力形式ごとにビジター関数を定義することができます。これらのビジター関数は新しいノードがフェーズ.4まで残っている場合に必要になります。\ ``todolist``\ はフェーズ.3までにすべて置き換えられてしまうため、ビジターを指定する必要はありません。

.. * :meth:`~Sphinx.add_directive` adds a new *directive*, given by name and class.

     The handler functions are created later.

* :meth:`~Sphinx.add_directive` メソッドは、指定された名前とクラスから、新しい\ ``ディレクティブ``\ を追加します。

  ハンドラー関数は後で作成します。

.. * Finally, :meth:`~Sphinx.connect` adds an *event handler* to the event whose
     name is given by the first argument.  The event handler function is called
     with several arguments which are documented with the event.

* 最後に、 :meth:`~Sphinx.connect` メソッドは、最初の引数に指定されたイベントの名前に対する、\ **イベントハンドラ**\ を追加します。イベントハンドラの関数は、ドキュメントに関する引数をいくつか伴って呼び出されます。


.. The Node Classes

ノードクラス
----------------

.. Let's start with the node classes:

それではノードクラスを実装していきます::

   from docutils import nodes

   class todo(nodes.Admonition, nodes.Element):
       pass

   class todolist(nodes.General, nodes.Element):
       pass

   def visit_todo_node(self, node):
       self.visit_admonition(node)

   def depart_todo_node(self, node):
       self.depart_admonition(node)

.. Node classes usually don't have to do anything except inherit from the standard
   docutils classes defined in :mod:`docutils.nodes`.  ``todo`` inherits from
   ``Admonition`` because it should be handled like a note or warning, ``todolist``
   is just a "general" node.

ノードクラスは :mod:`docutils.nodes` の中で定義されているdocutilsの標準クラスを継承する以外には何もやる必要はありません。\ ``todo``\ は\ ``note``\ や\ ``warning``\ のように使用されなければならないため、\ ``Admonition``\ クラスを定義しています。\ ``todolist``\ は単なる"一般"ノードです。

.. The Directive Classes

ディレクティブクラス
---------------------

.. A directive class is a class deriving usually from
   ``docutils.parsers.rst.Directive``.  Since the class-based directive interface
   doesn't exist yet in Docutils 0.4, Sphinx has another base class called
   ``sphinx.util.compat.Directive`` that you can derive your directive from, and it
   will work with both Docutils 0.4 and 0.5 upwards.  The directive interface is
   covered in detail in the docutils documentation; the important thing is that the
   class has a method ``run`` that returns a list of nodes.

ディレクティブクラスは、通常は\ ``docutils.parsers.rst.Directive``\ クラスを継承しています。Docutils 0.4にはクラスベースのディレクティブのインタフェースがなかったため、Sphinxは\ ``sphinx.util.compat.Directive``\ というクラスを実装しています。これを継承して実装すると、Docutils 0.4でも、0.5以上でも同じように動作します。このディレクティブのインタフェースはdocutilsのドキュメントの詳細までカバーしています。また、ディレクティブのインタフェースとして必須なのは、ノードのリストを返す\ ``run``\ メソッドを定義していることになります。

.. The ``todolist`` directive is quite simple:

``todolist``\ ディレクティブはきわめてシンプルです：：

   from sphinx.util.compat import Directive

   class TodolistDirective(Directive):

       def run(self):
           return [todolist('')]

.. An instance of our ``todolist`` node class is created and returned.  The
   todolist directive has neither content nor arguments that need to be handled.

``todolist``\ ノードクラスのインスタンスを作って返しています。\ ``todolist``\ ディレクティブでは、コンテンツも引数も取り扱う必要はありません。

.. The ``todo`` directive function looks like this:

``todo``\ ディレクティブのクラスは以下のようになります::

   from sphinx.util.compat import make_admonition

   class TodoDirective(Directive):

       # この変数をセットすると、ディレクティブの中にコンテンツを書けるようになります。
       has_content = True

       def run(self):
           env = self.state.document.settings.env

           targetid = "todo-%d" % env.new_serialno('todo')
           targetnode = nodes.target('', '', ids=[targetid])

           ad = make_admonition(todo, self.name, [_('Todo')], self.options,
                                self.content, self.lineno, self.content_offset,
                                self.block_text, self.state, self.state_machine)

           if not hasattr(env, 'todo_all_todos'):
               env.todo_all_todos = []
           env.todo_all_todos.append({
               'docname': env.docname,
               'lineno': self.lineno,
               'todo': ad[0].deepcopy(),
               'target': targetnode,
           })

           return [targetnode] + ad

..  # this enables content in the directive

.. Several important things are covered here. First, as you can see, you can refer
   to the build environment instance using ``self.state.document.settings.env``.

拡張機能の作成にあたって重要なことがこのクラスでカバーされています。まず最初に、見てわかるように、\ ``self.state.document.settings.env``\ を通じて、ビルド環境のインスタンスを参照することができるということです。

.. Then, to act as a link target (from the todolist), the todo directive needs to
   return a target node in addition to the todo node.  The target ID (in HTML, this
   will be the anchor name) is generated by using ``env.new_serialno`` which is
   returns a new integer directive on each call and therefore leads to unique
   target names.  The target node is instantiated without any text (the first two
   arguments).


   persistent between directive calls and therefore leads to unique target names.
   The target node is instantiated without any text (the first two arguments).

次に、\ ``todolist``\ からのリンクターゲットとして動作するために、\ ``todo``\ ディレクティブが\ ``todo``\ ノードだけでなく、ターゲットとなるノードを返さなければならないという点です。ターゲットのIDは\ ``env.new_serialno``\ を使用して作成されます。それぞれの呼び出しごとに、ユニークなターゲット名に繋がるような、これは新しい数値のディレクティブを返します。ターゲットノードは、あらゆるテキスト(最初の二つの引数)を受け取ることなく、インスタンス化されます。

.. An admonition is created using a standard docutils function (wrapped in Sphinx
   for docutils cross-version compatibility).  The first argument gives the node
   class, in our case ``todo``.  The third argument gives the admonition title (use
   ``arguments`` here to let the user specify the title).  A list of nodes is
   returned from ``make_admonition``.

Admonition(勧告)は標準のdocutils関数(docutilsのバージョン間の互換性のためにSphinxでラップしてある)を使って作成します。最初の引数はノードのクラスで、ここでは\ ``todo``\ を設定しています。３番目の引数はAdmonitionのタイトルです。\ ``arguments``\ を使用して、ユーザ定義の名前になります。\ ``make_admonition``\ から返されたものはノードのリストになります。

.. Then, the todo node is added to the environment.  This is needed to be able to
   create a list of all todo entries throughout the documentation, in the place
   where the author puts a ``todolist`` directive.  For this case, the environment
   attribute ``todo_all_todos`` is used (again, the name should be unique, so it is
   prefixed by the extension name).  It does not exist when a new environment is
   created, so the directive must check and create it if necessary.  Various
   information about the todo entry's location are stored along with a copy of the
   node.

``todo``\ ノードが環境に追加されました。これは全ドキュメントのToDoのエントリーのリストを作成できるようにするために必要なものです。ここで作ったリストは\ ``todolist``\ ディレクティブが置かれているところに出力されます。この場合、環境の属性の\ ``todo_all_todos``\ が使用されます。繰り返しになりますが、名前の重複を避けるために、属性名の頭には拡張名を設定します。新しい環境が作成されたときにはまだ存在していないため、ディレクティブの中では必要に応じてあるかどうかチェックを行い、作成する必要があります。ToDoエントリーの位置に関するさまざまな情報がノードのコピーの中に保存されます。

.. In the last line, the nodes that should be put into the doctree are returned:
   the target node and the admonition node.

最後の行では、作成したターゲットノードと、AdmonitionノードをDOCツリーの中に配置するために、returnで返しています。

.. The node structure that the directive returns looks like this:

ディレクティブが返すノード構造は以下のようになっています::

   +--------------------+
   | target node        |
   +--------------------+
   +--------------------+
   | todo node          |
   +--------------------+
     \__+--------------------+
        | admonition title   |
        +--------------------+
        | paragraph          |
        +--------------------+
        | ...                |
        +--------------------+


.. The Event Handlers

イベントハンドラ
------------------


.. Finally, let's look at the event handlers.  First, the one for the
   :event:`env-purge-doc` event:

最後に、イベントハンドラを見ていきます。最初に見るのは :event:`env-purge-doc` イベントです::

   def purge_todos(app, env, docname):
       if not hasattr(env, 'todo_all_todos'):
           return
       env.todo_all_todos = [todo for todo in env.todo_all_todos
                             if todo['docname'] != docname]

.. Since we store information from source files in the environment, which is
   persistent, it may become out of date when the source file changes.  Therefore,
   before each source file is read, the environment's records of it are cleared,
   and the :event:`env-purge-doc` event gives extensions a chance to do the same.
   Here we clear out all todos whose docname matches the given one from the
   ``todo_all_todos`` list.  If there are todos left in the document, they will be
   added again during parsing.

ソースファイルの中から情報を取り出し、環境の中に格納しましたが、これは永続化されます。そのため、ソースファイルが変更されると古い情報になってしまう可能性があります。そのため、それぞれのソースファイルを読み込む前に、環境の記録をクリアしています。 :event:`env-purge-doc` イベントは、拡張機能の中でそのような作業を行うのに適した場所になります。ここでは\ ``todo_all_todos``\ のリストの中の項目のうち、ドキュメントの名前(``docname``)がマッチしたものを削除しています。もしもドキュメント内のToDoが残っていたとしたら、パース時に重複して追加されてしまいます。

.. The other handler belongs to the :event:`doctree-resolved` event.  This event is
   emitted at the end of phase 3 and allows custom resolving to be done:

もう一つ :event:`doctree-resolved` イベントに関連したハンドラが定義されています。このイベントはフェーズ.3が完了したところで発生(emit)します。解決処理を独自に実装することができるようになります::

   def process_todo_nodes(app, doctree, fromdocname):
       if not app.config.todo_include_todos:
           for node in doctree.traverse(todo):
               node.parent.remove(node)

       # すべての todolist ノードを、収集したtodoのリストと置き換えます
       # それぞれの項目には、元の定義された位置へのリンクを追加します
       env = app.builder.env

       for node in doctree.traverse(todolist):
           if not app.config.todo_include_todos:
               node.replace_self([])
               continue

           content = []

           for todo_info in env.todo_all_todos:
               para = nodes.paragraph()
               filename = env.doc2path(todo_info['docname'], base=None)
               description = (
                   _('(The original entry is located in %s, line %d and can be found ') %
                   (filename, todo_info['lineno']))
               para += nodes.Text(description, description)

               # 参照の作成
               newnode = nodes.reference('', '')
               innernode = nodes.emphasis(_('here'), _('here'))
               newnode['refdocname'] = todo_info['docname']
               newnode['refuri'] = app.builder.get_relative_uri(
                   fromdocname, todo_info['docname'])
               newnode['refuri'] += '#' + todo_info['target']['refid']
               newnode.append(innernode)
               para += newnode
               para += nodes.Text('.)', '.)')

               # ToDoリストへの追加
               content.append(todo_info['todo'])
               content.append(para)

           node.replace_self(content)

..
       # Replace all todolist nodes with a list of the collected todos.
       # Augment each todo with a backlink to the original location.
       # Create a reference
       # Insert into the todolist

.. It is a bit more involved.  If our new "todo_include_todos" config value is
   false, all todo and todolist nodes are removed from the documents.

このコードは多少込み入っています。もしも新しい設定値である\ ``"todo_include_todos"``\ がfalseの場合には、すべてのtodoおよび、todolistのノードをドキュメントから削除します。

.. If not, todo nodes just stay where and how they are.  Todolist nodes are
   replaced by a list of todo entries, complete with backlinks to the location
   where they come from.  The list items are composed of the nodes from the todo
   entry and docutils nodes created on the fly: a paragraph for each entry,
   containing text that gives the location, and a link (reference node containing
   an italic node) with the backreference.  The reference URI is built by
   ``app.builder.get_relative_uri`` which creates a suitable URI depending on the
   used builder, and appending the todo node's (the target's) ID as the anchor
   name.

trueの場合にはtodoのノードはその場に保持されます。todolistノードはtodoのエントリーのリストに置き換えられ、定義された場所への逆リンクが張られます。リストアイテムはtodoエントリーのノードの内容から作成され、その場でdocutilsのノードが作成されます。エントリーごとに段落が作られます。段落の中には定義された位置を表すテキストと逆参照のためのリンクが含まれます。また参照はイタリック体のノードの中に定義されます。参照のリンクは\ ``app.builder.get_relative_uri``\ 関数によって作成されます。これはビルダーごとに適したURIを作成します。リンクには、ノードのターゲットのIDがアンカー名として追加されています。

.. highlight:: rest

.. :mod:`sphinx.ext.doctest` -- Test snippets in the documentation

:mod:`sphinx.ext.doctest` -- ドキュメント内の簡易テスト
=======================================================

.. module:: sphinx.ext.doctest
   :synopsis: ドキュメント内の簡易テスト

..   :synopsis: Test snippets in the documentation.


     .. index:: pair: automatic; testing
           single: doctest
           pair: testing; snippets

.. index:: pair: 自動; テスト
           single: doctest
           pair: テスト; 簡易

.. This extension allows you to test snippets in the documentation in a natural
   way.  It works by collecting specially-marked up code blocks and running them as
   doctest tests.

このSphinx拡張を使用すると、自然な形で、ドキュメント内で簡単なテストを行えるようになります。特別なマークアップのされたコードブロックを収集して、doctestとしてテストを行います。

.. Within one document, test code is partitioned in *groups*, where each group
   consists of:

ひとつのドキュメント内で、テストコードを\ **グループ**\ という形で分けることができます。それぞれのグループは以下のものを含みます。

.. * zero or more *setup code* blocks (e.g. importing the module to test)
.. * one or more *test* blocks

* ゼロ個以上の\ **セットアップコード**\ ブロック。テストに必要なモジュールをimportします。
* ひとつ以上の\ **テスト**\ ブロック。

.. When building the docs with the ``doctest`` builder, groups are collected for
   each document and run one after the other, first executing setup code blocks,
   then the test blocks in the order they appear in the file.

``doctest``\ ビルダーを使用してドキュメントをビルドすると、それぞれのドキュメントごとに同一グループの要素が集められて次々に実行されます。最初はセットアップコードブロックが実行され、その後はファイルの中で登場する順番にテストブロックが実行されます。

.. There are two kinds of test blocks:

テストブロックには以下の２種類あります:

.. * *doctest-style* blocks mimic interactive sessions by interleaving Python code
  (including the interpreter prompt) and output.

* Pythonコード(含プロンプト)と出力が交互に書かれている、インタラクティブモードに似た\ **doctestスタイル**\ のブロック

.. * *code-output-style* blocks consist of an ordinary piece of Python code, and
   optionally, a piece of output for that code.

* 通常のPythonコードと、出力を1つから構成される、\ **コード-出力スタイル**\ のブロック

.. The doctest extension provides four directives.  The *group* argument is
   interpreted as follows: if it is empty, the block is assigned to the group named
   ``default``.  If it is ``*``, the block is assigned to all groups (including the
   ``default`` group).  Otherwise, it must be a comma-separated list of group
   names.

doctest拡張は4つのディレクティブを提供します。 **グループ**\ 引数は以下のように解釈されます:

* もしも何も指定されなかった場合には、\ ``default``\ というグループ名が指定されたとみなします
* もしも\ ``*``\ が指定されると、そのブロックは\ ``default``\ を含む、すべてのグループに対して割り当てられたものとみなします。そうでなければ、これ以外の場合はグループ名は、カンマ区切りのリストでなければなりません。

.. rst:directive:: .. testsetup:: [グループ]

   セットアップのためのコードブロックです。このコードは他のビルダーを使用したときには出力されませんが、それが所属するグループのdoctestが実行される前に実行されます。

.. A setup code block.  This code is not shown in the output for other builders,
   but executed before the doctests of the group(s) it belongs to.


.. rst:directive:: .. doctest:: [グループ]

   doctestスタイルのコードブロックです。標準の :mod:`docteset` のフラグを使用すると、ユーザが指定した理想の出力と、実際に出力したものをどのように比較するのか、というのを制御することができます。以下のオプションが使用できます:

   * ``ELLIPSIS``

     省略記号(...)を期待される出力の中に書くことができます。どのような結果が来てもマッチします。

   * ``IGNORE_EXCEPTION_DETAIL``

     例外の詳細を省略して比較します。トレースバックの詳細までは比較しないようになります。

   * ``DONT_ACCEPT_TRUE_FOR_1``

     デフォルトでは、実際の出力が"True"で、理想の結果が"1"となっていた場合、デフォルトではこれもテスト成功とみなします。Python 2.2以前の名残です。

   このディレクティブは以下の二つのオプションをサポートしています:

   * ``hide``\ はフラグオプションです。他のビルダーの使用時に、doctestブロックを隠します。デフォルトでは、ハイライトされたdoctestブロックとして表示されます。

   * ``options``\ は文字列オプションです。それぞれのテストのサンプルに対して、カンマ区切りのdoctestフラグのリストを設定するのに使用します。doctestコメントの中でサンプルごとにフラグを明示することもできますが、他のビルダーをしようすると、そのフラグまでレンダリングされてしまいます。

   標準ライブラリのdoctestでは、予想出力の中に空行を入れたい場合には\ ``<BLANKLINE>``\ というキーワードを指定しなければなりませんでした。\ ``<BLANKLINE>``\ はHTMLやLaTeXなど、人が読める出力を行うビルドの際には削除されます。

   doctestの中で書くのと同様に、インラインでdoctestのオプションを指定することもできます。

      >>> datetime.date.now()   # doctest: +SKIP
      datetime.date(2008, 1, 1)

   これらのオプションは、テストの実行時には識別されますが、HTMLなどの出力の際には削除されます。

.. A doctest-style code block.  You can use standard :mod:`doctest` flags for
   controlling how actual output is compared with what you give as output.  By
   default, these options are enabled: ``ELLIPSIS`` (allowing you to put
   ellipses in the expected output that match anything in the actual output),
   ``IGNORE_EXCEPTION_DETAIL`` (not comparing tracebacks),
   ``DONT_ACCEPT_TRUE_FOR_1`` (by default, doctest accepts "True" in the output
   where "1" is given -- this is a relic of pre-Python 2.2 times).

   This directive supports two options:

   * ``hide``, a flag option, hides the doctest block in other builders.  By
     default it is shown as a highlighted doctest block.

   * ``options``, a string option, can be used to give a comma-separated list of
     doctest flags that apply to each example in the tests.  (You still can give
     explicit flags per example, with doctest comments, but they will show up in
     other builders too.)

   Note that like with standard doctests, you have to use ``<BLANKLINE>`` to
   signal a blank line in the expected output.  The ``<BLANKLINE>`` is removed
   when building presentation output (HTML, LaTeX etc.).

   Also, you can give inline doctest options, like in doctest::

      >>> datetime.date.now()   # doctest: +SKIP
      datetime.date(2008, 1, 1)

   They will be respected when the test is run, but stripped from presentation
   output.


.. rst:directive:: .. testcode:: [グループ]

   コード-出力タイプのテストのコードブロックです。

   このディレクティブは以下のオプションをサポートしています:

   * ``hide``\ はフラグオプションで、doctest以外の他のビルダーのビルド時はコードブロックが表示されなくなります。デフォルトでは、ハイライトされたコードブロックとして表示されます。

   .. note::

      ``testcode`` ブロックの中のコードは、含まれている文の量に関わらず、すべて、一度だけ実行されます。そのため、単なる式の場合には、出力は **行われません** 。 ``print`` を使用してください。サンプル::

         .. testcode::

            1+1        # 出力が行われない！
            print 2+2  # 出力が行われる

         .. testoutput::

            4

      doctestモジュールも、通常の出力と、例外メッセージを同じコードスニペット内で混ぜた書き方をサポートしていないように、testcode/testoutputにも同様の制限がある点に注意してください。

.. A code block for a code-output-style test.

   This directive supports one option:

   * ``hide``, a flag option, hides the code block in other builders.  By
     default it is shown as a highlighted code block.

   .. note::

      Code in a ``testcode`` block is always executed all at once, no matter how
      many statements it contains.  Therefore, output will *not* be generated
      for bare expressions -- use ``print``.  Example::

          .. testcode::

             1+1        # this will give no output!
             print 2+2  # this will give output

          .. testoutput::

             4

      Also, please be aware that since the doctest module does not support
      mixing regular output and an exception message in the same snippet, this
      applies to testcode/testoutput as well.

.. rst:directive:: .. testoutput:: [グループ]

   最後に定義された :rst:dir:`testcode` ブロックに対応する出力, もしくは例外メッセージを定義します。

   このディレクティブは以下の２つのオプションをサポートしています:

   * ``hide``\ はフラグオプションで、doctest以外の他のビルダーのビルド時はコードブロックが表示されなくなります。デフォルトでは、ハイライトされたコードブロックとして表示されます。

   * ``options``\ は文字列オプションで、通常のdoctestブロックと同じように、カンマ区切りのdoctestのフラグを設定するのに使用されます。

   サンプル::

      .. testcode::

         print '出力テキスト.'

      .. testoutput::
         :hide:
         :options: -ELLIPSIS, +NORMALIZE_WHITESPACE

         出力テキスト.

.. The corresponding output, or the exception message, for the last
   :rst:dir:`testcode` block.

   This directive supports two options:

   * ``hide``, a flag option, hides the output block in other builders.  By
     default it is shown as a literal block without highlighting.

   * ``options``, a string option, can be used to give doctest flags
     (comma-separated) just like in normal doctest blocks.

   Example:

      .. testoutput::
         :hide:
         :options: -ELLIPSIS, +NORMALIZE_WHITESPACE

         Output text.


.. The following is an example for the usage of the directives.  The test via
   :rst:dir:`doctest` and the test via :rst:dir:`testcode` and :rst:dir:`testoutput` are
   equivalent. 

以下のコードはこれらのディレクティブの使用方法のサンプルです。 :rst:dir:`doctest` を使用したテストと、 :rst:dir:`testcode` および :rst:dir:`testoutput` の二つで構成されたテストは等価です. ::

   オウムモジュール
   ================

   .. testsetup:: *

      import parrot

   parrotモジュールはオウムに関するモジュールです

   Doctest例:

   .. doctest::

      >>> parrot.voom(3000)
      This parrot wouldn't voom if you put 3000 volts through it!

   テスト出力例:

   .. testcode::

      parrot.voom(3000)

   この出力は以下のようになります:

   .. testoutput::

      This parrot wouldn't voom if you put 3000 volts through it!

.. There are also these config values for customizing the doctest extension:

doctest拡張の動作をカスタマイズする設定がいくつかあります:

.. confval:: doctest_path

   doctestビルダーが使用されるときに、 :data:`sys.path` に対して追加されるディレクトリのリストです。必ず絶対パスで記述してください。

.. A list of directories that will be added to :data:`sys.path` when the doctest
   builder is used.  (Make sure it contains absolute paths.)

.. confval:: doctest_global_setup

   Pythonコードを記述します。このコードはテストされる\ **すべての**\ ファイルの\ ``testsetup``\ ディレクティブに書き込んだのと同じように扱われます。例えば、doctest時にいつでも必要となるモジュールをimportするといった用途に使用できます。

   .. versionadded:: 0.6

.. Python code that is treated like it were put in a ``testsetup`` directive for
   *every* file that is tested, and for every group.  You can use this to
   e.g. import modules you will always need in your doctests.

.. confval:: doctest_test_doctest_blocks

   .. If this is a nonempty string (the default is ``'default'``), standard reST
      doctest blocks will be tested too.  They will be assigned to the group name
      given.

   この値に空でない文字列(デフォルトは\ ``'default'``)が設定されると、標準のreSTのdoctestブロックもテストされるようになります。それらのテストには、ここで与えられたグループ名が設定されます。

   .. reST doctest blocks are simply doctests put into a paragraph of their own,
      like so:

         Some documentation text.
  
         >>> print 1
         1
  
         Some more documentation text.

   reSTのdoctestブロックは、reSTの中のパラグラフとして単純にdoctestが置かれます::

      何かドキュメント.

      >>> print 1
      1

      追加の何かドキュメント.

   .. (Note that no special ``::`` is used to introduce the doctest block; docutils
      recognizes them from the leading ``>>>``.  Also, no additional indentation is
      used, though it doesn't hurt.)

   reSTの場合は、doctestブロックを表現するのに特別な\ ``::``\ は使用されません。docutilsは\ ``>>>``\ から始まる行を識別します。そのため、doctestのために追加でインデントを設定する必要はありません。

   .. If this value is left at its default value, the above snippet is interpreted
      by the doctest builder exactly like the following::

         Some documentation text.

         .. doctest::

            >>> print 1
            1

         Some more documentation text.

   この設定値がデフォルトのままであったとすると、上記のコード片は、下記のように書いた場合と同じようにdoctestビルダーから解釈されます::

      何かドキュメント.

      .. doctest::

         >>> print 1
         1

      追加の何かドキュメント.

   .. This feature makes it easy for you to test doctests in docstrings included
      with the :mod:`~sphinx.ext.autodoc` extension without marking them up with a
      special directive.

   この機能があるおかげで :mod:`~sphinx.ext.autodoc` 拡張を使用して取り込んだdocstring中のdoctestを簡単に実行することができます。特別なディレクティブでマークアップする必要はありません。

   .. Note though that you can't have blank lines in reST doctest blocks.  They
      will be interpreted as one block ending and another one starting.  Also,
      removal of ``<BLANKLINE>`` and ``# doctest:`` options only works in
      :rst:dir:`doctest` blocks, though you may set :confval:`trim_doctest_flags` to
      achieve the latter in all code blocks with Python console content.

   reSTのdoctestブロックでは空白行はパラグラフの境界として使用されるため、そのままでは結果として空行を記述することはできません。 :confval:`trim_doctest_flags` を設定して、すべてのコードブロックに対してPythonのコンソール出力を含めることができますが、削除された\ ``<BLANKLINE>``\ と\ ``# doctest:``\ は、 :rst:dir:`doctest` ブロック内でのみ動作します。




.. _extensions:

Sphinx拡張
==========

.. module:: sphinx.application
   :synopsis: アプリケーションクラスおよび、拡張インタフェース

..   :synopsis: Application class and extensibility interface.

.. Since many projects will need special features in their documentation, 
   Sphinx is designed to be extensible on several levels.

多くのプロジェクトはドキュメントの作成に関して特別な機能を必要とするでしょう。Sphinxはさまざまなレベルで拡張ができるように設計されています。

.. This is what you can do in an extension: First, you can add new
   :term:`builder`\s to support new output formats or actions on the parsed
   documents.  Then, it is possible to register custom reStructuredText roles and
   directives, extending the markup.  And finally, there are so-called "hook
   points" at strategic places throughout the build process, where an extension can
   register a hook and run specialized code.

拡張機能を通じてできることは主に３つあります。一つ目は新しい出力形式に対応したり、ドキュメントパース時の新しいアクションをサポートするために、\ :term:`ビルダー`\ を追加することができます。二つ目は、reStructuredText用の、新しいカスタムのロールやディレクティブを追加したり、マークアップを拡張したりすることができます。三つ目は"フックポイント"と呼ばれるもので、ビルドプロセスのさまざまな箇所に存在していて、特別なコードを実行するためのフックを登録することができます。

.. An extension is simply a Python module.  When an extension is loaded, Sphinx
   imports this module and executes its ``setup()`` function, which in turn
   notifies Sphinx of everything the extension offers -- see the extension tutorial
   for examples.

Sphinx拡張はシンプルなPythonモジュールです。拡張機能がロードされる時には、Sphinxはこのモジュールをインポートして、モジュール内にある\ ``setup()``\ 関数を呼び出します。この関数の中では拡張機能が提供するものをSphinxに知らせます。詳しくはSphinx拡張のチュートリアルの例を見てください。

.. The configuration file itself can be treated as an extension if it contains a
   ``setup()`` function.  All other extensions to load must be listed in the
   :confval:`extensions` configuration value.

設定ファイルそのものも、\ ``setup()``\ 関数を持っている場合には拡張機能として扱われます。それ以外のロードが必要なすべての拡張機能は、設定ファイルの中の :confval:`extensions` の中にリストアップしてください。

.. toctree::

   ext/tutorial
   ext/appapi
   ext/builderapi


.. Builtin Sphinx extensions
   
組み込みのSphinx拡張機能
-------------------------

.. These extensions are built in and can be activated by respective entries in the
   :confval:`extensions` configuration value:

これらの拡張機能はすべてSphinxに組み込まれています。設定ファイルの :confval:`extensions` のリストの中に名前を書くことで使用することができるようになります:

.. toctree::

   ext/autodoc
   ext/autosummary
   ext/doctest
   ext/intersphinx
   ext/math
   ext/graphviz
   ext/inheritance
   ext/refcounting
   ext/ifconfig
   ext/coverage
   ext/todo
   ext/extlinks
   ext/viewcode
   ext/oldcmarkup


.. Third-party extensions

サードパーティ製の拡張機能
--------------------------

.. There are several extensions that are not (yet) maintained in the Sphinx
   distribution.  The `Wiki at BitBucket`_ maintains a list of those.

Sphinxのディストリビューション内で(まだ)メンテナンスされていない拡張機能もいくつか存在します。
`BitBucketのWiki`_ の中に、これらのリストがあります。

.. If you write an extension that you think others will find useful, please write
   to the project mailing list (`join here <http://groups.google.com/group/sphinx-dev>`_) and we'll find the
   proper way of including or hosting it for the public.

もしも他の人から見て便利そうに見えると思えるような拡張機能を書いた場合には、プロジェクトのメーリングリスト(`ここから参加してください <http://groups.google.com/group/sphinx-dev>`_)に知らせてください。Sphinxに取り込まれたり、公開するためのホスティングの仕方について説明してもらえるでしょう。

.. _BitBucketのWiki: http://www.bitbucket.org/birkenfeld/sphinx/wiki/Home


.. Where to put your own extensions?

自分自身の拡張機能はどこに置くべき？
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. Extensions local to a project should be put within the project's directory
   structure.  Set Python's module search path, ``sys.path``, accordingly so that
   Sphinx can find them.
   E.g., if your extension ``foo.py`` lies in the ``exts`` subdirectory of the
   project root, put into :file:`conf.py`:

プロジェクトに関連する拡張機能はプロジェクトのディレクトリ構造の中に置かれるべきです。Pythonがモジュールを検索するのに使用する、\ ``sys.path``\ に置き場所を追加してSphinxがそれを見つけられるようにしましょう。たとえば、作った拡張機能が\ ``foo.py``\ という名前で、プロジェクトルートの下の\ ``exts``\ フォルダに置かれていた場合には、 :file:`conf.py` の中に以下のように記述します::

     import sys, os

     sys.path.append(os.path.abspath('exts'))

     extensions = ['foo']

.. You can also install extensions anywhere else on ``sys.path``, e.g. in the
   ``site-packages`` directory.

``sys.path``\ を使う以外の方法では、\ ``site-packages``\ ディレクトリの中にインストールするという方法などもあります。

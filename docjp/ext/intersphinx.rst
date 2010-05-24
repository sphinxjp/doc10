..

:mod:`sphinx.ext.intersphinx` -- 他のプロジェクトのドキュメントへのリンク
==========================================================================

.. module:: sphinx.ext.intersphinx
   :synopsis: 他のsphinxドキュメントにリンクします。

.. :synopsis: Link to other Sphinx documentation.

.. index:: pair: automatic; linking

.. versionadded:: 0.5

.. This extension can generate automatic links to the documentation of Python
   objects in other projects.  This works as follows:

この拡張機能は他のプロジェクトのPythonオブジェクトのドキュメントに対して、自動リンクを生成することができるようになります。この拡張機能は以下のように動作します。

.. * Each Sphinx HTML build creates a file named :file:`objects.inv` that
     contains a mapping from Python identifiers to URIs relative to the HTML set's
     root.

* Sphinxを使って生成されたHTMLの中には :file:`objects.inv` というファイルがあります。このファイルの中にはPythonの識別子とHTMLのルートからの相対URLのマッピング情報が含まれます。

.. * Projects using the Intersphinx extension can specify the location of such
     mapping files in the :confval:`intersphinx_mapping` config value.  The mapping
     will then be used to resolve otherwise missing references to Python objects
     into links to the other documentation.

* intersphinx拡張を使用したプロジェクトは、 :confval:`intersphinx_mapping` という設定値を使って、そのマッピングファイルの場所を指定することができます。このマッピング情報は、リンクが解決されていないPythonオブジェクトの参照から、外部のドキュメントのリンクを張るために使用されます。

.. * By default, the mapping file is assumed to be at the same location as the rest
     of the documentation; however, the location of the mapping file can also be
     specified individually, e.g. if the docs should be buildable without Internet
     access.

デフォルトの設定では、マッピングファイルはドキュメントと同じ位置にあるとみなされます。マッピングファイルの場所は個別に指定することができます。例えば、インターネットのアクセスができない環境でビルドできるようにする場合などです。

.. To use intersphinx linking, add ``'sphinx.ext.intersphinx'`` to your
   :confval:`extensions` config value, and use these new config values to activate
   linking:

Sphinx間リンクを使用する場合には、 :confval:`extensions` 設定値に\  ``'sphinx.ext.intersphinx'`` \ を追加します。追加すると、リンクを有効にするための新しい設定値が追加されます。

.. confval:: intersphinx_mapping

   この設定値はURI同士(値は場合によっては\ ``None``)をマッピングする辞書になります。キーは外部のSphinxのドキュメントのベースのURIを設定します。ローカルのパス、もしくはHTTPのURIが使用できます。値の法はインベントリーファイル(.inv)がある場所を設定します。これに設定できるのは、\ ``None``\ (base UIと同じ場所にあるとみなされます)、もしくはローカルのパス、HTTPのURIのどれかになります。

   相対的なローカルパスがキーに設定された場合には、ビルドドキュメントに対して相対的な場所であるとみなされます。値側に相対パスが設定された場合には、ソースディレクトリからの相対パスになります。

   例えば、Pythonの標準のライブラリドキュメントの中のモジュールやオブジェクトに対してリンクが張りたい場合には以下のようにします::

       intersphinx_mapping = {'http://docs.python.org/dev': None}

   これを設定すると、ソースディレクトリの中の :file:`python.inv` からインベントリー情報を読み込み、 ``http://docs.python.org/dev`` 以下のページに対するリンクを作成します。もしもPythonのドキュメントに新しいオブジェクトが追加された場合には、自分でアップデートする必要があります。

   リモートでインベントリーファイルを取得する場合には、環境変数の ``$HTTP_PROXY`` を設定しておくと、プロキシーを経由してアクセスを行います。

.. A dictionary mapping URIs to either ``None`` or an URI.  The keys are the
   base URI of the foreign Sphinx documentation sets and can be local paths or
   HTTP URIs.  The values indicate where the inventory file can be found: they
   can be ``None`` (at the same location as the base URI) or another local or
   HTTP URI.

   Relative local paths in the keys are taken as relative to the base of the
   built documentation, while relative local paths in the values are taken as
   relative to the source directory.

   An example, to add links to modules and objects in the Python standard
   library documentation:

      intersphinx_mapping = {'http://docs.python.org/dev': None}

   This will download the corresponding :file:`objects.inv` file from the
   Internet and generate links to the pages under the given URI.  The downloaded
   inventory is cached in the Sphinx environment, so it must be redownloaded
   whenever you do a full rebuild.

   A second example, showing the meaning of a non-``None`` value::

      intersphinx_mapping = {'http://docs.python.org/dev': 'python-inv.txt'}

   This will read the inventory from :file:`python.inv` in the source
   directory, but still generate links to the pages under
   ``http://docs.python.org/dev``.  It is up to you to update the inventory file
   as new objects are added to the Python documentation.

   When fetching remote inventory files, proxy settings will be read from
   the ``$HTTP_PROXY`` environment variable.

.. confval:: intersphinx_cache_limit

   リモートのインベントリーをキャッシュする最長の日数を設定します。デフォルトは\ ``5``\ で、5日間という意味になります。マイナスの値を設定すると、インベントリーのキャッシュの日数による制限がなくなります。

.. The maximum number of days to cache remote inventories.  The default is
   ``5``, meaning five days.  Set this to a negative value to cache inventories
   for unlimited time.

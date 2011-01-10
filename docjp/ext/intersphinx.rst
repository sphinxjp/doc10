..

:mod:`sphinx.ext.intersphinx` -- 他のプロジェクトのドキュメントへのリンク
==========================================================================

.. module:: sphinx.ext.intersphinx
   :synopsis: 他のsphinxドキュメントにリンクします。

.. :synopsis: Link to other Sphinx documentation.

.. index:: pair: automatic; linking

.. versionadded:: 0.5

.. This extension can generate automatic links to the documentation of objects 
   in other projects.

この拡張機能は他のプロジェクトのオブジェクトのドキュメントに対して、自動リンクを生成することができるようになります。

.. Usage is simple: whenever Sphinx encounters a cross-reference that has no
   matching target in the current documentation set, it looks for targets in the
   documentation sets configured in :confval:`intersphinx_mapping`.  A reference
   like ``:py:class:`zipfile.ZipFile``` can then link to the Python documentation
   for the ZipFile class, without you having to specify where it is located
   exactly.

使用方法はシンプルで、Sphinxがクロスリファレンスの参照を解決しようとして、現在のドキュメントの中から見つけられなかった場合には、 :confval:`intersphinx_mapping` で設定されたドキュメント集の中を探索しにいくようになります。 ``:py:class:`zipfile.ZipFile``` という参照があった場合には、そのドキュメントの詳細な場所を知らなくても、Pythonの標準ライブラリのドキュメントの、ZipFileクラスに対してリンクが張られます。

.. When using the "new" format (see below), you can even force lookup in a foreign
   set by prefixing the link target appropriately.  A link like ``:ref:`comparison
   manual <python:comparisons>``` will then link to the label "comparisons" in the
   doc set "python", if it exists.

もし、「新しい」フォーマット(後述)を使用する場合、リンクターゲット名に特定のプリフィックスを付けることで、強制的に外部ドキュメントを探索しにいくように設定することができます。  ``:ref:`比較マニュアル <python:comparisons>``` というリンクがあれば、もし"python"という名前のドキュメントセットが設定されていたとすると、その中の"comparisons"というラベルを探索しに行きます。

.. Behind the scenes, this works as follows:

この仕組みの背後では、次のようなことが行われています。

.. * Each Sphinx HTML build creates a file named :file:`objects.inv` that contains 
     a mapping from object names to URIs relative to the HTML set's root.

* Sphinxを使って生成されたHTMLの中には :file:`objects.inv` というファイルがあります。このファイルの中にはオブジェクト名と、HTMLのルートからの相対URLのマッピング情報が含まれます。

.. * Projects using the Intersphinx extension can specify the location of such
     mapping files in the :confval:`intersphinx_mapping` config value.  The mapping
     will then be used to resolve otherwise missing references to objects into 
     links to the other documentation.

* intersphinx拡張を使用したプロジェクトは、 :confval:`intersphinx_mapping` という設定値を使って、そのマッピングファイルの場所を指定することができます。このマッピング情報は、リンクが解決されていないオブジェクトの参照から、外部のドキュメントのリンクを張るために使用されます。

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

   .. This config value contains the locations and names of other projects that
      should be linked to in this documentation.

   この設定値には、このドキュメントからリンクさせる他のプロジェクトの場所と名前を設定します。

   .. Relative local paths in the keys are taken as relative to the base of the
      built documentation, while relative local paths in the values are taken as
      relative to the source directory.

   相対的なローカルパスがキーに設定された場合には、ビルドドキュメントに対して相対的な場所であるとみなされます。値側に相対パスが設定された場合には、ソースディレクトリからの相対パスになります。

   .. When fetching remote inventory files, proxy settings will be read from
      the ``$HTTP_PROXY`` environment variable.

   リモートでインベントリーファイルを取得する場合には、環境変数の ``$HTTP_PROXY`` を設定しておくと、プロキシーを経由してアクセスを行います。

   .. **Old format for this config value**

   **この設定値の古いフォーマット**

   .. This is the format used before Sphinx 1.0.  It is still recognized.

   このフォーマットはSphinx 1.0以前で使用されていました。これは現在でも使用できます。

   .. A dictionary mapping URIs to either ``None`` or an URI.  The keys are the
      base URI of the foreign Sphinx documentation sets and can be local paths or
      HTTP URIs.  The values indicate where the inventory file can be found: they
      can be ``None`` (at the same location as the base URI) or another local or
      HTTP URI.

   この設定値はURI同士(値は場合によっては\ ``None``)をマッピングする辞書になります。キーは外部のSphinxのドキュメントのベースのURIを設定します。ローカルのパス、もしくはHTTPのURIが使用できます。値はインベントリファイル(.inv)がある場所を設定します。これに設定できるのは、\ ``None``\ (base UIと同じ場所にあるとみなされます)、もしくはローカルのパス、HTTPのURIのどれかになります。

   .. **New format for this config value**

   **この設定値の新しいフォーマット**

   .. versionadded:: 1.0

   .. A dictionary mapping unique identifiers to a tuple ``(target, inventory)``.
      Each ``target`` is the base URI of a foreign Sphinx documentation set and can
      be a local path or an HTTP URI.  The ``inventory`` indicates where the
      inventory file can be found: it can be ``None`` (at the same location as
      the base URI) or another local or HTTP URI.

   ユニークな識別子をキーにして、 ``(ターゲット, インベントリ)`` というタプルを値に持つ辞書のマッピングです。それぞれの ``ターゲット`` は外部のSphinxのドキュメントを表すベースのURIで、ローカルファイルパスもしくはHTTPのURIを指定できます。 ``インベントリ`` はインベントリファイル(.inv)がある場所を設定します。これに設定できるのは、\ ``None``\ (ベースURIと同じ場所にあるとみなされます)、もしくはローカルのパス、HTTPのURIのどれかになります。

   .. The unique identifier can be used to prefix cross-reference targets, so that
      it is clear which intersphinx set the target belongs to.  A link like
      ``:ref:`comparison manual <python:comparisons>``` will link to the label
      "comparisons" in the doc set "python", if it exists.
   
   ユニークな識別子は、クロスリファレンスのターゲットのプリフィックスとして使用されます。そのため、ターゲットの要素がintersphinxによって設定されたことが明確になります。たとえば、 ``:ref:`比較のマニュアル <python:comparisons>``` という項目があれば、この"comparisons"というラベルは"python"のドキュメントセットの中にあるドキュメントに対してリンクが作成されます。

   .. **Example**

   **サンプル**

   .. To add links to modules and objects in the Python standard library documentation, use:

   Pythonの標準のライブラリドキュメントの中のモジュールやオブジェクトに対してリンクが張りたい場合には次のようにします::

      intersphinx_mapping = {'python': ('http://docs.python.org/', None)}

   .. This will download the corresponding :file:`objects.inv` file from the
      Internet and generate links to the pages under the given URI.  The downloaded
      inventory is cached in the Sphinx environment, so it must be redownloaded
      whenever you do a full rebuild.

   これを設定すると、ソースディレクトリの中の :file:`python.inv` からインベントリー情報を読み込み、 ``http://docs.python.org/`` 以下のページに対するリンクを作成します。ダウンロードされたインベントリ情報はキャッシュされるので、もしもPythonのドキュメントに新しいオブジェクトが追加された場合には、自分でアップデートする必要があります。

   .. A second example, showing the meaning of a non-``None`` value of the second 
      tuple item:

   2番目のサンプルは、2つ目のタプルの要素に ``None`` ではない値を与える場合です::

      intersphinx_mapping = {'python': ('http://docs.python.org/': 
                                        'python-inv.txt')}

   .. This will read the inventory from :file:`python-inv.txt` in the source
      directory, but still generate links to the pages under
      ``http://docs.python.org/``.  It is up to you to update the inventory file as 
      new objects are added to the Python documentation.

   これを設定すると、ソースディレクトリの中の :file:`python-inv.txt` からインベントリー情報を読み込みますが、先ほどの例と同じように ``http://docs.python.org/`` 以下のページに対するリンクを作成します。もしもPythonのドキュメントに新しいオブジェクトが追加された場合には、自分でアップデートする必要があります。







.. confval:: intersphinx_cache_limit

   リモートのインベントリーをキャッシュする最長の日数を設定します。デフォルトは\ ``5``\ で、5日間という意味になります。マイナスの値を設定すると、インベントリーのキャッシュの日数による制限がなくなります。

.. The maximum number of days to cache remote inventories.  The default is
   ``5``, meaning five days.  Set this to a negative value to cache inventories
   for unlimited time.

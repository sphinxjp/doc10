.. :mod:`sphinx.ext.extlinks` -- Markup to shorten external links
   ==============================================================

:mod:`sphinx.ext.extlinks` -- 外部リンクを短縮表記させるマークアップ
=====================================================================

.. module:: sphinx.ext.extlinks
   :synopsis: ベースのURLを持つリンクを簡単に挿入できるようにする。

..   :synopsis: Allow inserting external links with common base URLs easily.
.. moduleauthor:: Georg Brandl

.. versionadded:: 1.0

.. This extension is meant to help with the common pattern of having many external
   links that point to URLs on one and the same site, e.g. links to bug trackers,
   version control web interfaces, or simply subpages in other websites.  It does
   so by providing aliases to base URLs, so that you only need to give the subpage
   name when creating a link.

この拡張を利用すると、同一のウェブサイト内にある多くの外部参照リンクを利用する際に、共通部分をパターン化することができます。例えば、バグトラッカーや、バージョン管理システムのウェブインタフェース、他のウェブサイトの中のサブページなどです。この拡張機能は、ベースとなるURLのエイリアスを提供します。サブのページの名前をつけるだけで、リンクを作成できるようになります。

.. Let's assume that you want to include many links to issues at the Sphinx
   tracker, at :samp:`http://bitbucket.org/birkenfeld/sphinx/issue/{num}`.  Typing
   this URL again and again is tedious, so you can use :mod:`~sphinx.ext.extlinks`
   to avoid repeating yourself.

Sphinxのissueトラッカー上の項目に対して、多くのリンクを作成したいとしましょう。各ページのURLは、 :samp:`http://bitbucket.org/birkenfeld/sphinx/issue/{num}` というURLになります。このURLを何度も何度もタイプするのは疲れますが、 :mod:`~sphinx.ext.extlinks` を使うと、この繰り返し作業から解法されます。

.. The extension adds one new config value:

この拡張は新しい設定値を追加します。:

.. confval:: extlinks

   この設定値は、外部サイト情報を持つ辞書になります。ユニークな短いエイリアス名をキーに持ち、 ベースのURLと *prefix* を値に持ちます。例えば、上記で挙げたissueトラッカーを表現する場合には、次のように設定します:

   .. code-block:: python

      extlinks = {'issue': ('http://bitbucket.org/birkenfeld/sphinx/issue/%s',
                            'issue ')}

   このような設定をすると、 ``:issue:`123``` というように、エイリアス名をロールとして使用できます。このロールには http://bitbucket.org/birkenfeld/sphinx/issue/123 へのリンクが挿入されます。見て分かるように、ロールで与えられたターゲットは、ベースURLの ``%s`` に置き換えられます。

   リンクの *キャプション* は、タプルの2つ目の要素の *prefix* によって表記が異なります。

   - もし *prefix* が ``None`` であれば、リンクのキャプションは完全なURLになります。
   - もし *prefix* が空文字列であれば、リンクのキャプションはロールのターゲットの中身の、URLの一部になります。この例では ``123`` になります。
   - もし *prefix* に空でない文字列が指定されたら、 *prefix* + ロールのターゲットになります。上記の例であれば、 ``issue 123`` となります。

   他の相互リンクのためのロールのように、 ``:issue:`この問題 <123>``` という、明示的な名前を指定する書き方も使うことができます。この場合、 *prefix* は利用されません。

.. This config value must be a dictionary of external sites, mapping unique
   short alias names to a base URL and a *prefix*.  For example, to create an
   alias for the above mentioned issues, you would add ::

      extlinks = {'issue': ('http://bitbucket.org/birkenfeld/sphinx/issue/%s',
                            'issue ')}

   Now, you can use the alias name as a new role, e.g. ``:issue:`123```.  This
   then inserts a link to http://bitbucket.org/birkenfeld/sphinx/issue/123.
   As you can see, the target given in the role is substituted in the base URL
   in the place of ``%s``.

   The link *caption* depends on the second item in the tuple, the *prefix*:

   - If the prefix is ``None``, the link caption is the full URL.
   - If the prefix is the empty string, the link caption is the partial URL
     given in the role content (``123`` in this case.)
   - If the prefix is a non-empty string, the link caption is the partial URL,
     prepended by the prefix -- in the above example, the link caption would be
     ``issue 123``.

   You can also use the usual "explicit title" syntax supported by other roles
   that generate links, i.e. ``:issue:`this issue <123>```.  In this case, the
   *prefix* is not relevant.   

.. note

   Since links are generated from the role in the reading stage, they appear as
   ordinary links to e.g. the ``linkcheck`` builder.

.. note::

   読み込み段階でロールからリンクが生成されるため、 ``linkcheck`` ビルダーなどでは通常のリンクとして扱われます。
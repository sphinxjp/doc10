.. highlight:: rest

.. _code-examples:

.. Showing code examples
.. ---------------------

コードサンプルの表示
--------------------

.. index:: pair: code; examples
           single: sourcecode

.. Examples of Python source code or interactive sessions are represented using standard reST literal blocks.  They are started by a ``::`` at the end of the preceding paragraph and delimited by indentation.

Pythonのソースコードや、インタラクティブモードのセッションを表現するのには、標準のreSTのリテラルブロックを使用します。リテラルブロックは前の段落の末尾を ``::`` にして、インデントにすることで開始されます。

.. Representing an interactive session requires including the prompts and output along with the Python code.  No special markup is required for interactive sessions.  After the last line of input or output presented, there should not be an "unused" primary prompt; this is an example of what *not* to do

インタラクティブセッションの表現には、プロンプトと、Pythonコードが表示する出力も含める必要があります。インタラクティブセッション用の特別なマークアップはありません。最後の行の後、もしくは出力を書いているところには、"未使用の"プロンプトは置いてはいけません。下記の例は *しないほうがいいもの* の例です。::

   >>> 1 + 1
   2
   >>>

.. Syntax highlighting is done with `Pygments <http://pygments.org>`_ (if it's installed) and handled in a smart way

シンタックスハイライトは、もしインストールされていれば `Pygments <http://pygments.org>`_ を使ってスマートに行われます。

.. * There is a "highlighting language" for each source file.  Per default, this is ``'python'`` as the majority of files will have to highlight Python snippets, but the doc-wide default can be set with the :confval:`highlight_language` config value.

* ソースファイルごとに"ハイライトする言語"があります。一番ハイライトされる言語として多いのはPythonのコード片なので、デフォルトでは ``'python'`` として処理するようになっています。ドキュメント全体のデフォルトの設定は :confval:`highlight_language` で設定することができます。

.. * Within Python highlighting mode, interactive sessions are recognized
..   automatically and highlighted appropriately.  Normal Python code is only
..   highlighted if it is parseable (so you can use Python as the default, but
..   interspersed snippets of shell commands or other code blocks will not be
..   highlighted as Python).

* Pythonハイライトモードではインタラクティブモードも自動で識別され、適切にハイライトされます。通常のPythonコードはパース可能であればきちんとハイライトされます。しかし、シェルコマンドや他のコードブロックの部分的なコード片はPythonとして処理できないこともあります。

.. * The highlighting language can be changed using the ``highlight`` directive,
..   used as follows::

..     .. highlight:: c

..  This language is used until the next ``highlight`` directive is encountered.

* ハイライト言語は ``highlight`` ディレクティブを以下のようにして変更することができます::

    .. highlight:: c

  ここで設定された言語は、次に ``highlight`` ディレクティブが実行されるまで有効です。

.. * For documents that have to show snippets in different languages, there's also 
     a :rst:dir:`code-block` directive that is given the highlighting language directly::

     .. code-block:: ruby

        Some Ruby code.

     The directive's alias name :rst:dir:`sourcecode` works as well.

* 様々な言語のコード片がドキュメント中に登場する場合には、 :rst:dir:`code-block` ディレクティブを使用すると、その場でハイライトしたい言語を与えることができます::

    .. code-block:: ruby

       Rubyのプログラム

  このディレクティブのエイリアスの :rst:dir:`sourcecode` も同じように動作します。

.. * The valid values for the highlighting language are:

    * ``none`` (no highlighting)
    * ``python`` (the default when :confval:`highlight_language` isn't set)
    * ``guess`` (let Pygments guess the lexer based on contents, only works with
      certain well-recognizable languages)
    * ``rest``
    * ``c``
    * ... and any other lexer name that Pygments supports.

* ハイライトする言語として適切な値は以下の通りです:

  * ``none`` (ハイライトしない)
  * ``python`` ( :confval:`highlight_language` が設定されていない時のデフォルト)
  * ``guess`` (Pygmentsに推測させます。推測しやすい言語でないとうまく動作しません)
  * ``rest``
  * ``c``
  * ... など、Pygmentsがサポートしているすべての言語

.. * If highlighting with the selected language fails, the block is not highlighted in any way.

* 選択された言語によるハイライトがうまくいかなかった場合には、そのブロックはハイライトされなくなります。

.. Line numbers
.. ^^^^^^^^^^^^

行番号
^^^^^^

.. If installed, Pygments can generate line numbers for code blocks.  For 
   automatically-highlighted blocks (those started by ``::``), line numbers must be 
   switched on in a :rst:dir:`highlight` directive, with the ``linenothreshold`` option:

もしインストールされていれば、Pygmentsはコードブロックに対して行番号を発生させることができます。自動ハイライトブロック( ``::`` で開始されるもの)を使用している場合には、 :rst:dir:`highlight` ディレクティブの中で、 ``linenothreshold`` オプションを使って機能を有効にする必要があります::

   .. highlight:: python
      :linenothreshold: 5

.. This will produce line numbers for all code blocks longer than five lines.

この設定では5行以上あるコードブロックのすべてに対して、行番号が生成されるようになります。

.. For :rst:dir:`code-block` blocks, a ``linenos`` flag option can be given to switch 
   on line numbers for the individual block::

:rst:dir:`code-block` ブロックを使用している場合には、 ``linenos`` フラグオプションを使用すると、個別のブロックの行番号表示を有効にできます::

   .. code-block:: ruby
      :linenos:

      Rubyのコード

..      Some more Ruby code.


.. Includes
.. ^^^^^^^^

インクルード
^^^^^^^^^^^^

..
   .. rst:directive:: .. literalinclude:: filename

.. rst:directive:: .. literalinclude:: ファイル名

   .. Longer displays of verbatim text may be included by storing the example text in 
      an external file containing only plain text.  The file may be included using the 
      ``literalinclude`` directive. [1]_ For example, to include the Python source file
      :file:`example.py`, use::

         .. literalinclude:: example.py

   プレーンテキスト形式で外部ファイルとして保存指定あるサンプルのテキストを引用して表示することもできます。長いソースコードを正確にそのまま表示したい場合に便利です。ファイルをインクルードするには、 ``literalinclude`` ディレクティブを使用します。 [1]_ 例えば、 :file:`example.py` というPythonソースコードをインクルードするには以下のようにします::

      .. literalinclude:: example.py

   .. The file name is usually relative to the current file's path.  However, if it 
      is absolute (starting with ``/``), it is relative to the top source 
      directory.

   ソースコードのファイルは通常、現在のパスからの相対パスで指定します。 ``/`` から開始されているときはトップのソースディレクトリからのパス指定をすることができます。

   .. Tabs in the input are expanded if you give a ``tab-width`` option with the
      desired tab width.

   ``tab-width`` オプションを指定すると、入力ファイル中のタブを希望の幅に展開することができます。

   .. The directive also supports the ``linenos`` flag option to switch on line 
      numbers, and a ``language`` option to select a language different from the 
      current file's standard language.  Example with options:

   このディレクティブでも、 ``linenos`` フラッグオプションを利用して、行番号表示を有効にすることができます。また、 ``language`` オプションを使うと、ファイルの標準の言語と違う言語を選択することができます。オプションのサンプルを示します::

      .. literalinclude:: example.rb
         :language: ruby
         :linenos:

   .. Include files are assumed to be encoded in the :confval:`source_encoding`. 
      If the file has a different encoding, you can specify it with the 
      ``encoding`` option::

   読み込むファイルは :confval:`source_incodeing` で設定されているエンコードで保存されているものとして処理されます。もし違うエンコーディングのファイルを読み込む場合には ``encoding`` オプションで設定することができます::

      .. literalinclude:: example.py
         :encoding: latin-1

   .. The directive also supports including only parts of the file.  If it is a
      Python module, you can select a class, function or method to include using
      the ``pyobject`` option::

   このディレクティブは、ファイル全体ではなく、一部分だけを読み込むこともサポートしています。もしPythonモジュールの場合には、 ``pyobject`` オプションを使用してクラス、関数、メソッドの単位でインクルードすることもできます::

      .. literalinclude:: example.py
         :pyobject: Timer.start

   .. This would only include the code lines belonging to the ``start()`` method in 
      the ``Timer`` class within the file.

   上記のサンプルを書くと、指定されたファイルに含まれる、 ``Timer`` クラスの ``start()`` メソッドに属するコード行だけがドキュメントに挿入されます。

   .. Alternately, you can specify exactly which lines to include by giving a
      ``lines`` option::

   これとは別に、 ``lines`` オプションを使って行番号を正確に指定することでも部分的なインクルードを行うことができます::

      .. literalinclude:: example.py
         :lines: 1,3,5-10,20-

   .. This includes the lines 1, 3, 5 to 10 and lines 20 to the last line.

   このサンプルはでは、指定されたファイルの 1行目, 3行目, 5〜10行目, そして20行目から最終行までのコードがインクルードされます。

   .. Another way to control which part of the file is included is to use the
      ``start-after`` and ``end-before`` options (or only one of them).  If
      ``start-after`` is given as a string option, only lines that follow the first 
      line containing that string are included.  If ``end-before`` is given as a 
      string option, only lines that precede the first lines containing that string 
      are included.

   どのパートをインクルードするか、というのを制御する別の方法としては、 ``start-after``, ``end-before`` オプションの両方、もしくはどちらか一方を使うものがあります。 もしスタートのオプションとして ``start-after`` にオプションとして文字列が指定されると、その文字列を含む行から始まるコードがインクルードされます。 ``end-before`` にオプションとして文字列が指定されると、指定された文字列が含まれる行の前の部分がインクルードされます。

   .. You can prepend and/or append a line to the included code, using the
      ``prepend`` and ``append`` option, respectively.  This is useful e.g. for
      highlighting PHP code that doesn't include the ``<?php``/``?>`` markers.

   ``prepend``, ``append`` オプションを使用すると、読み込まれた行の前後にコード行を追加することができます。例えば、 ``<?php``/``?>`` マーカーを含まないPHPコードをハイライトする際などに役立ちます。

   .. 
      .. versionadded:: 0.4.3
         The ``encoding`` option.
      .. versionadded:: 0.6
         The ``pyobject``, ``lines``, ``start-after`` and ``end-before`` options,
         as well as support for absolute filenames.
      .. versionadded:: 1.0
         The ``prepend`` and ``append`` options, as well as ``tab-width``.

   .. versionadded:: 0.4.3
      ``encoding`` オプション
   .. versionadded:: 0.6
      ``pyobject``, ``lines``, ``start-after``, ``end-before`` オプションと、プロジェクトのルートからの絶対パス指定
   .. versionadded:: 1.0
      ``prepend``, ``append``, ``tab-width``


.. .. rubric:: Footnotes

   .. [1] There is a standard ``.. include`` directive, but it raises errors if the
          file is not found.  This one only emits a warning.

.. rubric:: 脚注

.. [1] 標準の ``.. include`` ディレクティブは、ファイルがないときにはエラーが発生しますが、こちらの方は警告を出力します。

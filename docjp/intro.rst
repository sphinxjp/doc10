.. Introduction
.. ============

イントロダクション
==================

.. This is the documentation for the Sphinx documentation builder.  Sphinx is a 
   tool that translates a set of reStructuredText_ source files into various output
   formats, automatically producing cross-references, indices etc.  That is, if 
   you have a directory containing a bunch of reST-formatted documents (and 
   possibly subdirectories of docs in there as well), Sphinx can generate a 
   nicely-organized arrangement of HTML files (in some other directory) for easy 
   browsing and navigation.  But from the same source, it can also generate a 
   LaTeX file that you can compile into a PDF version of the documents, or a
   PDF file directly using `rst2pdf <http://rst2pdf.googlecode.com>`_.


これはSphinxドキュメンテーションビルダーのドキュメントです。Sphinxは一連の reStructuredText_ (以下reST)のソースファイルを様々な出力形式に変換したり、クロスリファレンスやインデックスなどを自動生成するツールです。これは、もしreSTフォーマットのドキュメント群が含まれるディレクトリがあったとしたら、Sphinxはそこから非常によくまとまった配置のHTMLファイル群を生成することができるということを意味しています。サブディレクトリにソースが分かれていても問題はありません。また、結果のHTMLはブラウザで簡単に見たり、ナビゲーションもしっかりしたものになります。それだけではなく、同じソースファイルから、同様にLaTeXファイルも出力することができ、これをコンパイルすることでPDFバージョンのドキュメントも生成することができますし、 `rst2pdf <http://rst2pdf.googlecode.com>`_ を使用すると、直接PDFファイルを生成することもできます。

.. The focus is on hand-written documentation, rather than auto-generated API docs.
   Though there is limited support for that kind of docs as well (which is intendedto be 
   freely mixed with hand-written content), if you need pure API docs have alook 
   at `Epydoc <http://epydoc.sf.net/>`_, which also understands reST.

このドキュメントでは、自動生成のAPIのドキュメントではなく、手で作成するドキュメンテーションにフォーカスします。そのようなドキュメントのサポートに関してはまだ限定的にはあります(手で作成するコンテンツも自由に追加できるようにする予定)が、もし純粋なAPIドキュメントが必要であれば、 `Epydoc <http://epydoc.sf.net/>`_ をご覧ください。こちらもreSTを解釈することができます。

.. Conversion from other systems
.. -----------------------------

他のシステムからの変換
----------------------

.. This section is intended to collect helpful hints for those wanting to migrate 
   to reStructuredText/Sphinx from other documentation systems.

このセクションでは、他のドキュメントシステムからreStructuredText/Sphinxへの移行を考えている人達へのヒントを集めています。

.. * Gerard Flanagan has written a script to convert pure HTML to reST; it can be 
     found at `BitBucket 
     <http://bitbucket.org/djerdo/musette/src/tip/musette/html/html2rest.py>`_.

* Gerard FlanaganはHTMLからreSTに変換するスクリプトを作成しました。スクリプトは `BitBucket <http://bitbucket.org/djerdo/musette/src/tip/musette/html/html2rest.py>`_ 上で見つけることができます。

.. * For converting the old Python docs to Sphinx, a converter was written which  
     can be found at `the Python SVN repository  
     <http://svn.python.org/projects/doctools/converter>`_.  It contains generic  
     code to convert Python-doc-style LaTeX markup to Sphinx reST.

* 古いPythonのドキュメントをSphinxにコンバートするには、専用のコンバート用のツールを `PythonのSVNリポジトリ <http://svn.python.org/projects/doctools/converter>`_ で見つけることができます。これを使えば、Python-docスタイルのLaTeXのマークアップをSphinx reSTに変換できます。

.. * Marcin Wojdyr has written a script to convert Docbook to reST with Sphinx
     markup; it is at `Google Code <http://code.google.com/p/db2rst/>`_.

* Marcin WojdyrはDocbookをreST＋Sphinxマークアップに変換するスクリプトを作成しました。 `Google Code <http://code.google.com/p/db2rst/>`_ にあります。

.. Use with other systems
   ----------------------

他のシステムと併用
------------------

.. See the :ref:`pertinent section in the FAQ list <usingwith>`.

:ref:`FAQの中の関連のリスト <usingwith>` を参照してください。


.. Prerequisites
.. -------------

前提条件
--------

.. Sphinx needs at least **Python 2.4** to run.  If you like to have source code 
   highlighting support, you must also install the Pygments_ library, which you can 
   do via setuptools' easy_install.  Sphinx should work with docutils version 0.4 
   or some (not broken) SVN trunk snapshot.

Sphinxの実行には **Python 2.4** よりも新しいバージョンのPythonが必要です。もしもソースコードハイライトのサポートが必要であれば、 Pygments_ ライブラリも一緒にインストールする必要がありますが、 setuptoolsのeasy_installを使用すれば一緒にインストールできます。Sphinxが依存しているコンポーネントとしては、docutilsのバージョン 0.4、もしくはSVNリポジトリのTrunkのスナップショット(壊れていないものに限定)があります。

.. _Pygments: http://pygments.org
.. _reStructuredText: http://docutils.sf.net/rst.html

.. Usage
   -----

使用方法
--------

.. See :doc:`tutorial` for an introduction.  It also contains links to more
   advanced sections in this manual for the topics it discusses.

導入の説明にあたっては、 :doc:`tutorial` を参照してください。このドキュメントには、説明しているそれぞれの内容に対して、発展的な内容を説明しているセクションへのリンクが含まれています。

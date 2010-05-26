
.. Writing new builders
   ====================

.. _writing-builders:

新しいビルダーを作成する
========================

.. todo:: Expand this.

.. currentmodule:: sphinx.builders

.. class:: Builder

   .. This is the base class for all builders.

   このクラスはすべてのビルダーのベースクラスです。

   .. These methods are predefined and will be called from the application:

   これらのメソッドは事前に定義されており、アプリケーションから呼び出されます。

   .. method:: get_relative_uri(from_, to, typ=None)

      .. Return a relative URI between two source filenames. May raise environment.
         NoUri if there’s no way to return a sensible URI.

      2つのソースファイル間の相対URIを返します。URIを返す方法がない場合には、 environment.NoUri 例外を投げる場合があります。

   .. method:: build_all

      .. Build all source files.

      すべてのソースファイルをビルドします。

   .. method:: build_specific(filenames)

      .. Only rebuild as much as needed for changes in the filenames.

      オプションで指定されたファイル名のリストに含まれる、変更が必要なものだけ再ビルドします。
      
   .. method:: build_update

      .. Only rebuild what was changed or added since last build.

      最後のビルドの後に変更されたり、追加されたものだけ再ビルドします。

   .. method:: build(docnames, summary=None, method='update')

      .. Main build method. First updates the environment, and then calls write().

      メインのビルド用メソッドです。最初に環境をアップデートしてから, write() を呼びます。

   .. These methods can be overridden in concrete builder classes:

   これらのメソッドは派生されたビルダークラス側でオーバーライドすることができます:

   .. method:: init

      .. Load necessary templates and perform initialization.  
         The default implementation does nothing.

      必要なテンプレートをロードしたり、初期化を行うためのメソッドです。
      デフォルトの実装では、何も行いません。

   .. method:: get_outdated_docs

      .. Return an iterable of output files that are outdated, or a string 
         describing what an update build will build.

         If the builder does not output individual files corresponding to source 
         files, return a string here. If it does, return an iterable of those 
         files that need to be written.

      ビルドが必要な、古いファイルを返すイテレータを返します。言い換えると、アップデートビルドを行うと、何がビルドされるか、というのを説明する文字列を返します。

      もしもビルダーがソースファイルに関連する、個別のファイルを出力しない場合には、ここでは文字列を返してください。その場合には、書かれるべきファイルのイテレータを返します。

   .. method:: get_target_uri(docname, typ=None)

      .. Return the target URI for a document name (typ can be used to 
         qualify the link characteristic for individual builders).

      ドキュメント名に関連する、対象のURLを返します。

      typはそれぞれのビルダーごとのリンクの修飾子として使うことができます。

   .. method:: prepare_writing(docnames)

   .. method:: write_doc(docname, doctree)

   .. method:: finish

      .. Finish the building process. The default implementation does nothing.

      ビルドプロセスの終了です。デフォルトの実装では何も呼び出されません。

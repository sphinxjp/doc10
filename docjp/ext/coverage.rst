
.. :mod:`sphinx.ext.coverage` -- Collect doc coverage stats
   
:mod:`sphinx.ext.coverage` -- ドキュメントのカバレッジの状況を収集します
========================================================================

.. module:: sphinx.ext.coverage
   :synopsis: PythonモジュールとC言語のAPIのドキュメント内のカバレッジを収集します

..   :synopsis: Check Python modules and C API for coverage in the documentation.

.. This extension features one additional builder, the :class:`CoverageBuilder`.

この拡張機能には :class:`CoverageBuilder` という追加のビルダーが一つ含まれます。

.. class:: CoverageBuilder

   このビルダーを使用するには、coverage拡張を設定ファイルに登録して使用できるようにしたあとで、コマンドラインのオプションとして ``-b coverage`` を渡してください。

.. To use this builder, activate the coverage extension in your configuration
   file and give ``-b coverage`` on the command line.

.. todo:: Write this section.


.. Several new configuration values can be used to specify what the builder
   should check:

ビルダーがチェックすべきものを決定するための、いくつかの新しい設定値も追加されます:

.. confval:: coverage_ignore_modules

.. confval:: coverage_ignore_functions

.. confval:: coverage_ignore_classes

.. confval:: coverage_c_path

.. confval:: coverage_c_regexes

.. confval:: coverage_ignore_c_items

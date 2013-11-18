autex
========
texとかなんやかんやのコンパイルを自動化するためのスクリプトです。

Preparation
-----------------
任意のディレクトリでファイルが変更されたらそれをトリガーにしてなんかコマンドを実行するみたいなそんなやつです。
まずは準備をしましょう。

.. code-block:: bash

    $ cd /path/to/directory/that/in/your/PATH
    $ ln -s /path/to/autex.py autex

とかしとくとよい気がします。

Example Usage
-----------------

.. code-block:: bash

    $ cd /path/to/project/directory
    $ autex .

これで拡張子に.texとつくファイルが変更もしくは作成されたタイミングでmakeコマンドが実行されます．

実行コマンドを指定したい場合は

.. code-block:: bash

    $ autex . -c "the command that you wanna do"

もしくは

.. code-block:: bash

    $ autex . --cmd "the command that you wanna do"

としましょう。

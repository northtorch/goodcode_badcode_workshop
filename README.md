# NorthTorch株式会社 社内勉強会用「Good Code, Bad Code ～持続可能な開発のためのソフトウェアエンジニア的思考」を読む ワークショップ用ソースコード

## 動作環境

- WSL2での動作を想定
- Python 3.11.3
- pyenvインストール済み
- poetryインストール済み
- vscodeをインストール済み

## ディレクトリ構成

話題ごとにディレクトリを作成し、ワークショップのベースコードを格納している

| ディレクトリ名 | 内容 | 備考 |
| :-- | :-- | :-- | 
| 02_01_abstraction_layer | 第２章 抽象化レイヤー | |
| 03_01_state_and_mutability | 第３章 状態と可変性 | |
| 06_01_magic_value | 第６章 マジックバリュー | |
| 06_02_unexpected_side_effect | 第６章 予期せぬ副作用 | |
| 06_03_changing_input_parameters | 第６章 入力パラメータの変更 | |
| 07_01_mutability | 第７章 可変性のバグ | |
| 07_02_general_purpose_type | 第７章 汎用的なデータ型 | |

## 動作環境作成手順

1. MeCabのインストール

    ```
    $ sudo apt-get install mecab mecab-ipadic-utf8 libmecab-dev swig
    $ sudo cp /etc/mecabrc /usr/local/etc/
    ```

1. リポジトリをクローンする

    ```
    $ git clone https://github.com/northtorch/goodcode_badcode_workshop.git
    ```

1. 環境セットアップスクリプトを実行する

    ```
    $ cd goodcode_badcode_workshop
    $ bash make_develop_env.sh
    ```

1. vscodeでルートディレクトリを開く


    ```
    $ code .
    ```
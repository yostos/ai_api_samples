# AI APIサンプルプログラム

このリポジトリには、OpenAIのGPT-4とAnthropicのClaude 3.5 Sonnetを使用したAI APIサンプルプログラムが含まれています。

## 目次

1. [必要条件](#必要条件)
2. [セットアップ](#セットアップ)
3. [サンプルプログラム](#サンプルプログラム)
4. [依存関係管理](#依存関係管理)
5. [使用方法](#使用方法)
6. [注意事項](#注意事項)
7. [ライセンス](#ライセンス)
8. [貢献](#貢献)

## 必要条件

- Python 3.9以上
- pip または Poetry

## セットアップ

1. このリポジトリをクローンまたはダウンロードします。
2. 仮想環境を作成します：
   ```
   python -m venv venv
   source venv/bin/activate  # Linuxまたは macOS
   venv\Scripts\activate  # Windows
   ```
3. 依存関係をインストールします（[依存関係管理](#依存関係管理)セクションを参照）。
4. `.env`ファイルをプロジェクトのルートディレクトリに作成し、APIキーを設定します：
   ```
   OPENAI_API_KEY=あなたのOpenAI APIキー
   ANTHROPIC_API_KEY=あなたのAnthropic APIキー
   ```

## サンプルプログラム

このリポジトリには2つのサンプルプログラムが含まれています：

1. `openai-sample.py`: OpenAI GPT-4 APIを使用
2. `claude3-sample.py`: Anthropic Claude 3.5 Sonnet APIを使用

両プログラムとも、NTPサーバー（ntp.nict.jp）から現在時刻を取得するPythonプログラムを生成します。

## 依存関係管理

`requirements.txt`と`pyproject.toml`の両方を提供しています。お好みのツールを選択してください。

### pipを使用する場合（requirements.txt）

```
pip install -r requirements.txt
```

### Poetryを使用する場合（pyproject.toml）

```
poetry install
```

注: Poetryが未インストールの場合は、[Poetry公式サイト](https://python-poetry.org/docs/#installation)を参照してください。

## 使用方法

1. 仮想環境がアクティブであることを確認します。
2. サンプルプログラムを実行：
   ```
   python openai-sample.py
   # または
   python claude3-sample.py
   ```

## 注意事項

これらのスクリプトはデモンストレーション目的です。本番環境での使用には、追加のエラー処理や最適化が必要な場合があります。常に各APIの最新のドキュメントを参照してください。

## ライセンス

[MITライセンス](LICENSE)

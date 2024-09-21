import anthropic
import os
from dotenv import load_dotenv

# .envファイルから環境変数をロード
load_dotenv(os.path.expanduser("~/.env"))

# Anthropic APIのキーを取得
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

# APIキーが取得できなかった場合の処理
if anthropic_api_key is None:
    raise ValueError(
        "Anthropic APIキーが環境変数 'ANTHROPIC_API_KEY' に設定されていません。"
    )

# Anthropic APIのキーを設定
client = anthropic.Anthropic(api_key=anthropic_api_key)


def format_ai_message(ai_response):
    # AIからのメッセージを扱いやすいように加工します
    if isinstance(ai_response, list):
        # リストの場合、テキストを結合
        ai_response = " ".join(ai_response)

    formatted_message = ai_response.replace("[TextBlock(text='", "").replace(
        "', type='text')]", ""
    )
    formatted_message = formatted_message.replace("\\n", "\n")
    return formatted_message


# Anthropicの APIを呼び出して、応答を取得
message = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=1024,
    temperature=0,
    system="あなたは優秀なPythonのエンジニアです。",
    messages=[
        {
            "role": "user",
            "content": "NTPサーバーから現在時間を取得し表示するプログラムを作成してください。サーバーのアドレスはntp.nict.jpです。",
        }
    ],
)

# message.contentのデータ形式を確認
if isinstance(message.content, list):
    # リストの場合は、結合して1つの文字列に
    content = " ".join(
        [
            msg["text"] if isinstance(msg, dict) and "text" in msg else str(msg)
            for msg in message.content
        ]
    )
else:
    content = message.content  # 文字列の場合はそのまま使用

# フォーマットを適用
answer = format_ai_message(content)

# 結果を表示
print(answer)

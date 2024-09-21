from openai import OpenAI

import os
from dotenv import load_dotenv

# .envファイルから環境変数をロード
load_dotenv(os.path.expanduser("~/.env"))

# OpenAI APIのキーを取得
openai_api_key = os.getenv("OPENAI_API_KEY")

# APIキーが取得できなかった場合の処理
if openai_api_key is None:
    raise ValueError("OpenAI APIキーが環境変数 'OPENAI_API_KEY' に設定されていません。")

# OpenAI APIのキーを設定

client = OpenAI(api_key=openai_api_key)


def format_ai_message(ai_response):
    # AIからのメッセージを扱いやすいように加工します
    formatted_message = ai_response.replace("[TextBlock(text='", "").replace(
        "', type='text')]", ""
    )
    formatted_message = formatted_message.replace("\\n", "\n")
    return formatted_message


# GPT-4 APIを呼び出して、応答を取得
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "あなたは優秀なPythonのエンジニアです。"},
        {
            "role": "user",
            "content": "NTPサーバーから現在時間を取得し表示するプログラムを作成してください。サーバーのアドレスはntp.nict.jpです。",
        },
    ],
    max_tokens=1024,
    temperature=0,
)

# APIからの応答を取得
message_content = response.choices[0].message.content

# フォーマットを適用
answer = format_ai_message(message_content)

# 結果を表示
print(answer)

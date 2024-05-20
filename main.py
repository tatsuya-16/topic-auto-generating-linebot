import os
import base64
import urllib.request
import json
import requests
import openai
from dotenv import load_dotenv

# .envファイルの内容を読み込む
load_dotenv()

from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)

# DBアクセスここから

DOMAIN = os.getenv('DB_DOMAIN')## ドメイン　自環境のものを入れる
LOGIN = os.getenv('DB_LOGIN_ID')## ログイン名　自環境のものを入れる
PASS = os.getenv('DB_LOGIN_PASS')## パス　自環境のものを入れる
appno = 2## 取得したいアプリのアプリNo
record_no = 1## 取得したいレコードのレコード番号
uri = "https://" + DOMAIN + ".cybozu.com/k/v1/record.json"
AUTH = base64.b64encode((LOGIN + ":" + PASS).encode())
## ヘッダ作成
headers = {
    "Host":DOMAIN + ".cybozu.com:443",
    "X-Cybozu-Authorization":AUTH,
    "Content-Type": "application/json",
}
## body作成
body = {
    "app":appno,
    "id":record_no
}
## リクエスト作成
req = urllib.request.Request(
            url=uri, ## url
            data=json.dumps(body).encode(), ## body 
            headers=headers, ## header
            method="GET", ## GET
            )
## リクエスト送信　結果受け取り
try:
    response = urllib.request.urlopen(req)
except urllib.error.URLError as e:## エラーが生じた場合は補足する
    # https://docs.python.org/ja/3/howto/urllib2.html tryの参考
        if hasattr(e, "reason"):
            res_error = (
                "We failed to reach a server." + "\n" +
                "Reason: " + e.reason + "\n"
            )
            print(res_error)
        elif hasattr(e, 'code'):
            res_error = (
                'The server couldn\'t fulfill the request.' + "\n" +
                'Error code: ', e.code + "\n"
            )
            print(res_error)
else:
    res_dict = json.load(response)
    print(res_dict)
# 送られてきたデータから必要な情報を取得して新しい変数に格納する
age_A = res_dict['record']['年齢']['value']
birthplace_A = res_dict['record']['出身地域']['value']
residence_A = res_dict['record']['居住地域']['value']
hobby_A = res_dict['record']['趣味']['value']
 
# 取得した情報を確認する
print("年齢:", age_A)
print("出身地域:", birthplace_A)
print("居住地域:", residence_A)
print("趣味:", hobby_A)
 
DOMAIN = os.getenv('DB_DOMAIN')## ドメイン　自環境のものを入れる
LOGIN = os.getenv('DB_LOGIN_ID')## ログイン名　自環境のものを入れる
PASS = os.getenv('DB_LOGIN_PASS')## パス　自環境のものを入れる
appno = 2## 取得したいアプリのアプリNo
record_no = 4## 取得したいレコードのレコード番号
uri = "https://" + DOMAIN + ".cybozu.com/k/v1/record.json"
AUTH = base64.b64encode((LOGIN + ":" + PASS).encode())
## ヘッダ作成
headers = {
    "Host":DOMAIN + ".cybozu.com:443",
    "X-Cybozu-Authorization":AUTH,
    "Content-Type": "application/json",
}
## body作成
body = {
    "app":appno,
    "id":record_no
}
## リクエスト作成
req = urllib.request.Request(
            url=uri, ## url
            data=json.dumps(body).encode(), ## body 
            headers=headers, ## header
            method="GET", ## GET
            )
## リクエスト送信　結果受け取り
try:
    response = urllib.request.urlopen(req)
except urllib.error.URLError as e:## エラーが生じた場合は補足する
    # https://docs.python.org/ja/3/howto/urllib2.html tryの参考
        if hasattr(e, "reason"):
            res_error = (
                "We failed to reach a server." + "\n" +
                "Reason: " + e.reason + "\n"
            )
            print(res_error)
        elif hasattr(e, 'code'):
            res_error = (
                'The server couldn\'t fulfill the request.' + "\n" +
                'Error code: ', e.code + "\n"
            )
            print(res_error)
else:
    res_dict = json.load(response)
    print(res_dict)
# 送られてきたデータから必要な情報を取得して新しい変数に格納する
age_B = res_dict['record']['年齢']['value']
birthplace_B = res_dict['record']['出身地域']['value']
residence_B = res_dict['record']['居住地域']['value']
hobby_B = res_dict['record']['趣味']['value']
 
# 取得した情報を確認する
print("年齢:", age_B)
print("出身地域:", birthplace_B)
print("居住地域:", residence_B)
print("趣味:", hobby_B)
 
DOMAIN = os.getenv('DB_DOMAIN')## ドメイン　自環境のものを入れる
LOGIN = os.getenv('DB_LOGIN_ID')## ログイン名　自環境のものを入れる
PASS = os.getenv('DB_LOGIN_PASS')## パス　自環境のものを入れる
appno = 2## 取得したいアプリのアプリNo
record_no = 5## 取得したいレコードのレコード番号
uri = "https://" + DOMAIN + ".cybozu.com/k/v1/record.json"
AUTH = base64.b64encode((LOGIN + ":" + PASS).encode())
## ヘッダ作成
headers = {
    "Host":DOMAIN + ".cybozu.com:443",
    "X-Cybozu-Authorization":AUTH,
    "Content-Type": "application/json",
}
## body作成
body = {
    "app":appno,
    "id":record_no
}
## リクエスト作成
req = urllib.request.Request(
            url=uri, ## url
            data=json.dumps(body).encode(), ## body 
            headers=headers, ## header
            method="GET", ## GET
            )
## リクエスト送信　結果受け取り
try:
    response = urllib.request.urlopen(req)
except urllib.error.URLError as e:## エラーが生じた場合は補足する
    # https://docs.python.org/ja/3/howto/urllib2.html tryの参考
        if hasattr(e, "reason"):
            res_error = (
                "We failed to reach a server." + "\n" +
                "Reason: " + e.reason + "\n"
            )
            print(res_error)
        elif hasattr(e, 'code'):
            res_error = (
                'The server couldn\'t fulfill the request.' + "\n" +
                'Error code: ', e.code + "\n"
            )
            print(res_error)
else:
    res_dict = json.load(response)
    print(res_dict)
# 送られてきたデータから必要な情報を取得して新しい変数に格納する
age_C = res_dict['record']['年齢']['value']
birthplace_C = res_dict['record']['出身地域']['value']
residence_C = res_dict['record']['居住地域']['value']
hobby_C = res_dict['record']['趣味']['value']
 
# 取得した情報を確認する
print("年齢:", age_C)
print("出身地域:", birthplace_C)
print("居住地域:", residence_C)
print("趣味:", hobby_C)
 
DOMAIN = os.getenv('DB_DOMAIN')## ドメイン　自環境のものを入れる
LOGIN = os.getenv('DB_LOGIN_ID')## ログイン名　自環境のものを入れる
PASS = os.getenv('DB_LOGIN_PASS')## パス　自環境のものを入れる
appno = 2## 取得したいアプリのアプリNo
record_no = 6## 取得したいレコードのレコード番号
uri = "https://" + DOMAIN + ".cybozu.com/k/v1/record.json"
AUTH = base64.b64encode((LOGIN + ":" + PASS).encode())
## ヘッダ作成
headers = {
    "Host":DOMAIN + ".cybozu.com:443",
    "X-Cybozu-Authorization":AUTH,
    "Content-Type": "application/json",
}
## body作成
body = {
    "app":appno,
    "id":record_no
}
## リクエスト作成
req = urllib.request.Request(
            url=uri, ## url
            data=json.dumps(body).encode(), ## body 
            headers=headers, ## header
            method="GET", ## GET
            )
## リクエスト送信　結果受け取り
try:
    response = urllib.request.urlopen(req)
except urllib.error.URLError as e:## エラーが生じた場合は補足する
    # https://docs.python.org/ja/3/howto/urllib2.html tryの参考
        if hasattr(e, "reason"):
            res_error = (
                "We failed to reach a server." + "\n" +
                "Reason: " + e.reason + "\n"
            )
            print(res_error)
        elif hasattr(e, 'code'):
            res_error = (
                'The server couldn\'t fulfill the request.' + "\n" +
                'Error code: ', e.code + "\n"
            )
            print(res_error)
else:
    res_dict = json.load(response)
    print(res_dict)
# 送られてきたデータから必要な情報を取得して新しい変数に格納する
age_D = res_dict['record']['年齢']['value']
birthplace_D = res_dict['record']['出身地域']['value']
residence_D = res_dict['record']['居住地域']['value']
hobby_D = res_dict['record']['趣味']['value']
 
 
# 取得した情報を確認する
print("年齢:", age_D)
print("出身地域:", birthplace_D)
print("居住地域:", residence_D)
print("趣味:", hobby_D)
 
DOMAIN = os.getenv('DB_DOMAIN')## ドメイン　自環境のものを入れる
LOGIN = os.getenv('DB_LOGIN_ID')## ログイン名　自環境のものを入れる
PASS = os.getenv('DB_LOGIN_PASS')## パス　自環境のものを入れる
appno = 2## 取得したいアプリのアプリNo
record_no = 7## 取得したいレコードのレコード番号
uri = "https://" + DOMAIN + ".cybozu.com/k/v1/record.json"
AUTH = base64.b64encode((LOGIN + ":" + PASS).encode())
## ヘッダ作成
headers = {
    "Host":DOMAIN + ".cybozu.com:443",
    "X-Cybozu-Authorization":AUTH,
    "Content-Type": "application/json",
}
## body作成
body = {
    "app":appno,
    "id":record_no
}
## リクエスト作成
req = urllib.request.Request(
            url=uri, ## url
            data=json.dumps(body).encode(), ## body 
            headers=headers, ## header
            method="GET", ## GET
            )
## リクエスト送信　結果受け取り
try:
    response = urllib.request.urlopen(req)
except urllib.error.URLError as e:## エラーが生じた場合は補足する
    # https://docs.python.org/ja/3/howto/urllib2.html tryの参考
        if hasattr(e, "reason"):
            res_error = (
                "We failed to reach a server." + "\n" +
                "Reason: " + e.reason + "\n"
            )
            print(res_error)
        elif hasattr(e, 'code'):
            res_error = (
                'The server couldn\'t fulfill the request.' + "\n" +
                'Error code: ', e.code + "\n"
            )
            print(res_error)
else:
    res_dict = json.load(response)
    print(res_dict)
# 送られてきたデータから必要な情報を取得して新しい変数に格納する
age_E = res_dict['record']['年齢']['value']
birthplace_E = res_dict['record']['出身地域']['value']
residence_E = res_dict['record']['居住地域']['value']
hobby_E = res_dict['record']['趣味']['value']
 
# 取得した情報を確認する
print("年齢:", age_E)
print("出身地域:", birthplace_E)
print("居住地域:", residence_E)
print("趣味:", hobby_E)

# DBアクセスここまで

# プリント出力ここから

profile_A = f"Aさんは{age_A}で、{birthplace_A}出身で、趣味は{hobby_A}です。"
print(profile_A)
 
profile_B = f"Bさんは{age_B}で、{birthplace_B}出身で、趣味は{hobby_B}です。"
print(profile_B)
 
profile_C = f"Cさんは{age_C}で、{birthplace_C}出身で、趣味は{hobby_C}です。"
print(profile_C)
 
profile_D = f"Dさんは{age_D}で、{birthplace_D}出身で、趣味は{hobby_D}です。"
print(profile_D)
 
profile_E = f"Eさんは{age_E}で、{birthplace_E}出身で、趣味は{hobby_E}です。"
print(profile_E)

# プリント出力ここまで


# ChatGPTここから
openai.api_key = os.getenv('OPENAI_API_KEY')
 
 
response = openai.chat.completions.create(
model="gpt-3.5-turbo",
messages=[
{"role": "system", "content": "あなたは話題提供Botです。あたえられたキーワードで、盛り上がる話題を1文で具体的な質問文で出力します。"},
{"role": "user", "content": profile_A},
{"role": "user", "content": profile_B},
{"role": "user", "content": profile_C},
{"role": "user", "content": profile_D},
{"role": "user", "content": profile_E},
]
)

print(response.choices[0].message.content)

# GPTここまで

app = Flask(__name__)

configuration = Configuration(access_token=os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'



@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):

    # 受信したメッセージ
    received_text = event.message.text
    
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=response.choices[0].message.content)]
            )
        )

def forward():
  import ngrok

  listener = ngrok.forward(8888, authtoken_from_env=True)
  print(f"Ingress established at {listener.url()}")


if __name__ == "__main__":
    if os.getenv('ENV') == 'dev':
        forward()

    app.run(port=8888)
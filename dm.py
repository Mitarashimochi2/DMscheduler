
import time
import schedule
import tweepy


# 認証に必要なキーとトークン
API_KEY = 'token'
API_SECRET = 'token'
ACCESS_TOKEN = 'token'
ACCESS_TOKEN_SECRET = 'token'

# APIの認証
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)



def send():

    message="送信したいテキスト"
    Account = 'TwitterのID(@以降）'
    print("送信成功" + message)


    # アカウントの内部IDを取得する
    inner_id = api.user_timeline(screen_name=Account, count=1, page=0)[0].user.id
    api.send_direct_message(recipient_id=inner_id,text=message)

    schedule.clear()

schedule.every().day.at("21:53").do(send)

 
while True:
  schedule.run_pending()
  time.sleep(1)

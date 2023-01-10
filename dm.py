
import time
import datetime
import schedule
import tweepy
import random

# 認証に必要なキーとトークン
API_KEY = 'hFrFfBqCJ2SDqkx4nBvn8nYiP'
API_SECRET = 'oDttfZzNWCo6lWC0QZRxc1eUEPMIIJOh4NhjR5rTdMD0Ma105i'
ACCESS_TOKEN = '1261838378254741504-pmzVY4aflFnluIQOVIepJoKaJSm7Id'
ACCESS_TOKEN_SECRET = 'aG1NdVTwVxTgDQHXrvIK6niTfV8M5ojrCTM9dbd2vaNRC'

# APIの認証
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

switch=False

def send():
    global switch

    message="ww 公式割と自由だね"
    Account = 'arigataiari'
    print("送信成功" + message)

    switch = False
    # アカウントの内部IDを取得する
    inner_id = api.user_timeline(screen_name=Account, count=1, page=0)[0].user.id
    api.send_direct_message(recipient_id=inner_id,text=message)

    schedule.clear()

schedule.every().day.at("21:53").do(send)

 
while True:
  schedule.run_pending()
  time.sleep(1)
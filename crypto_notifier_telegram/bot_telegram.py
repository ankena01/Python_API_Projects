'''
1. Create a bot using Telegram  app and assign [Name , Username]
2. Create group in telegram <identifier>
3. Add a bot to newly created group
4. Create a test case to trigger this bot to send messages in group

Requests - 


'''

import requests
from datetime import datetime
import pytz
from cmc_api_test import cmc
from telegram_secrets import telegram_secrets

IST = pytz.timezone("Asia/Kolkata")
raw_time = datetime.now(IST)
curr_date = raw_time.strftime("%d-%m-%Y")
curr_time = raw_time.strftime("%H-%M-%S")

# 2107313679:AAFFkhKzViwwntQhV88iPlSS5Io52IMWt9A
telegram_auth_token = telegram_secrets.telegram_token
telegram_group_id = "crypto_notifier_3"

msg = f"Current price of Bitcoin is {cmc.get_price('BTC')['data']['BTC']['quote']['USD']['price']} on {curr_date} {curr_time}"


def send_msg_on_telegram(message):
    telegram_api_url = f"https://api.telegram.org/bot{telegram_auth_token}/sendMessage?chat_id=@{telegram_group_id}&text={message}"
    print(f"https://api.telegram.org/bot{telegram_auth_token}/sendMessage?chat_id=@{telegram_group_id}&text={message}")
    telegram_response = requests.get(telegram_api_url)
    print(telegram_secrets.telegram_token)

    if telegram_response.status_code == 200:
        print("Notification sent to telegram !!!")
    else:
        print("Failed !!!")

send_msg_on_telegram(msg)








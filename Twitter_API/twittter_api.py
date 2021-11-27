import tweepy
import requests
import json
import cmc_api_test

API_KEY = # <Your API KEY>
SECRET_KEY = # <Your SECRET KEY>
ACCESS_TOKEN = # <Your ACCESS TOKEN>
ACCESS_TOKEN_SECRET = # <Your ACCESS TOKEN SECRET>
#callback_url = 'oob'

auth_handler = tweepy.OAuthHandler(consumer_key=API_KEY , consumer_secret=SECRET_KEY)
auth_handler = auth_handler.set_access_token(ACCESS_TOKEN , ACCESS_TOKEN_SECRET)


api = tweepy.API(auth_handler , wait_on_rate_limit=True)

print(api)

print("Login successful")

bitcppoinprice = cmc_api_test.cmc.get_price('BTC')['data']['BTC']['quote']['USD']['price']
#print(bitcppoinprice)
api.update_status(str(bitcppoinprice))









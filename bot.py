import tweepy
import time

# Authenticate to Twitter
api_key = process.env.API_KEY
api_secret = process.env.API_SECRET
access_token =  process.env.ACESS_TOKEN
access_token_secret = process.env.ACCESS_TOKEN_SECRET

auth = tweepy.OAuth1UserHandler(
   api_key, api_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

while True:
    api.update_status_with_media("", "fotodeps.jpeg")
    time.sleep(60*10)
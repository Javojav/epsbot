import tweepy
import time
import os

# Authenticate to Twitter
api_key = os.environ.get('API_KEY', None)
api_secret = os.environ.get('API_SECRET', None)
access_token = os.environ.get('ACESS_TOKEN', None)
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET', None)

auth = tweepy.OAuth1UserHandler(
   api_key, api_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

# Post every 10 minutes
while True:
    api.update_status_with_media("", "fotodeps.jpeg")
    time.sleep(60*10)
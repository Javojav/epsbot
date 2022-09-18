import tweepy

# Authenticate to Twitter
api_key = ""
api_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuth1UserHandler(
   api_key, api_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

api.update_status_with_media("", "fotodeps.jpeg")
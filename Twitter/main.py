from configparser import ConfigParser
from time import sleep

import tweepy

# Assign keys and secrets using default.ini
parser = ConfigParser()
parser.read('default.ini')

conKey = parser.get('consumer', 'key')
conSecret = parser.get('consumer', 'secret')
accessKey = parser.get('access', 'token')
accessSecret = parser.get('access', 'secret')

# Use OAuthHandler to get access to the Twitter API
auth = tweepy.OAuthHandler(conKey, conSecret)
auth.set_access_token(accessKey, accessSecret)

api = tweepy.API(auth)

myTweets = api.home_timeline()

for tweet in myTweets:
    print(f"Status: {tweet.text}")
    print(f"Dated Created: {tweet.created_at}")
    

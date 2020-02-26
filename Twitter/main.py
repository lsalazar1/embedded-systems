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

try:
    # Prompt user for the twitter page they would like to see
    userInput = input('Whose twitter info would you like to see? Enter their screen name: ')
    twitter = api.get_user(userInput)

    # Use senseHAT to show twitter info
    print(f'Name: {twitter.name}')
    print(f'Latest Status: {twitter.status.text}')
except tweepy.error.TweepError:
    print('User not found. Try another user.')

    

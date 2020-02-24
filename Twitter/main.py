from Listener import *
from configparser import ConfigParser

if __name__ == '__main__':
    parser = ConfigParser()
    parser.read('default.ini')

    consumerKey = parser.get('consumer', 'apiKey')
    consumerSecret = parser.get('consumer', 'apiSecret')


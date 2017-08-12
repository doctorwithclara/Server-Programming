import tweepy
import time, sys

consumer_key = 'iiRI3RZhVYRKRpGbe91ZmXgy8'
consumer_secret = 'hR40sQ7OqJ0Oq9dkCj0uhkp1sp21Ndvn5t9i4gWftKlbVeYB8K'
access_token = '605285251-P1F5efNk95CnHYHxyFcVLsABCW3cG3pR64jsRNZk'
access_token_secret= 'Qx7qTKejt5RMTbI1oajYxEQELFRczWXFgVkImiWpsqNwQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items():
    print(status.text)
    time.sleep(0.3)

import tweepy
import csv
from tweepy.auth import OAuthHandler

consumer_key = 'S1k9skL3JDxE2Lljt5RFXomAN'
consumer_secret = 'FYuA2Sq9tBhN97r5ujEUiO9nNs2CF2DwD908aedOk5XFMNoh6z'
access_token = '412147347-TCcy5EQXetkK4KDyZl2d6E7WEBgexEqaOkDn7inP'
access_token_secret = 'quNzAT5hFvJYILIxPKF3wo8uRIiWhuZiQPWANsKjZiytM'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('teroris.csv', 'a')
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#GantiPresiden2019",count=50,
                           lang="id",
                           since="2018-03-30").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
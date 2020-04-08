import tweepy
from textblob import TextBlob
import csv
import json

# Step 1 - Authenticate
consumer_key= ''
consumer_secret= ''

access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, parser = tweepy.parsers.JSONParser())

#Step 3 - Retrieve Tweets
#public_tweets = api.search('Cape Town', rpp = 1)
public_tweets = api.search('Hello World', count =2)

with open('your_data.json', 'w', encoding='utf-8') as f: json.dump(public_tweets, f, ensure_ascii=False, indent = 4)

#for tweet in public_tweets:
    #print(tweet.text)

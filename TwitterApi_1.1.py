import tweepy
from textblob import TextBlob
import csv
import json
import logging
import boto3
import botocore.exceptions import ClientError

# Step 1 - Authenticate
consumer_key= ''
consumer_secret= ''

access_token=''
access_token_secret=''

ACCESS_KEY=''
SECRET_KEY=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, parser = tweepy.parsers.JSONParser())

#Step 3 - Retrieve Tweets
#public_tweets = api.search('Cape Town', rpp = 1)
public_tweets = api.search('Hello World', count =2)

#Step 4 - Save tweets to JSON file
with open('your_data.json', 'w', encoding='utf-8') as f: json.dump(public_tweets, f, ensure_ascii=False, indent = 4)

S#Step 5 - Save JSON to S3
def upload_file(file_name, bucket, object_name=NONE):

    if object_name =None:
        object_name = file_name

    #Upload File
    s3_client = boto3.client('s3', aws_acees_key=ACCESS_KEY, aws_secret_key=SECRET_KEY)
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as :
        logging.error(e)
        return False
    return True

upload_file(x,x,x)
#for tweet in public_tweets:
    #print(tweet.text)

# Dependencies
import tweepy
import json
import time

# Twitter API Keys
access_token = “971242588580777984-o9Ij0ND0oaqGA5qRZo9Odsi4n7HdfRp”
access_token_secret = “zUxKPiwI1IftMxiNxylpdL94sMWCTQeWtuJVcgIhb0cfl”
consumer_key = “LxcMXMWLwqlJttkA6cPMKB8Bd”
consumer_secret =“MpjzVseaBDFA8rVWStGqJeG6ksnJ2HeMNqDXI6FDMVJ9oALncQ”

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE


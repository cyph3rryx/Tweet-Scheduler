import tweepy
import datetime
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
auth.set_access_token("access_token", "access_token_secret")

# Create API object
api = tweepy.API(auth)

# Function to schedule tweet
def schedule_tweet(tweet, year, month, day, hour, minute):
    scheduled_time = datetime.datetime(year, month, day, hour, minute)
    current_time = datetime.datetime.now()
    time_difference = (scheduled_time - current_time).total_seconds()
    time.sleep(time_difference)
    api.update_status(tweet)

# Get input from user
tweet = input("Enter the text of the tweet: ")
year = int(input("Enter the year of the scheduled tweet: "))
month = int(input("Enter the month of the scheduled tweet: "))
day = int(input("Enter the day of the scheduled tweet: "))
hour = int(input("Enter the hour of the scheduled tweet: "))
minute = int(input("Enter the minute of the scheduled tweet: "))

# Call function to schedule tweet
schedule_tweet(tweet, year, month, day, hour, minute)

print("Tweet successfully scheduled!")

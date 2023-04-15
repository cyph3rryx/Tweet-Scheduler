import tweepy
import datetime
import time
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Authenticate to Twitter
auth = tweepy.OAuthHandler(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"])
auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])

# Create API object
api = tweepy.API(auth)

# Function to schedule tweet
def schedule_tweet(tweet, year, month, day, hour, minute):
    try:
        scheduled_time = datetime.datetime(year, month, day, hour, minute)
        current_time = datetime.datetime.now()
        time_difference = (scheduled_time - current_time).total_seconds()

        if time_difference <= 0:
            raise ValueError("Scheduled time must be in the future")

        time.sleep(time_difference)
        api.update_status(tweet)
        logger.info("Tweet successfully scheduled")

    except Exception as e:
        logger.error(f"Error scheduling tweet: {e}")
        raise e

# Get input from user
while True:
    try:
        tweet = input("Enter the text of the tweet (280 characters or less): ")
        if len(tweet) > 280:
            raise ValueError("Tweet must be 280 characters or less")

        year = int(input("Enter the year of the scheduled tweet (e.g. 2023): "))
        month = int(input("Enter the month of the scheduled tweet (1-12): "))
        day = int(input("Enter the day of the scheduled tweet (1-31): "))
        hour = int(input("Enter the hour of the scheduled tweet (0-23): "))
        minute = int(input("Enter the minute of the scheduled tweet (0-59): "))

        schedule_tweet(tweet, year, month, day, hour, minute)
        break

    except ValueError as e:
        logger.error(f"Invalid input: {e}")
        print(f"Invalid input: {e}. Please try again.\n")
        continue

    except Exception as e:
        logger.error(f"Error: {e}")
        print(f"Error: {e}. Please try again.\n")
        continue

print("Tweet successfully scheduled!")

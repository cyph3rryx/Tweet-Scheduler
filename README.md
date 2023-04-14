# Tweet-Scheduler


This is a simple Python command-line interface (CLI) program that allows you to schedule tweets to be sent at a later time. It uses the Tweepy library to authenticate to Twitter's API and send the scheduled tweet.

## Installation

Clone the repository:

``` bash  
git clone https://github.com/<username>/tweet-scheduler.git
```

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

    1. Create a Twitter API key and access token by following these steps:

    2. Create a Twitter developer account if you don't already have one.

    3. Create a new app and generate your API key, API secret key, access token, and access token secret.

    4. Add your API key, API secret key, access token, and access token secret to a .env file in the root directory of the project:

```
CONSUMER_KEY=<your_consumer_key>
CONSUMER_SECRET=<your_consumer_secret>
ACCESS_TOKEN=<your_access_token>
ACCESS_TOKEN_SECRET=<your_access_token_secret>
```

# Usage
To schedule a tweet, run the scheduler.py script and enter the text of the tweet and the date and time you want it to be sent:

``` python
python scheduler.py
```
You will be prompted to enter the text of the tweet, the year, month, day, hour, and minute of the scheduled tweet. The program will then calculate the time difference between the scheduled time and the current time, and sleep for that amount of time before sending the tweet.

### Error handling
The program does not currently include error handling or validation, so it is important to ensure that the input is valid and that the tweet text is less than 280 characters.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

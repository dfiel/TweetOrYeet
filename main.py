import requests
import json
import time


def grab_api():
    return json.loads(requests.get("https://api.tweetoryeet.tech").text)


def grab_latest_tweet():
    tweet_time = time.strptime(grab_api()[0]["created_at"], "%a %b %d %H:%M:%S +0000 %Y")
    return time.mktime(tweet_time), grab_api()[0]["text"]


def check_tweet_time(tweet, check=86400):
    return time.time() - tweet < check


if __name__ == '__main__':
    print(grab_latest_tweet())

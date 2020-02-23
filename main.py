import requests
import json
import time
import os


def grab_api():
    return json.loads(requests.get("https://api.tweetoryeet.tech").text)


def grab_latest_tweet():
    tweet_time = time.strptime(grab_api()[0]["created_at"], "%a %b %d %H:%M:%S +0000 %Y")
    return time.mktime(tweet_time), grab_api()[0]["text"]


def check_tweet_time(tweet, check=86400):
    return time.time() - tweet < check


def trav_dirs(rootDir):
    for i in os.walk(rootDir):
        for x in i[2]:
            print(os.path.abspath(x))



if __name__ == '__main__':
    print(grab_latest_tweet())
    tweet_time = grab_latest_tweet()
    print(check_tweet_time(tweet_time[0]))
    trav_dirs('.')


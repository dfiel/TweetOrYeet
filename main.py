import json
import os
import time

import requests

import encryption
import generate_key

DEBUG = True


def grab_latest_tweet():
    api = json.loads(requests.get("https://api.tweetoryeet.tech").text)
    tweet_time = time.strptime(api[0]["created_at"], "%a %b %d %H:%M:%S +0000 %Y")
    return time.mktime(tweet_time), api()[0]["text"]


def check_tweet_time(tweet_time, check=86400):
    return time.time() - tweet_time < check


def trav_dirs(rootDir):
    for i in os.walk(rootDir):
        for x in i[2]:
            print(os.path.abspath(x))


def main():
    encrypter = encryption.Encrypter()
    if os.path.exists('fernet.key'):
        encrypter.load_key('fernet.key')
    else:
        generate_key.generate_fernet_key()


if __name__ == '__main__':
    if DEBUG:
        system_root = 'TestDir'
    else:
        system_root = '.'
    encrypter = encryption.Encrypter()
    encrypter.load_key('fernet.key')
    print(grab_latest_tweet())
    latest_tweet = grab_latest_tweet()
    print(check_tweet_time(latest_tweet[0]))
    trav_dirs(system_root)


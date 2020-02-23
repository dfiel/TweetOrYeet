import requests
import json
import time
import os
import encryption, generate_key


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


def main():
    encrypter = encryption.Encrypter()
    if os.path.exists('fernet.key'):
        encrypter.load_key('fernet.key')
    else:
        generate_key.generate_fernet_key()



if __name__ == '__main__':
    encrypter = encryption.Encrypter()
    encrypter.load_key('fernet.key')
    print(grab_latest_tweet())
    tweet_time = grab_latest_tweet()
    print(check_tweet_time(tweet_time[0]))
    trav_dirs('.')


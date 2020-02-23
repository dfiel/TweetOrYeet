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
    return time.mktime(tweet_time), api[0]["text"]


def check_tweet_time(tweet_time, check=86400):
    return time.time() - tweet_time < check


def traverse_dirs(root_dir, encrypt=None, decrypt=None):
    for i in os.walk(root_dir):
        for x in i[2]:
            path = os.path.normpath(os.path.join(os.getcwd(), i[0], x))
            if encrypt:
                encrypt.encrypt_file(path)
            elif decrypt:
                decrypt.decrypt_file(path)
            else:
                print(path)


def tweet_loop(api_refresh=120, tweet_age=86400):
    wait_time = 0
    while True:
        if time.time() - wait_time < api_refresh:
            time.sleep(1)
            continue
        tweet = grab_latest_tweet()
        wait_time = time.time()
        if time.time() - tweet[0] < tweet_age:
            time.sleep(1)
            continue
        break
    print("Timeout reached on tweet. Entering Grace Period.")
    grace_period()


def grace_period(api_refresh=120, timeout=129600):
    wait_time = 0
    while True:
        if time.time() - wait_time < api_refresh:
            time.sleep(1)
            continue
        tweet = grab_latest_tweet()
        wait_time = time.time()
        if time.time() - tweet[0]
        if not check_tweet_time(tweet[0], timeout):
            if time.time() - tweet[0]
            time.sleep(1)
            continue



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
    main()

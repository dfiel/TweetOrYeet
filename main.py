import json
import os
import time

import requests

import encryption
import generate_key

DEBUG = True
DEBUG_API_REFRESH_DELAY = 2
DEBUG_TWEET_AGE_MAX = 30


def grab_latest_tweet():
    api = json.loads(requests.get("https://api.tweetoryeet.tech").text)
    tweet_time = time.strptime(api[0]["created_at"], "%a %b %d %H:%M:%S +0000 %Y")
    return time.mktime(tweet_time)-18000, api[0]["text"]  # Adjusting by 5 hours


def tweet_loop(api_refresh=120, tweet_age=86400):
    if DEBUG:
        api_refresh = DEBUG_API_REFRESH_DELAY
        tweet_age = DEBUG_TWEET_AGE_MAX
    wait_time = 0
    while True:
        if time.time() - wait_time < api_refresh:
            if DEBUG:
                print("TWEET_LOOP: Waiting to refresh API")
            time.sleep(1)
            continue
        print("TWEET_LOOP: Grabbing Tweet")
        tweet = grab_latest_tweet()
        wait_time = time.time()
        if DEBUG:
            print('TWEET_LOOP: Current Time: {}  Tweet Time: {}  Difference: {}'.format(wait_time, tweet[0],
                                                                                        wait_time-tweet[0]))
        if time.time() - tweet[0] < tweet_age:
            if DEBUG:
                print("TWEET_LOOP: Tweet time less than maximum age")
            time.sleep(1)
            continue
        print("Timeout reached on tweet. Entering Grace Period.")
        result = grace_period(api_refresh=api_refresh, timeout=tweet_age)
        if result == 'Encrypt':
            break
        if result == 'Safe':
            wait_time = 0
            continue
    encryption.traverse_dirs(system_root, encrypt=encrypter)
    return 'Encrypted'


def grace_period(api_refresh=120, timeout=86400):
    wait_time = 0
    while True:
        if time.time() - wait_time < api_refresh:
            if DEBUG:
                print("GRACE_PERIOD: Waiting to refresh API")
            time.sleep(1)
            continue
        tweet = grab_latest_tweet()
        wait_time = time.time()
        tweet_time = time.time() - tweet[0]
        if DEBUG:
            print('TWEET_LOOP: Current Time: {}  Tweet Text: {}  Tweet Time: {}  Difference: {}'.format(wait_time,
                                                                                                        tweet[1],
                                                                                                        tweet[0],
                                                                                                        tweet_time))
        if timeout < tweet_time < 1.5*timeout:
            if DEBUG:
                print("GRACE_PERIOD: Tweet time less than maximum age")
            time.sleep(1)
            continue
        if tweet_time > 1.5*timeout:
            if DEBUG:
                print("GRACE_PERIOD: Maximum time exceeded. Encrypting")
            return 'Encrypt'
        if tweet_time < 1.5*timeout and tweet[1] == 'I Love Life':
            if DEBUG:
                print('GRACE_PERIOD: Tweet confirmed, exiting Grace Period')
            return 'Safe'


def main():
    if os.path.exists('fernet.key'):
        encrypter.load_key('fernet.key')
    else:
        generate_key.generate_fernet_key()
    print("Entering Twitter Scraping Loop")
    print("This will wait 24 hours for a tweet from your account")
    print("If after 24 hours there is no twitter activity, a grace period is entered")
    print('If you tweet "I Love Life" during this grace period, the loop is restarted and your data is not encrypted')
    print("If this grace period passes, your data is encrypted")
    print()
    print("ENSURE YOU HAVE SAVED YOUR ENCRYPTION KEY")
    print("THIS KEY WILL BE ENCRYPTED AS WELL")
    print()
    for i in range(10, 0, -1):
        print("Starting in " + str(i) + " seconds")
        time.sleep(1)
    print("Loop Started. Ctrl+C to exit")
    print()
    if tweet_loop() == 'Encrypted':
        encrypter.clear()
        print('Data has been encrypted. Exiting...')
        exit()


if __name__ == '__main__':
    if DEBUG:
        system_root = 'TestDir'
    else:
        system_root = '.'
    encrypter = encryption.Encrypter()
    main()

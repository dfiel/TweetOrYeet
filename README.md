## Inspiration
Death is inevitable. What happens to the data we leave behind?
## What it does
Using the Twitter API, we scrape all tweets from a user and select the latest one. If 24 hours have passed since the last tweet, enter a grace period where if the user tweets a specific phrase, the encryption is cancelled. If there is no valid tweet during the grace period, traverse through all directories and encrypt every file. After encrypting, flush the key from memory, and exit.

## How we built it
We decided to use Python, as the wide availability of libraries facilitates rapid development. We used the Twitter API to grab the latest tweet, and Fernet encryption to encrypt all files. We hosted an API wrapper on Google Cloud in order to not have to disclose our Twitter API secrets. We used the domain TweetOrYeet.tech from domain.com for a place to host the API. 

## Challenges we ran into
It was difficult to figure out how to traverse through all directories and build correct absolute paths to feed into the encryption function. We also struggled to find a bug in our time logic, that ended up being a time zone difference between the Twitter API response and the local machine. We also had some slight problems making sure everything encrytpted correctly. 

## Accomplishments that we're proud of
We were able to implement all features we set out to include, and more, in the allotted time.

## What we learned
We learned how to create a http server in Python to grab values from Twitter and serve them, and how to use nginx to proxy requests to Python while also rate limiting. We learned how Fernet encryption works, and how to create a class that utilizes it to encrypt and decrypt files, including a mode that encypts the file name as well as the contents.

## What's next for Tweet Or Yeet
We hope to add logic to automatically add the script as a system service, so it is always running, as well as reading the input files in chunks rather than all at once to reduce memory errors on low-memory systems. 

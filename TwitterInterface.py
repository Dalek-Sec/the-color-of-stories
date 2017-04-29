import twitter
import json


##

CONSUMER_KEY = "7oWaYZdQSWzaCYBZDc83QE7W9"
CONSUMER_SECRET = "0010JpzWZ1e3u8oEoq2l6bM5B6GLzeY9ajKVTXMvi6LUC2rTg5"
ACCESS_TOKEN_KEY = "858295726811512832-WOfKkjq6Fi5nV5VKoLFzGG3BVZ3Ikca"
ACCESS_TOKEN_SECRET = "vbz5jrgda4BwJxwS3bCA8P8AAwVzdrS8szEL8pYg9ezro"


api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN_KEY,
                  access_token_secret=ACCESS_TOKEN_SECRET)

def main():
    print("This is a Twitter Bot")
    print(api.GetDirectMessages())

if __name__ == '__main__':
    main()
    

import tweepy
import random
import pyinputplus as pyip

# Twitter API Authentication
def twitter_auth():
    api_key = "3r6HNcqjB0hMkipq5qpzs9v3J"
    api_secret_key = "WRxagtTkJmmYBIxiiMm2nFBz395l05qcl5TzURWW2HcFgyaXxY"
    access_token = "1658380517828620293-RZgKRCC4DdaQb1QijsGhbRcUc7wBaX"
    access_token_secret = "avW22KEJWUI06f8mFx7ER2JqqSSQCtejh5ddKPQ6xyyu7"
    
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAI0NxAEAAAAAPp3YWRIWxspajBfUks1kYTdcIk4%3DUakIRYVjz6y46bW7JrJEQzvtqkb9cJ823Cw47yyY6jwi4OZgSa", consumer_key=api_key,
                         consumer_secret=api_secret_key, access_token=access_token,
                         access_token_secret=access_token_secret)

# Generate a Tech Tweet
def generate_tech_tweet():
    tech_tweets = [
        "AI is transforming the world of technology. Stay ahead of the curve!",
        "Quantum computing: the next frontier in solving complex problems.",
        "Cloud computing is not just a trend; it's the backbone of modern applications.",
        "Cybersecurity is more important than ever. Are your systems secure?",
        "AR and VR are revolutionizing the way we interact with digital content.",
    ]
    return random.choice(tech_tweets)

# Get User Permission
def get_permission():
    response = pyip.inputYesNo("A new tech tweet is ready to post. Do you want to proceed? (yes/no): ")
    return response.lower() == "yes"

# Post the Tweet using v2 API
def post_tweet(api, tweet):
    try:
        api.create_tweet(text=tweet)
        print("Tweet posted successfully!")
    except tweepy.errors.Forbidden as e:
        print(f"Access issue: {e}")
    except tweepy.errors.TweepyException as e:
        print(f"An error occurred: {e}")

# Main Function
if __name__ == "__main__":
    api = twitter_auth()
    tweet = generate_tech_tweet()
    print(f"Generated Tweet: {tweet}")
    
    if get_permission():
        post_tweet(api, tweet)
    else:
        print("Tweet not posted.")

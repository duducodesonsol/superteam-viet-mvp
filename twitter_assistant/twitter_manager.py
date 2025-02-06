# twitter_assistant/twitter_manager.py

import tweepy
from local_llm.llm import generate_response

# Replace these with your actual Twitter API credentials.
TWITTER_API_KEY = "YOUR_TWITTER_API_KEY"
TWITTER_API_SECRET = "YOUR_TWITTER_API_SECRET"
TWITTER_ACCESS_TOKEN = "YOUR_TWITTER_ACCESS_TOKEN"
TWITTER_ACCESS_TOKEN_SECRET = "YOUR_TWITTER_ACCESS_TOKEN_SECRET"

def get_twitter_client():
    auth = tweepy.OAuth1UserHandler(
        TWITTER_API_KEY, TWITTER_API_SECRET,
        TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
    )
    return tweepy.API(auth)

def propose_tweet(context: str) -> str:
    """
    Use the local LLM to generate a draft tweet based on the provided context.
    """
    prompt = f"Propose a tweet based on: {context}"
    tweet_draft = generate_response(prompt, context)
    return tweet_draft

def correct_handles(tweet_draft: str, valid_handles: list) -> str:
    """
    Correct Twitter handles in the tweet draft based on a list of valid handles.
    """
    words = tweet_draft.split()
    corrected_words = []
    for word in words:
        if word.startswith("@"):
            handle = word[1:]
            if handle not in valid_handles:
                # Replace with the first valid handle as an example.
                corrected_words.append("@" + valid_handles[0])
            else:
                corrected_words.append(word)
        else:
            corrected_words.append(word)
    return " ".join(corrected_words)

def publish_tweet(tweet: str):
    """
    Publish the tweet using the Twitter API. For demo purposes, this function
    prints the tweet instead of actually publishing it.
    """
    client = get_twitter_client()
    # In a real implementation, uncomment the following line:
    # client.update_status(tweet)
    print("Tweet published:", tweet)

if __name__ == '__main__':
    context = "Announcing our latest update!"
    tweet_draft = propose_tweet(context)
    valid_handles = ["SuperteamVN", "ExampleHandle"]
    corrected_tweet = correct_handles(tweet_draft, valid_handles)
    publish_tweet(corrected_tweet)

# twitter_assistant/twitter_manager.py

import tweepy
from local_llm.llm import generate_response
    
TWITTER_API_KEY = "YOUR_TWITTER_API_KEY"
TWITTER_API_SECRET = "YOUR_TWITTER_API_SECRET"
TWITTER_ACCESS_TOKEN = "YOUR_TWITTER_ACCESS_TOKEN"
TWITTER_ACCESS_TOKEN_SECRET = "YOUR_TWITTER_ACCESS_TOKEN_SECRET"
#It's advisable to store the above details as environment variables for security

def get_twitter_client():
    auth = tweepy.OAuth1UserHandler(
        TWITTER_API_KEY, TWITTER_API_SECRET,
        TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
    )
    return tweepy.API(auth)

def propose_tweet(context: str) -> str:
    # Use the local LLM to generate a draft tweet based on the provided context.
    prompt = f"Propose a tweet based on: {context}"
    tweet_draft = generate_response(prompt, context)
    return tweet_draft

def find_most_likely_handle(handle: str, valid_handles: list) -> str:
        # This function finds the most likely handle from the valid_handles list.
        # For simplicity, we use the first valid handle as the most likely one.
        # In a real implementation, you might use a more sophisticated method.
        if handle in valid_handles:
            return handle
        else:
            # Notify the user that the handle isn't valid
            print(f"Handle @{handle} isn't valid. Replacing with @{valid_handles[0]}")
            return valid_handles[0]

def correct_handles(tweet_draft: str, valid_handles: list) -> str:
        # Correct Twitter handles in the tweet draft based on a list of valid handles.
        words = tweet_draft.split()
        corrected_words = []
        for word in words:
            if word.startswith("@"):
                handle = word[1:]
                corrected_handle = find_most_likely_handle(handle, valid_handles)
                corrected_words.append("@" + corrected_handle)
            else:
                corrected_words.append(word)
        return " ".join(corrected_words)

def publish_tweet(tweet: str):
    # Publish the tweet using the Twitter API. For demo purposes, this function prints the tweet instead of actually publishing it.
    client = get_twitter_client()
    # In a real implementation, uncomment the following line:
    # client.update_status(tweet)
    print("Tweet published:", tweet)


if __name__ == '__main__':
    context = "Announcing our latest update!"
    tweet_draft = propose_tweet(context)
    valid_handles = ["SuperteamVN", "SuperteamNG", "dudu_codes"]
    corrected_tweet = correct_handles(tweet_draft, valid_handles)
    publish_tweet(corrected_tweet)
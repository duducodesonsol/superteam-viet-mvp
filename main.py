# main.py

import threading
from telegram_bot.bot import run_bot
from member_finder.finder import load_members, find_member
from twitter_assistant.twitter_manager import propose_tweet, correct_handles, publish_tweet
from content_advisor.advisor import advise_content

def start_telegram_bot():
    run_bot()

def run_member_finder_example():
    members = load_members()
    query = "I want to find a RUST developer to build a DEFI project with Twitter integration."
    explanation, member = find_member(query, members)
    print("Member Finder Output:", explanation)
    if member:
        print("Member details:", member)

def run_twitter_assistant_example():
    context = "Announcing our latest update!"
    tweet_draft = propose_tweet(context)
    valid_handles = ["SuperteamVN", "ExampleHandle"]
    corrected_tweet = correct_handles(tweet_draft, valid_handles)
    print("Proposed Tweet:", corrected_tweet)
    publish_tweet(corrected_tweet)

def run_content_advisor_example():
    platform = "Telegram"
    content = "Welcome to our community group!"
    improved_content = advise_content(platform, content)
    print("Content Advisor Suggestion:", improved_content)

if __name__ == '__main__':
    # Run the Telegram bot in a separate thread so it can listen continuously.
    telegram_thread = threading.Thread(target=start_telegram_bot)
    telegram_thread.daemon = True
    telegram_thread.start()

    # Run example workflows for the other modules.
    run_member_finder_example()
    run_twitter_assistant_example()
    run_content_advisor_example()

    # Keep the main thread alive to allow the Telegram bot to run.
    telegram_thread.join()

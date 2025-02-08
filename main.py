# main.py

import threading
from telegram_bot.bot import run_bot
from member_finder.finder import load_members, find_matching_member
from twitter_assistant.twitter_manager import (
    propose_tweet,
    correct_handles,
    publish_tweet
)
from content_advisor.advisor import advise_content
from content_advisor.advisor import advise_content

def start_telegram_bot():
    run_bot()

def run_member_finder_example():
    query = "example_query"
    members = load_members()
    member_explanation, found_member = find_matching_member(query, members)
    print("Member Finder Output:", member_explanation)
    if found_member:
        print("Member details:", found_member)

def run_twitter_assistant_example():
    context = "Announcing our latest update!"
    proposed_tweet = propose_tweet(context)
    valid_twitter_handles = ["SuperteamVN", "ExampleHandle"]
    corrected_tweet = correct_handles(proposed_tweet, valid_twitter_handles)
    print("Proposed Tweet:", corrected_tweet)
    publish_tweet(corrected_tweet)

def run_content_advisor_example():
    platform = "Telegram"
    initial_content = "Welcome to our community group!"
    improved_content = advise_content(platform, initial_content)
    print("Content Advisor Suggestion:", improved_content)

if __name__ == '__main__':
    # Run the Telegram bot in a separate thread so it can listen continuously.
    telegram_bot_thread = threading.Thread(target=start_telegram_bot)
    telegram_bot_thread.daemon = True
    telegram_bot_thread.start()

    # Run example workflows for the other modules.
    run_member_finder_example()
    run_twitter_assistant_example()
    run_content_advisor_example()

    # Keep the main thread alive to allow the Telegram bot to run.
    telegram_bot_thread.join()

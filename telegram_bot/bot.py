import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from telegram_bot.doc_processing import retrieve_answer

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# Retrieve the token from an environment variable
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("No TELEGRAM_BOT_TOKEN found in environment variables")

# Retrieve the webhook URL from an environment variable
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
if not WEBHOOK_URL:
    raise ValueError("No WEBHOOK_URL found in environment variables")

def start(update, _):
    """
    Send a welcome message when the /start command is issued.
    """
    update.message.reply_text("Welcome to the bot! How can I assist you today?")

def handle_message(update, context):
    """
    Handle incoming messages and respond with an answer retrieved from the documents.
    """
    query = update.message.text
    answer = retrieve_answer(query)
    update.message.reply_text(answer)

def run_bot():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    
    # Set up the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(os.getenv("PORT", "8443")),
                          url_path=TELEGRAM_BOT_TOKEN)
    updater.bot.set_webhook(WEBHOOK_URL + TELEGRAM_BOT_TOKEN)
    
    updater.idle()

if __name__ == '__main__':
    run_bot()

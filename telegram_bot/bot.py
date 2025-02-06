# telegram_bot/bot.py

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram_bot.doc_processing import retrieve_answer

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# Replace with your actual Telegram bot token.
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

def start(update, context):
    update.message.reply_text("Hello! Ask me anything about our documents.")

def handle_message(update, context):
    query = update.message.text
    answer = retrieve_answer(query)
    update.message.reply_text(answer)

def run_bot():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    run_bot()

import os
from telegram import Bot
from telegram.ext import Updater, CommandHandler
import schedule
import time
import threading

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = Bot(token=TOKEN)

def send_signal():
    message = "سیگنال امروز:\nجفت ارز: EUR/USD\nتحلیل: صعودی\nپیشنهاد: خرید\nتارگت: 1.1000\nاستاپ: 1.0900"
    bot.send_message(chat_id=CHAT_ID, text=message)

def start(update, context):
    update.message.reply_text("ربات فعال است!")

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    schedule.every().day.at("11:00").do(send_signal)

    thread = threading.Thread(target=run_schedule)
    thread.start()

    updater.start_polling()
    updater.idle()

if name == "__main__":
    main()
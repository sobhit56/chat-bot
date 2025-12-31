import telebot
import time

BOT_TOKEN = "8588176987:AAEyrrp0FzaVg1hbo2JCUvhSJuCQRnh7zKk"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Bot is running successfully!")

while True:
    try:
        print("Bot started...")
        bot.infinity_polling(timeout=20, long_polling_timeout=20)
    except Exception as e:
        print("Error occurred, restarting in 5 seconds...")
        time.sleep(5)
import telebot
import time
import threading

BOT_TOKEN = "8588176987:AAEyrrp0FzaVg1hbo2JCUvhSJuCQRnh7zKk"
bot = telebot.TeleBot(BOT_TOKEN)

user_ids = set()   # store users

        
        


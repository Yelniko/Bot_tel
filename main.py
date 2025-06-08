import telebot
from config import api_token

bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, message.chat.id)

@bot.message_handler(commands=['id'])
def id_chat(message):
    bot.send_message(message.chat.id, f'ID: {message.chat.id}')

@bot.message_handler(content_types=['text'])
def text(message):
    pass

if __name__ == "__main__":
    bot.infinity_polling()
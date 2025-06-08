import telebot
import datetime
from paris import char, char_1
# from time import sleep

bot = telebot.TeleBot('7362065990:AAGbuq3oN1oardFkGXYUZfCSN40UgGY2qjo')

@bot.message_handler(commands=['start', 'schedule'])
def schedule_message(message):
    number_1, number_2  = 0, 1

    data = datetime.date.today()
    data_now = data.weekday()

    if number_1 == 0:
        to_pin = bot.send_message(message.chat.id, char[data_now] , parse_mode='html').message_id
        bot.pin_chat_message(chat_id=message.chat.id, message_id=to_pin)
    else:
        to_pin = bot.send_message(message.chat.id, char_1[data_now], parse_mode='html').message_id
        bot.pin_chat_message(chat_id=message.chat.id, message_id=to_pin)


@bot.message_handler(commands=["tomorrow's_schedule", "tomorrow"])
def schedule_message(message):
    number_1, number_2, = 0, 1

    data = datetime.date.today()
    data_now = data.weekday()

    if number_1 == 0:
        to_pin = bot.send_message(message.chat.id, char[data_now+1], parse_mode='html').message_id
        bot.pin_chat_message(chat_id=message.chat.id, message_id=to_pin)
    else:
        to_pin = bot.send_message(message.chat.id, char_1[data_now+1], parse_mode='html').message_id
        bot.pin_chat_message(chat_id=message.chat.id, message_id=to_pin)

@bot.message_handler(commands=["test"])
def schedule_message(message):
    for i in range(5):
        bot.send_message(message.chat.id, char[i], parse_mode='html')

    for i in range(5):
        bot.send_message(message.chat.id, char_1[i], parse_mode='html')


if __name__ == "__main__":
    bot.infinity_polling()


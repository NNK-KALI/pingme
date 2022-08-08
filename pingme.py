import telebot
from os import environ

API_TOKEN = environ["TELEGRAM_API_TOKEN"]
ALERT_RECIEVER_ID = environ["TELEGRAM_ALERT_REC_ID"]
SECRET_CODE = environ["SECRET_CODE"]

bot = telebot.TeleBot(API_TOKEN)

# Handle /start 
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message( message.chat.id, "If You know who I am then you know me.", )


@bot.message_handler(commands=['ping'])
def ping_me(message):
    code = message.text
    code = code.strip("/ping ")
    code = code.strip()
    if code == SECRET_CODE:
        bot.send_message(ALERT_RECIEVER_ID, "U have got  an alert from  {}({}).".format(message.chat.id, message.chat.username))
        print("Encountered an alert from {} .".format(message.chat.id))



bot.infinity_polling()

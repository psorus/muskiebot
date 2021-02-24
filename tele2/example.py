import telebot
with open("../secret","r") as f:
    secret=f.read()


bot = telebot.TeleBot(secret)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.reply_to(message,str(dir(message.chat)))
        id=message.chat.id
        bot.send_message(id,"Hello World")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)

bot.polling()

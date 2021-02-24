import telebot

bot = telebot.TeleBot("1693773077:AAEAjptVHlL9id1Om435t4n3l98A9XuFUO8")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.reply_to(message,str(dir(message.chat)))
        id=message.chat.id
        bot.send_message(id,"Hello World")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)

bot.polling()

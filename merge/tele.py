import telebot
import numpy as np
import os
import asyncio
with open("../secret","r") as f:
    secret=f.read()


bot = telebot.TeleBot(secret)

perm=[]
if os.path.isfile("perma.npz"):
    perm=[int(zw) for zw in np.load("perma.npz")["q"]]

perm=set(perm)

def savep():
    np.savez_compressed("perma",q=[zw for zw in perm])

def scream(tex):
    for id in perm:
        bot.send_message(id,tex)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"You are now subscribed to musky bot. To stop your subscription, please enter /stop")
    id=message.chat.id
    perm.add(id)
    savep()

@bot.message_handler(commands=['stop'])
def stop_message(message):
    bot.reply_to(message,"You are now unsubscribed from musky bot. To renew your subscription, simply enter /start")
    id=message.chat.id
    perm.remove(id)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.reply_to(message,"Whats there to ask... He tweets, I write you. Use /start and /stop to manage your subscription")


#bot.polling()
def run_pol():
    bot.polling(none_stop=False, interval=0, timeout=20)

#asyncio.run(run_pol())
run_pol()


if __name__=="__main__":
    print("hi")





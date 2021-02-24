from telegram.ext import Updater, CommandHandler, MessageHandler,    Filters, InlineQueryHandler

with open("../secret","r") as f:
    secret=f.read()


def sayhi(bot, job):
    job.context.message.reply_text("hi")

def time(bot, update,job_queue):
    job = job_queue.run_repeating(sayhi, 5, context=update)

def main():
    updater = Updater(secret)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text , time,pass_job_queue=True))


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

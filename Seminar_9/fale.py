# from telegram import Bot
# from telegram.exp import Updater, C

# token1 = 5564736708:AAGdXYl50Iqt2i5w-bv_VZRymvFOrRxOvNg

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint


token1 = "5564736708:AAGdXYl50Iqt2i5w-bv_VZRymvFOrRxOvNg"

# bot = Bot(token="5564736708:AAGdXYl50Iqt2i5w-bv_VZRymvFOrRxOvNg")
# updater = Updater(token=token1)
# dispatcher = updater.dispatcher

# def start(update, contex):
#     contex.bot.send_message(update.effective_chat.id, "Hello1234")

A = 0
B = 1

bot = Bot(token="5564736708:AAGdXYl50Iqt2i5w-bv_VZRymvFOrRxOvNg5983035956:AAGXMRbVaKLvUn432Dc-qyV1SlanbcYjT_g")
updater = Updater(token=token1)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет \n Как дела?")
    return A

def howareu(update, context):
    text = update.message.text
    if 'хор' in text.lower():
        context.bot.send_message(update.effective_chat.id,"Я рад, что у вас всё хорошо")
    else:
        context.bot.send_message(update.effective_chat.id,"Не грусти, всё будет отлично")
    context.bot.send_message(update.effective_chat.id,"Какая у тебя погода?")
    return B

def weather(update, context):
    text = update.message.text
    context.bot.send_message(update.effective_chat.id,"У меня сегодня такая же погода")
    context.bot.send_message(update.effective_chat.id,"Мне пора бежать, пока!")


# def rand(update, contex):
#     contex.bot.send_message(update.effective_chat.id, f'{randint(1, 100)}')

# def default(update, contex):
#     contex.bot.send_message(update.effective_chat.id, "Я не умею разговаривать")

# def privet(update, contex):
#     text = update.message.text
#     if 'прив' in text.lower():
#         contex.bot.send_message(update.effective_chat.id, "И тебе привет мой дорогой друг")
#     else:
#         contex.bot.send_message(update.effective_chat.id, "Я тебя не понимаю")


start_handler = CommandHandler('start', start)
# random_handler = CommandHandler('random', rand)
# default_handler =  MessageHandler(Filters.voice, default)
# privet_handler =  MessageHandler(Filters.text, privet)



dispatcher.add_handler(start_handler)
# dispatcher.add_handler(random_handler)
# dispatcher.add_handler(default_handler)
# dispatcher.add_handler(privet_handler)


updater.start_polling()
updater.idle()

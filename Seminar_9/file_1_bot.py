# pip install python-telegram-bot==13.14 --- РЅСѓР¶РЅР°СЏ РІРµСЂСЃРёСЏ
# -------------------------------------------------------------------------
# РџРѕСЃР»Рµ СЌС‚РѕРіРѕ РЅСѓР¶РЅРѕ Р±СѓРґРµС‚ СЂР°СЃСЃРєР°Р·Р°С‚СЊ

# from telegram import Bot
# from telegram.ext import Updater, CommandHandler


# bot = Bot(token="5564736708:AAGdXYl50Iqt2i5w-bv_VZRymvFOrRxOvNg")
# updater = Updater(token="5564736708:AAGdXYl50Iqt2i5w-bv_VZRymvFOrRxOvNg")
# dispatcher = updater.dispatcher


# def start(update, context):
#     context.bot.send_message(update.effective_chat.id, 'Hello, Dmitriy1989')


# start_handler = CommandHandler('start', start)
# dispatcher.add_handler(start_handler)


# updater.start_polling()
# updater.idle()

# -------------------------------------------------------------------------
# # python anywhere --- РґР»СЏ СЂР°Р·РІРѕСЂР°С‡РёРІР°РЅРёСЏ СЃРІРѕРµРіРѕ СЃРµСЂРІРµСЂР°
# -------------------------------------------------------------------------
# from telegram import Bot, Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# from random import randint as rd


# bot = Bot(token="5564736708:AAGdXYl50Iqt2i5w-bv_VZRymvFOrRxOvNg")
# updater = Updater(token="5564736708:AAGdXYl50Iqt2i5w-bv_VZRymvFOrRxOvNg")
# dispatcher = updater.dispatcher


# def start(update, context):
#     context.bot.send_message(update.effective_chat.id, 'Hello')


# def rand(update, context):
#     context.bot.send_message(update.effective_chat.id, f'{rd(1, 100)}')


# def voice(update, context):
#     context.bot.send_message(update.effective_chat.id, 'Я не знаю таких команд :(')


# start_handler = CommandHandler('start', start)
# random_handler = CommandHandler('random', rand)
# message_handler = MessageHandler(Filters.command, voice)

# dispatcher.add_handler(start_handler)
# dispatcher.add_handler(random_handler)
# dispatcher.add_handler(message_handler)


# updater.start_polling()
# updater.idle() # ctrl + c
# ------------------------------------------------------------------------
# # Р”РѕР±Р°РІРёРј СЂРµР°РіРёСЂРѕРІР°РЅРёРµ РЅР° РІРІРѕРґРёРјС‹Рµ СЃР»РѕРІР°
# ------------------------------------------------------------------------
# from telegram import Bot, Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# from random import randint as rd

# token = '5564736708:AAGdXYl50Iqt2i5w-bv_VZRymvFOrRxOvNg'
# bot = Bot(token)
# updater = Updater(token)
# dispatcher = updater.dispatcher


# def start(update, context):
#     context.bot.send_message(update.effective_chat.id, 'Hello')


# def rand(update, context):
#     context.bot.send_message(update.effective_chat.id, f'{rd(1, 100)}')



# def voice(update, context):
#     text = update.message.text
#     if 'РїСЂРёРІ' in text.lower():
#         context.bot.send_message(update.effective_chat.id, 'Р С‚РµР±Рµ РїСЂРёРІРµС‚, РјРѕР№ РґРѕСЂРѕРіРѕР№ РґСЂСѓРі!')
#     else:
#         context.bot.send_message(update.effective_chat.id, 'РЇ С‚РµР±СЏ РЅРµ РїРѕРЅРёРјР°СЋ :(')


# start_handler = CommandHandler('start', start)
# random_handler = CommandHandler('random', rand)
# message_handler = MessageHandler(Filters.text, voice)

# dispatcher.add_handler(start_handler)
# dispatcher.add_handler(random_handler)
# dispatcher.add_handler(message_handler)


# updater.start_polling()
# updater.idle() 
# --------------------------------------------------------------------------------------------
# # Р”РѕР±Р°РІРёРј РЅРµР±РѕР»СЊС€РѕР№ РґРёР°Р»РѕРі
# --------------------------------------------------------------------------------------------
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint as rd
from file_3 import stroka

token = '5564736708:AAGdXYl50Iqt2i5w-bv_VZRymvFOrRxOvNg'
bot = Bot(token)
updater = Updater(token)
dispatcher = updater.dispatcher


A = 0
B = 1


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет \n Как дела?')
    return A


def howareyou(update, context):
    text = update.message.text
    if 'хор' in text.lower():
        context.bot.send_message(update.effective_chat.id, 'Я рад, что у вас всё хорошо')
    else:
        context.bot.send_message(update.effective_chat.id, 'Не грусти, всё будет отлично')
    context.bot.send_message(update.effective_chat.id, 'Какая у тебя погода?')
    return B

def weather(update, context):
    text = update.message.text
    context.bot.send_message(update.effective_chat.id, 'У меня сегодня така же погода')
    context.bot.send_message(update.effective_chat.id, 'Мне пора бежать, пока!')

    return ConversationHandler.END


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Что-то пошло не так!!!')


start_handler = CommandHandler('start', start)
howareyou_handler = MessageHandler(Filters.text, howareyou)
weather_handler = MessageHandler(Filters.text, weather)
cancel_handler = CommandHandler('cancel', cancel)
stroka_handler = MessageHandler(Filters.text, stroka)
# message_handler = MessageHandler(Filters.text, voice)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                    states={A: [howareyou_handler],
                                    B: [weather_handler]},
                                    fallbacks=[cancel_handler])
dispatcher.add_handler(conv_handler)
dispatcher.add_handler(stroka_handler)

updater.start_polling()
updater.idle() 
# --------------------------------------------------------------------------------------------


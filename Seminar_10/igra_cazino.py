# Задача1. Напишите бота - игра в казино.

from random import randint, choice
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = '5564736708:AAGdXYl50Iqt2i5w-bv_VZRymvFOrRxOvNg'
SEPARATOR = '--'
SEPARATOR_1 = '|'
updater = Updater(TOKEN)
bot = Bot(TOKEN)
dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id, 'Всем привет! Это игра в "Казино" \n\
Сделайте ставку')

def gameboard():
    board1 = ['⚽️', '⚽️','⚽️','⚽️', '🏀', '🏀','🏀','🏈','🏈','🎱']
    board2 = [choice(board1) for i in range(12)]
    
    return board2

def output_gamaboard(board2: list):
    """Возврвщает что то"""
    board_str: list = []
    board_str.append(SEPARATOR * 12)
    for i in range(0, len(board2),4):
        board_str.append(SEPARATOR_1.join(board2[i:i + 4]))
        board_str.append(SEPARATOR * 12)
    board_str = '\n'.join(board_str)
    return board_str

def win_coeeff(board2):
    total_coeff = 0
    coeff_dict = {
                  '⚽️': [1.5, 1],
                  '🏀': [2.5, 2],
                  '🏈': [3.5, 3],
                  '🎱': [4.5, 4],
                 }

    for i in range(len(board2), 4):
        if (board2[i] == board2[i+1] ==
            board2[i+2] == board2[i+3]):
            total_coeff += coeff_dict[board2[i]][0]
    
    for i in range(len(board2)// 3):
        if board2[i] == board2[i+4] == board2[i+8]:
            total_coeff += coeff_dict[board2[i]][1]
    return total_coeff

def game(update: Update, context: CallbackContext):
    bet = float(update.message.text)
    board = gameboard()
    context.bot.send_message(update.effective_chat.id,
                            output_gamaboard(board))
    context.bot.send_message(update.effective_chat.id,
                            win_coeeff(board)*bet)

start_handler = CommandHandler('start', start)
game_handler = MessageHandler(Filters.text, game)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(game_handler)

# ⚽️🏀🏈🎱
board = gameboard()
print(output_gamaboard(board))
print(win_coeeff(board))
updater.start_polling()
updater.idle()
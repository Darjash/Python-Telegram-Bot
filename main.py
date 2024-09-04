import telebot
import random
import os
from dotenv import load_dotenv

load_dotenv('.env')
token: str = os.getenv('TOKEN')

bot = telebot.TeleBot(token)

randNum = ""


def random_int():
    rand_num = ""
    while len(rand_num) < 4:
        num = str(random.randint(0, 9))
        if num not in rand_num:
            rand_num += num
    return rand_num


def number_is_unique(num):
    return len(set(num)) == 4


@bot.message_handler(commands=['start'])
def start(message):
    global randNum
    randNum = random_int()
    bot.send_message(message.chat.id, '<b>Welcome to Bulls and Cows game.'
                                      '\n'
                                      '\nRules: This bot generates 4-digit  number and you have to guess it. '
                                      '\nFor each guess, the bot provides feedback in terms of “cows” and “bulls”,'
                                      ' where “cows” represent correct digits in the wrong position, '
                                      'and “bulls” represent correct digits in the correct position. '
                                      '\n'
                                      '\nStart guessing! Enter a 4 digit number!</b>', parse_mode='html')
    main()


@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, '\nThis bot generates 4-digit  number and you have to guess it. '
                                      '\nFor each guess, the bot provides feedback in terms of “cows” and “bulls”'
                                      '\nThe number of Bulls - numbers correct in the right position'
                                      '\nThe number of Cows - numbers correct but in the wrong position'
                                      '\nFor example, if generated number is "1854" and you guess "4879," the '
                                      'feedback from the bot is: bulls = 1 & cows = 1'
                                      '("8" is the bull, and "4" is the cow).')


def main():

    @bot.message_handler(func=lambda message: True)
    def message(message):
        global randNum
        player_num = message.text.replace(' ', '').replace('.', '').replace(',', '')

        if not player_num.isdigit():
            bot.send_message(message.chat.id, "The input you sent is not a number")
            return
        if len(player_num) != 4:
            bot.send_message(message.chat.id, "Enter a 4 digit number")
            return
        if not number_is_unique(player_num):
            bot.send_message(message.chat.id, "Enter a number with unique digits")
            return

        else:
            bulls = 0
            cows = 0
            for i in range(len(randNum)):
                if player_num[i] in randNum:
                    if player_num[i] == randNum[i]:
                        bulls += 1
                    else:
                        cows += 1
            bot.send_message(message.chat.id, f'Bulls= {bulls} & Cows= {cows}')
            if bulls == 4:
                bot.send_message(message.chat.id, 'YOU WON! :)'
                                                  '\nTO RESTART THE GAME PRESS /start')
                randNum = ""


bot.polling(none_stop=True)

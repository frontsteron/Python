# Добавьте в бота игру «Угадай числа». Бот загадывает число от 1 до 1000. 
# Когда игрок угадывает его, бот выводит количество сделанных ходов.

import telebot
import random
 
bot = telebot.TeleBot('TOKEN_BOT')
 
 
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, для начала игры "Угадай числа" жми на "/play"!')
 
 
@bot.message_handler(commands=['play'])
def guess_number(message):
    guesses_made = 0
    guesses_mademax = 10
    the_number = random.randint(0, 1000)
    bot.send_message(message.chat.id, 'Я загадал число от 0 до 1000!' 'У тебя есть {0} попыток, чтобы отгадать его'.format(guesses_mademax))
    bot.send_message(message.chat.id, "Вводи число..")
 
    while guesses_made < guesses_mademax: #главное условие
        guess = int(message.text.lower())
        if guess < the_number:
            bot.send_message(message.chat.id, 'Твое число меньше того, что я загадал.')
            guesses_made += 1
        if guess > the_number:
            bot.send_message(message.chat.id, 'Твое число больше того, что я загадал.')
            guesses_made += 1
        if guess == the_number:
            bot.send_message(message.chat.id,
                                 'Ты угадал число, использовав {0} попыток!'.format(guesses_made))
        else:
            bot.send_message(message.chat.id, 'А вот и не угадал! Я загадал число {0}'.format(the_number))
 
 
bot.polling(none_stop=True)
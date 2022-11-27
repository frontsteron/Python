# Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

import telebot

bot = telebot.TeleBot('TOKEN_BOT')

@bot.message_handler(commands=['start', 'help', 'Привет', 'Здравствуйте'])
def send_welcome(message):
	print(message) #вывод всю информацию о пользователе в консоль
	bot.reply_to(message, "Здравствуйте! Вас приветствует Бот техподдержки 'Банка №1', если хотите сообщить о потере карты, то напишите /ЯПотерялКарту, если хотите заблокировать крату, то напишите /ЗаблокироватьКарту и следующим сообщением напишите её номер")

@bot.message_handler(commands=['ЯПотерялКарту'])
def send_answer1(message):
	bot.reply_to(message, "Заблокируйте карту, для этого напишите /ЗаблокироватьКарту")

@bot.message_handler(commands=['ЗаблокироватьКарту'])
def send_answer2(message):
	bot.reply_to(message, "Напишите номер карты и в скором времени карта будет заблокирована")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	data = open('expense.txt', 'a+', encoding='utf-8')
	data.writelines(message.text + '\n')
	data.close

bot.infinity_polling()
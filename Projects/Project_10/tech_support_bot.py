# Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.
# Добавьте боту модуль, который позволяет считывать из файла вопрос, отвечать на него и отправлять ответ обратно пользователю.

import telebot

bot = telebot.TeleBot('TOKEN_BOT')

@bot.message_handler(content_types=['text'])
def send_welcome(message):
	if 'Привет' in message.text:
		print(message) #вывод всю информацию о пользователе в консоль
		bot.reply_to(message, "Здравствуйте, " + message.from_user.first_name + ". Вас приветствует Бот техподдержки 'Банка №1', если хотите сообщить о потере карты, то напишите Я потерял карту, если хотите заблокировать крату, то напишите Заблокировать карту и следующим сообщением напишите её номер")
	if 'Я потерял карту' in message.text:
		bot.reply_to(message, "Заблокируйте карту, для этого напишите Заблокировать карту")
	if 'Заблокировать карту' in message.text:
		bot.reply_to(message, "Напишите номер карты и в скором времени карта будет заблокирована")
	data = open('expense.txt', 'a+', encoding='utf-8')
	data.writelines(message.text + '\n')
	data.close

bot.infinity_polling()
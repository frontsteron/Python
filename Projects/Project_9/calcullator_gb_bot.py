# Добавьте telegram-боту возможность вычислять выражения: 1 + 4 * 2 -> 9

# Доброго дня, Денис Владимирович! Отличный калькулятор получился, правда, функции удаления записей надо будет ещё доделать.

import telebot

bot = telebot.TeleBot('TOKEN_BOT')

value = ''
old_value = ''

Keyboard = telebot.types.InlineKeyboardMarkup()
Keyboard.row(  telebot.types.InlineKeyboardButton(' ', callback_data='no'),
               telebot.types.InlineKeyboardButton('C ', callback_data='C '),
               telebot.types.InlineKeyboardButton('<= ', callback_data='<= '),
               telebot.types.InlineKeyboardButton('/ ', callback_data='/ ') )

Keyboard.row(  telebot.types.InlineKeyboardButton('7', callback_data='7'),
               telebot.types.InlineKeyboardButton('8', callback_data='8'),
               telebot.types.InlineKeyboardButton('9', callback_data='9'),
               telebot.types.InlineKeyboardButton('*', callback_data='*') )

Keyboard.row(  telebot.types.InlineKeyboardButton('4', callback_data='4'),
               telebot.types.InlineKeyboardButton('5', callback_data='5'),
               telebot.types.InlineKeyboardButton('6', callback_data='6'),
               telebot.types.InlineKeyboardButton('-', callback_data='-') )

Keyboard.row(  telebot.types.InlineKeyboardButton('1', callback_data='1'),
               telebot.types.InlineKeyboardButton('2', callback_data='2'),
               telebot.types.InlineKeyboardButton('3 ', callback_data='3 '),
               telebot.types.InlineKeyboardButton('+', callback_data='+') )

Keyboard.row(  telebot.types.InlineKeyboardButton(' ', callback_data='no'),
               telebot.types.InlineKeyboardButton('0', callback_data='0'),
               telebot.types.InlineKeyboardButton(',', callback_data='.'),
               telebot.types.InlineKeyboardButton('=', callback_data='=') )

@bot.message_handler(commands=['start', 'calculater'])
def getMessage(message):
   global value
   if value == '':
      bot.send_message(message.from_user.id, '0', reply_markup=Keyboard)
   else:
      bot.send_message(message.from_user.id, value, reply_markup=Keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
   global value, old_value
   data = query.data

   if data == 'no':
      pass
   elif data == 'C':
      value =''
   elif data == '<=':
      if value != '':
         value = value[:len(value)-1]
   elif data =='=':
      try:
         value = str( eval(value) )
      except:
         value = 'Error!'
   else:
      value += data

   if ( value != old_value and value !='' ) or ( '0' != old_value and value == '' ):
      if value == '':
         bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=Keyboard)
         old_value = '0'
      else:
         bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=Keyboard)
         old_value = value

   old_value = value
   if value == 'Error!': value = ''


bot.polling(none_stop=False, interval=0)
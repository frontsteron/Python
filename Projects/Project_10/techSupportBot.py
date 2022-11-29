import telebot
import os
from fuzzywuzzy import fuzz

bot = telebot.TeleBot('TOKEN_BOT')

# Загружаем список фраз и ответов в массив

mas=[]
if os.path.exists('https://github.com/frontsteron/Python/blob/main/Projects/Project_10/dialog.txt'):
    f=open('https://github.com/frontsteron/Python/blob/main/Projects/Project_10/dialog.txt', 'r', encoding='UTF-8')
    for x in f:
        if(len(x.strip()) > 2):
            mas.append(x.strip().lower())
    f.close()

# определяем наиболее похожую фразу и выдаем в качестве ответа следующий элемент списка
def answer(text):
    try:
        text=text.lower().strip()
        if os.path.exists('https://github.com/frontsteron/Python/blob/main/Projects/Project_10/dialog.txt'):
            a = 0
            n = 0
            nn = 0
            for q in mas:
                if('u: ' in q):
                    # Изучаем, насколько похожи две строки
                    aa=(fuzz.token_sort_ratio(q.replace('u: ',''), text))

                    if(aa > a and aa!= a):
                        a = aa
                        nn = n
                n = n + 1
            s = mas[nn + 1]
            return s

        else:
            return 'Не смог'

    except:
        return 'Ошибка'

@bot.message_handler(commands=["start"])
def start(m, res=False):
        bot.send_message(m.chat.id, 'Давай поболтаем. Например, напиши мне Привет!')

# получение сообщений от клиента
@bot.message_handler(content_types=["text"])
def handle_text(message):

    s=answer(message.text)

    bot.send_message(message.chat.id, s)

bot.polling(none_stop=True, interval=0)
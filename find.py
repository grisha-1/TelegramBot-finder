# -*- coding: utf-8 -*-
import telebot
import re
import wikipedia

bot = telebot.TeleBot('Здесь пропишите токен бота')

wikipedia.set_lang('ru')


def getwiki(s):
    try:
        ny = wikipedia.page(s)  # поиск
        wikitext = ny.content[:1000]  # 1000 символов
        wikimas = wikitext.split('.')  # разделяем строку по точкам
        wikimas = wikimas[:-1]
        wikitext2 = ''  # пусто

        for x in wikimas:
            if not ('==' in x):

                if len((x.strip())) > 3:
                    wikitext2 = wikitext2 + x + '.'
                else:
                    break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)

        return wikitext2
    except Exception as e:
        return 'В энциклопедии нет этого:`('


@bot.message_handler(commands=['start'])
def star(m, res=False):
    bot.send_message(m.chat.id, 'отправь, что-либо, а я поищу на википедии')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))
    print(message)


bot.polling(none_stop=True, interval=0)

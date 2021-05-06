# Используя библиотеку pyTelegramBotAPI напишите телеграм-бота, который ждет от пользователя команду /game.
# При получении этой команды, бот заходит на страницу бесплатных игр на сайте Steam (https://store.steampowered.com/genre/Free%20to%20Play/),
# находит таблицу игр, выбирает из таблицы случайную игру и выводит пользователю ее название и список тегов.
# Используйте re.findall для того, чтобы обнаружить пользовательские команды.

# Обращаемся к модулю беблиотеки
import telebot
import re
import random
import requests
from bs4 import BeautifulSoup

# Сохраняем наш токен
token = 'token'

# Создаем бот
bot = telebot.TeleBot(token)


# Добавляем функционал, для этого используем уже определенный в библиотеке декоратор, который работает с командами
@bot.message_handler(content_types=['text'])
def search_game(message):
    tickers = re.findall('game', message.text)
    if tickers:
        for t in tickers:
            url = 'https://store.steampowered.com/genre/Free%20to%20Play'
            soup = BeautifulSoup(requests.get(url).text, 'html.parser')
            games = soup.find_all('div', class_='tab_item_content')
            games_dic = {}
            for game in games:
                game_name = game.find_all('div', class_='tab_item_name')[0].text
                game_tags = game.find_all('span', class_='top_tag')
                game_tags_list = []
                for tag in game_tags:
                    game_tags_list.append(tag.text)
                games_dic[game_name] = game_tags_list
            game_chosen = random.choice(list(games_dic.keys()))
            bot.reply_to(message, 'Игра: {}, теги: {}'.format(game_chosen, ''.join(games_dic[game_chosen])))
    else:
        bot.send_message(message.chat.id, 'Для того чтобы получить игру введите команду game')


# Мониторим телеграм канал с заданным токеном
bot.infinity_polling()

# На этой же странице найдите и обработайте таблицу игр:
# Используйте функцию Inspect Element в вашем браузере, чтобы понять, какие теги и классы вам нужно обрабатывать.
# Составьте и распечатайте словарь игр и их тегов. Например, {'Incremental Epic Breakers': ['2D Platformer', ', Puzzle Platformer', ', Idler', ', Destruction'], ... }


import requests
from bs4 import BeautifulSoup

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


print(games_dic)

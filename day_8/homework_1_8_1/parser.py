# С помощью библиотек requests и bs4 прочитайте содержимое страницы бесплатных игр на сайте Steam
# Получите все ссылки (тег <a href = ‘...’>), для каждой ссылки получите текст ссылки и url.
# Сформируйте словарь, состоящий только из тех ссылок, у которых в тексте встречается фраза “Free To Play”.
# Выведите словарь на экран.


import requests
from bs4 import BeautifulSoup

url = 'https://store.steampowered.com/genre/Free%20to%20Play'

soup = BeautifulSoup(requests.get(url).text, 'html.parser')

links = soup.find_all('a')
dic_free_game = {}

for element in links:
    if element.text.find('Free To Play') > 0:
        dic_free_game[element.text] = element.get('href')

print(dic_free_game)

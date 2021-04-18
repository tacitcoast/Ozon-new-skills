# На этой же странице, с помощью requests и bs4 найдите и обработайте раздел тегов:
# Сформируйте словарь, в котором ключами будут имена тегов, а значениями - количества игр, относящихся к этим тегам. Например: {‘Indie’: 2355, ... }
# Обратите внимание, что теги можно найти вот по такому bs-запросу: .find_all('div', class_ = 'tag_count_button')


import requests
from bs4 import BeautifulSoup

url = 'https://store.steampowered.com/genre/Free%20to%20Play'

soup = BeautifulSoup(requests.get(url).text, 'html.parser')

tags = soup.find_all('div', class_='tag_count_button')

tags_dic = {}

for tag in tags:
    tag_name = tag.find_all('span', class_='tag_name')[0].text
    tag_count = tag.find_all('span', class_='tag_count')[0].text
    tags_dic[tag_name] = tag_count

print(tags_dic)

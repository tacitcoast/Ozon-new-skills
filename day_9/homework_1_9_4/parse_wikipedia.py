# Спомощью re и BeautifulSoup исследуйте страницу Википедии, посвященную премии “Небьюла” (https://ru.wikipedia.org/wiki/Небьюла).
# Соберите все ссылки на этой странице.
# Отфильтруйте только те, не ведут на страницы Википедии.

import requests
from bs4 import BeautifulSoup
import re

url = 'https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B1%D1%8C%D1%8E%D0%BB%D0%B0'

soup = BeautifulSoup(requests.get(url).text, 'html.parser')

links = soup.find_all('a')

for element in links:
    url = element.get('href')
    if url == None:
        continue
    result = re.search('^\/wiki\/|wikipedia', url)
    if result:
        print(url)

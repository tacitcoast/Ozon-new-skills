# В приложении к уроку задан файл lesson09_cats_of_ulthar.txt.
# С помощью библиотеки re посчитайте сколько раз в нем встречается слово “кошка” в любой форме.

import re

text_string = ''
cats_count = 0

with open('lesson09_cats_of_ulthar.txt', encoding='utf-8') as file:
    text_string = file.read()

cats_count = len(re.findall('кошк', text_string))

print(cats_count)

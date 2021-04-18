# Используйте таблицу ближайших к Земле галактик lesson09_closest_galaxies.csv.
# С помощью re.search отберите те галактики, которые имеют отношение к созвездию Андромеды и имеют данные о расстоянии до Земли.
# Соберите эти галактики в список словарей вот в таком формате:
# [{'Название': 'Карликовая сфероидальная галактика в Пегасе (DDO 216)', 'Расстояние': 3.0, 'Примечания': 'Спутник Андромеды'}, ...]
# Обратите внимание, что расстояние до Земли должно быть конвертировано в тип float.
# Отсортируйте полученный список по возрастанию расстояния до Земли.

import re

galaxies = []
galaxies_list = []

with open('lesson09_closest_galaxies.csv', encoding='utf-8') as file:
    for line in file:
        galaxies.append(line.split(','))

for line in galaxies:
    notes = line[3]
    distance = line[2]
    # Отбераем те галактики, которые имеют отношение к созвездию Андромеды (из Примечаний)
    result_name = re.search('Андромеды', notes)
    # Отбераем те галактики, которые имеют данные о расстоянии до Земли
    result_distance = re.search('^[0-9.]+', distance)
    if result_name and result_distance:
        # Собераем эти галактики в словари
        galaxies_dic = {'Название': line[0], 'Расстояние': float(result_distance[0]), 'Примечания': notes}
        # Добавляем словари в список
        galaxies_list.append(galaxies_dic)

# Сортируем список по полю расстояния до Земли
print(sorted(galaxies_list, key=lambda row: row['Расстояние']))

# В приложении к заданию находится рассказ “Кошки Ультара” Говарда Лавкрафта (файл lesson06_cats_of_ulthar.txt). Напишите программу, которая:
# - Открывает файл и считывает данные;
# - Подсчитывает сколько раз в файле встречается слово “кошка” и выводит это число на экран;
# - Находит все строки, в которых встречается слово “кошка” и выводит эти строки на экран.

cat = 0
strings = []
res = []

# Читаем файл, добавляем в переменную количество найденных слов "кошка" и создаем список со строками, где есть слово "кошка"
with open(' lesson06_cats_of_ulthar.txt', encoding='utf-8') as file:
    for line in file:
        for word in line.split():
            if word == 'кошка':
                cat += 1
                strings.append(line)

# При помощи цикла убираем дубли строк
for i in strings:
    if i not in res:
        res.append(i)

# При помощи цикла выводим каждый элемент в отдельной строке
for i in res:
    print(i)

# Выводим общее количество слов "кошка"
print(cat)
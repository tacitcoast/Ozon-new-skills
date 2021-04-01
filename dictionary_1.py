# В приложении задан словарь с названиями и жанрами сериалов shows.
# Выведите на экран жанр для сериала “Ведьмак”.
# Напишите два цикла - один из них должен распечатывать только названия сериалов, второй только жанры.
# Подумайте какой из циклов здесь уместно использовать и почему.

shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма', 'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}

# Выводим на экран жанр для сериала "Ведьмак"
print('Жанр сериала "Ведьмак":', shows['Ведьмак'])

# Первый цикл распечатывает только названия сериалов (уместен for, т.к. интерируется по всем значениям, а для while необходимо условие и программа будет длиннее)
for i in shows.keys():
    print(i)

# Второй цикл распечатывает только жанры
for i in shows.values():
    print(i)
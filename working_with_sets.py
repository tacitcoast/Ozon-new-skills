anya = {'Секретные материалы': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
olya = {'Клан Сопрано': 'криминал', '24': 'драма', 'Во все тяжкие': 'криминал', 'Карточный домик': 'драма'}
nastya = {'Ведьмак': 'фэнтази', 'Игра престолов': 'фэнтази'}
sveta = {'Черное зеркало': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}

# Создаем списки из ключей для последующего сравнения и переводим их в множества
list_anya = set(anya.keys())
list_olya = set(olya.keys())
list_nastya = set(nastya.keys())
list_sveta = set(sveta.keys())

# Сравниваем с кем из коллег у Ани больше всего общих любимых сериалов, с помощью len вычисляем количество
olya_count = len(list_anya & list_olya)
nastya_count = len(list_anya & list_nastya)
sveta_count = len(list_anya & list_sveta)

# Создаем новый список с именами и количеством пересечений
list_intersections = {'Оля': olya_count,
                     'Настя': nastya_count,
                     'Света': sveta_count}

# Выводим результат
print('У Ани с Олей общих сериалов: ', olya_count, ', У Ани с Настей общих сериалов: ', nastya_count, ', У Ани со Светой общих сериалов: ', sveta_count)

max_list_intersection = 0
name = ''

# С помощтю цикла находим с кем больше всего пересечений
for key, value in list_intersections.items():
    if list_intersections[key] > max_list_intersection:
        total = list_intersections[key]
        name = key

# Выводим результат
print('У Ани больше всего общих любимых сериалов с', name)
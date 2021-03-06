# В приложении заданы словари с названиями, рейтингами и жанрами сериалов shows и ratings.
# Напишите программу, которая рассчитывает средний рейтинг для сериалов с жанром “фантастика”.

shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма', 'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98, 'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}

count = 0
sum_rating = 0

# Запускаем цикл, который ищет фильмы по жанру "фантастика"
for key, value in shows.items():
    if value == 'фантастика':
        # Считаем количество совпадений
        count += 1
        # Считаем сумму общего рейтинга
        sum_rating += ratings[key]

# Рассчитываем средний рейтинг для сериалов с жанром "фантастика"
avg_rating = sum_rating / count
print(avg_rating)
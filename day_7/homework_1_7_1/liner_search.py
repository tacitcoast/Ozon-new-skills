# В приложении к уроку задан список имен животных animals. Модифицируйте алгоритм линейного поиска таким образом, чтобы он находил все индексы указанного слова и возвращал список индексов.
# Например, для слова ‘жираф’ функция должна вернуть список [10, 12, 13, 16, 17, 19, 24, 26, 31, 38, 41]
# Вызовите получившуюся функцию для всех уникальных имен животных.


animals = ['питон', 'питон', 'кит', 'собака', 'питон', 'кит', 'кошка', 'горилла', 'кит', 'кошка', 'жираф', 'леопард', 'жираф', 'жираф', 'кошка', 'горилла', 'жираф', 'жираф', 'кошка', 'жираф', 'кошка', 'кошка', 'собака', 'кит',
'жираф', 'леопард', 'жираф', 'собака', 'кит', 'кит', 'кит', 'жираф', 'собака', 'собака', 'кит', 'питон', 'леопард', 'кошка', 'жираф', 'собака', 'кошка', 'жираф', 'кошка', 'собака', 'кит', 'леопард', 'леопард', 'горилла',
'горилла', 'кит']


def liner_search(animals, x):
    list_index = []
    for i in range(len(animals)):
        if animals[i] == x:
            list_index.append(i)

    return list_index


for i in set(animals):
    print(i)
    print(liner_search(animals, i))

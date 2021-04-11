# В приложении задана функция сортировки выбором, которая сортирует список и возвращаем время, затраченное на сортировку.
# Исследуйте, как увеличение размера сортируемого списка влияет на скорость сортировки.
# Возьмите вот такие размеры списка: 1000, 2000, 5000, 10000
# Напишите цикл, в котором перебираются размеры списков. Для каждого размера:
# - Генерируется список нужной длины, заполненный случайными целыми числами;
# - Полученный список сортируется функцией selection_sort;
# - Печатается размер списка и время сортировки.
# Какой вывод вы можете сделать по результатам работы программы? Добавьте вывод в комментарий к программе.


import random, time


def generate_list(n):
    res = []
    for i in range(n):
        res.append(random.randint(0, 10000))
    return res


def selection_sort(input_list):
    start_time = time.time()
    for i in range(len(input_list)):
        min_i = i
        for j in range(i + 1, len(input_list)):
            if input_list[min_i] > input_list[j]: min_i = j
        input_list[i], input_list[min_i] = input_list[min_i], input_list[i]
    return time.time() - start_time


list_1 = generate_list(1000)
list_2 = generate_list(2000)
list_3 = generate_list(5000)
list_4 = generate_list(10000)

print('Размер списка {}, время выполнения сортировки {:f}'.format(len(list_1), selection_sort(list_1)))
print('Размер списка {}, время выполнения сортировки {:f}'.format(len(list_2), selection_sort(list_2)))
print('Размер списка {}, время выполнения сортировки {:f}'.format(len(list_3), selection_sort(list_3)))
print('Размер списка {}, время выполнения сортировки {:f}'.format(len(list_4), selection_sort(list_4)))

# Время выполнения сортировки растет в геометрической прогрессии. Данный метод сортировки не очень удачный для больших списков.
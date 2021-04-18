import random

amount_of_bullets = int(input('Сколько патронов вы собираетесь вставить в револьвер?'))

baraban = [0, 0, 0, 0, 0, 0]

for i in range(amount_of_bullets):
    baraban[i] = 1

print('Посмотрите на барабан', baraban)

how_much = input('Сколько раз вы собираетесь нажать на курок?')
hm = int(how_much)
for i in range(hm):
    random.shuffle(baraban)
    print(baraban[0])
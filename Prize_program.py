import time
import random
print('Всем привет! Это простая программа, которая делаит розыгрыши среди участников')

people = []

amount = input('Введите, какое количество участников в розыгрыше: ')

for i in range(int(amount)):
    people.append(input("Имя " + str(i + 1) + " человека: "))

print("Программа проводит розыгрыш!")
for i in range(5):
    print(i)
    time.sleep(1) # опциональная строчка и импорт времени тоже опционален

print('Выиграл '+ random.choice(people)+'! Поздравляем его!')
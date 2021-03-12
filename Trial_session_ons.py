import random

while True:
  rand_value = random.randint(1, 30)

  while True:
    guess = int(input('Угадай число: '))
    print(guess)
    if rand_value == guess:
      print('Молодец! Ты победил.')
      break
    elif rand_value > guess:
      print('Возьми число побольше')
    else:
      print('Возьми число поменьше')

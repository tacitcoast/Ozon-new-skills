import random

deposit = 10000
journal = []

print('Добро пожаловать в виртуальное казино! Ваш стартовый депозит составляет', deposit, 'единиц.')
while deposit > 0:
    dice = random.randint(2, 12)
    guess = int(input('Программа бросила кубики. Сделайте вашу ставку: '))
    if dice == guess:
        deposit += 1000
        print('Вы угадали, вам сегодня явно везет! Ваша ставка:', guess, 'Ставка казино:', dice, 'Ваш счет составляет:', deposit, 'единиц')
        journal.append('Ваша ставка: ' + str(guess) + ', Ставка казино: ' + str(dice) + ', Ваш счет составляет ' + str(deposit) + ' единиц')

    elif guess > 12 or guess < 2:
        print('Вы не можете сделать такую ставку, пожалуйста, введите число от 2 до 12')

    elif dice != guess:
        deposit -= 1000
        print('Вы не угадали. Ваша ставка:', guess, 'Ставка казино:', dice, 'Ваш счет составляет', deposit, 'единиц')
        journal.append('Ваша ставка: ' + str(guess) + ', Ставка казино: ' + str(dice) + ', Ваш счет составляет ' + str(deposit) + ' единиц')

print('К сожалению, вы проиграли, ваш счет составляет', deposit, 'единиц. Вы можете начать игру заного')

for i in journal:
    print(i)

max_num = 9

for i in range(0, max_num):
    number1 = i + 1
    for j in range(0, max_num):
        number2 = j + 1
        result = number1 * number2
        print(number1, '*', number2, '=', result)

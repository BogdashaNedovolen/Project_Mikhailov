"""
Ввести 4 числа. Найти и вывести на экран количество четных чисел.
"""

one, two, three, four = input('Введите первое число: '), input('Введите второе число: '), input('Введите третье число: '), input('Введите четвёртое число: ')

while type(one) != int:
    try:
        one = int(one)
    except Exception as e:
        print('Неверный ввод числа..')
        one = input('Введите первое число: ')
        
while type(two) != int:
    try:
        two = int(two)
    except Exception as e:
        print('Неверный ввод числа..')
        two = input('Введите второе число: ')

while type(three) != int:
    try:
        three = int(three)
    except Exception as e:
        print('Неверный ввод числа..')
        three = input('Введите третье число: ')
        
while type(four) != int:
    try:
        four = int(four)
    except Exception as e:
        print('Неверный ввод числа..')
        four = input('Введите четвертое число: ')


count_numbers = 0
i = 1

while i <= 4:
    if i == 1:
        number = one
    if i == 2:
        number = two
    if i == 3:
        number = three
    if i == 4:
        number = four
    if i == 5:
        break

    if number % 2 == 0:
        count_numbers += 1
    
    i += 1
    
print(f'Кол-во четных чисел: {count_numbers}')

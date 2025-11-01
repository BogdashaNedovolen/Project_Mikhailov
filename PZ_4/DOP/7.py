"""
Даны два целых числа A и B (A < B). Вывести в порядке убывания все целые числа,
расположенные между A и B (вкл. сами числа A и B), а также количество этих
чисел (исп. оператор цикла)
"""

A, B = input('Введите первое число: '), input('Введите второе число: ')

while type(A) != int:
    try:
        A = int(A)
        break
    except ValueError:
        print("Неправильно ввели!")
        A = input("Введите первое число: ")

while type(B) != int:
    try:
        B = int(B)
        break
    except ValueError:
        print("Неправильно ввели!")
        B = input("Введите второе число: ")

if A >= B:
    print('Ошибка: A должно быть меньше B.')
else:
    count = 0
    current = B

    print('Числа в порядке убывания:', end=' ')

    while current >= A:
        print(current, end=' ')
        count += 1
        current -= 1
    
    print()
    print('Количестов чисел:', count)

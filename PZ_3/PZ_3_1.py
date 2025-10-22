"""
Даны два целых числа A и B. Проверить истинность высказывания: Ровно одно
из чисел A и B чётное.
"""

A = input('Введите число A: ')
B = input('Введите число B: ')

while type(A) != int:
    try:
        A = int(A)
    except Exception as e:
        print('Неверный ввод числа..')
        A = input('Введите число A: ')
        
while type(B) != int:
    try:
        B = int(B)
    except Exception as e:
        print('Неверный ввод числа..')
        B = input('Введите число B: ')
        

if (A % 2 == 0 and B % 2 != 0) or (A % 2 != 0 and B % 2 == 0):
    print(f'Высказывание верно, одно из чисел A и B чётное.\nЧисла: {A} и {B}')
elif (A % 2 == 0 and B % 2 == 0):
    print(f'Высказывание неверно, оба числа чётные.\nЧисла: {A} и {B}')
elif (A % 2 != 0 and B % 2 != 0):
    print(f'Высказывание неверно, оба числа нечётные.\nЧисла: {A} и {B}.')
else:
    print('Ошибка..')

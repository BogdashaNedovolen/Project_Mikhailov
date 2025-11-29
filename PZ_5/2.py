"""
Описать функцию MinMax(x, y), записывающую в еременную Х минимальное из значений Х и У,
 а в переменную У - максимальное из этих значений(Х и У - вещественные парметры,
 являющиеся одновременно входными и выхоными). Испольуя четыре вызова этой функции,
 найти минимальное и максимальное из данных чисел A, B, C, D.
"""

def MinMax(x, y):
    global mn_val, mx_val

    if x < y:
        mn_val = x
        mx_val = y
    else:
        mn_val = y
        mx_val = x

A, B, C, D = input('Введите число A: '), input('Введите число B: '), input('Введите число C: '), input('Введите число D: '), 

while type(A) != int:
    try:
        A = int(A)
    except Exception as e:
        print('Неверный ввод числа..')
        A = input('Введите первое число: ')
        
while type(B) != int:
    try:
        B = int(B)
    except Exception as e:
        print('Неверный ввод числа..')
        B = input('Введите второе число: ')

while type(C) != int:
    try:
        C = int(C)
    except Exception as e:
        print('Неверный ввод числа..')
        C = input('Введите третье число: ')
        
while type(D) != int:
    try:
        D = int(D)
    except Exception as e:
        print('Неверный ввод числа..')
        D = input('Введите четвертое число: ')


i = 1
mn_cur = A
mx_cur = A


while i <= 3:
    if i == 1:
        MinMax(mn_cur, B)
        mn_cur = mn_val
        MinMax(mx_cur, B)
        mx_cur = mx_val
    elif i == 2:
        MinMax(mn_cur, C)
        mn_cur = mn_val
        MinMax(mx_cur, C)
        mx_cur = mx_val
    elif i == 3:
        MinMax(mn_cur, D)
        mn_cur = mn_val
        MinMax(mx_cur, D)
        mx_cur = mx_val

    i += 1

print(f'Минимальное число из A, B, C, D - {mn_cur}.\nМаксимальное число - {mx_cur}')

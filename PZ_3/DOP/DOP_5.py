"""
Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2.
"""

one, two = input('Введите первое число: '), input('Введите второе число: ')

while type(one) != int:
    try:
        one = int(one)
    except ValueError:
        print('Неправильно введено первое число.')
        one = input('Введите первое число: ')
        
while type(two) != int:
    try:
        two = int(two)
    except ValueError:
        print('Неправильно введено второе число.')
        two = input('Введите первое число: ')
        
multiplication = one + two
        
if (multiplication % 5) == 0:
    multiplication += 1
else:
    multiplication -= 2
    
print(f'Итоговое число: {multiplication}')
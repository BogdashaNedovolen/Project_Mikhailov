"""
Ввести 2 числа. Если их произведение отрицательно, 
умножить его на 8, в противном случае увеличить его в 1.5 раза.
"""
one, two = input('Введите первое число: '), (input('Введите второе число: '))

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
        

multiplicate = one * two

if multiplicate < 0:
    final_multiplicate = multiplicate * 8
elif multiplicate == 0:
    final_multiplicate = 0
elif multiplicate > 0:
    final_multiplicate = multiplicate * 1.5

print(f'Итоговое число: {final_multiplicate}')
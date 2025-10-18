"""
Дано целое число. Если оно является положительным, 
то прибавить к нему 20, в противном случае вычесть из него 5.
"""

number = input(f'Введите число: ')

while type(number) != int:
    try:
        number = int(number)
    except ValueError:
        print('Неправильно введено число.')
        number = input('Введите число: ')


if number > 0:
    number += 20
elif number < 0:
    number -= 20
else:
    number = 0
    
print(f'Итоговое число: {number}')

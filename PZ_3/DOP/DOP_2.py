"""
Ввести число. Если оно четное, разделить его на 4, 
если нечетное - умножить на 5.
"""

one = input('Введите первое число: ')

while type(one) != int:
    try:
        one = int(one)
    except ValueError:
        print('Неправильно введено первое число.')
        one = input('Введите первое число: ')
        
if one % 2 == 0:
    preparation = one / 4
if one % 2 != 0:
    preparation = one * 5
    
print(f'Итоговое число: {preparation}')

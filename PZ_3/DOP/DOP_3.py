"""
Ввести двухзначное число. Если сумма цифр числа четная, 
то увеличить число на 2, в противном случае уменьшить на 2.
"""

number = input('Введите число: ')

while type(number) != int:
    try:
        number = int(number)
    except ValueError:            
        print('Неправильно введено число.')
        number = input('Введите число: ')
        


while len(str(number)) != 2:
    try:
        print('Неправильно введено число.')
        number = int(input('Введите число: '))
    except ValueError:            
        print('Неправильно введено число.')
        number = int(input('Введите число: '))


first_symb_number = number // 10
second_symb_number = number % 10
    
if ((first_symb_number + second_symb_number) % 2) == 0:
    number += 2
else:
    number -= 2
        
    print(f'Итоговое число: {number}')
    
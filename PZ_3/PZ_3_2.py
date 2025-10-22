"""
Дан номер месяца - число в диапазоне 1-12.
Определить количество дней в этом месяце для невисокосного года.
"""

month_number = input('Введите номер месяца: ')

while type(month_number) != int:
    try:
        month_number = int(month_number)
    except ValueError:
        print('Неправильно введено второе число.')
        month_number = input('Введите первое число: ')

while (month_number > 12) or (month_number < 1):
    try:
        print(f'Неверно указан номер месяца..')
        month_number = input('Введите номер месяца: ')
        
        while type(month_number) != int:
            try:
                month_number = int(month_number)
            except ValueError:
                print('Неправильно введено второе число.')
                month_number = input('Введите первое число: ')
                
    except ValueError as e:
        pass



if month_number == 1 or month_number == 3 or month_number == 5 or month_number == 7 or month_number == 8 or month_number == 10 or month_number == 12:
    print('Количество дней в указанном месяце - 31')
elif month_number == 2:
    print('Количество дней в указанном месяце - 28')
elif month_number == 3:
    print('Количество дней в указанном месяце - 31')
elif month_number == 4 or month_number == 6 or month_number == 9 or month_number == 11:
    print('Количество дней в указанном месяце - 3')

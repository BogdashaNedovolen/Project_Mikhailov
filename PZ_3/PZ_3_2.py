"""
Дан номер месяца - число в диапазоне 1-12.
Определить количество дней в этом месяце для невисокосного года.
"""
try:
    days_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    month_number = input('Введите номер месяца: ')
    
    while type(month_number) != int:
        try:
            month_number = int(month_number)
        except Exception as e:
            print(f'Что то пошло не так.({e})')
            month_number = input('Введите номер месяца: ')
    
    while (month_number > 12) or (month_number < 1):
        try:
            raise ValueError()
        except ValueError as e:
            print(f'Неверно указан номер месяца..')
            month_number = input('Введите номер месяца: ')
    
    print(f'Количество дней в указанном месяце - {days_list[month_number-1]}')
    
except Exception as e:
    print(f'Что-то пошло не так. {e}')
    

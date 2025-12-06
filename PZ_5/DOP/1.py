"""
Даны три целых числа. 
Определить у какого числа большая сумма цифр. 
Вывод в основной программе. Расчёт суммы цифр в функции
"""

def rasschoyt(one,two,three):

    one_sum = digits_sum(number = one)
    two_sum = digits_sum(number = two)
    three_sum = digits_sum(number = three)

    if one_sum > two_sum:
        if one_sum > three_sum:
            return one_sum
        elif three_sum > one_sum:
            return three_sum
    elif two_sum > one_sum:
        if two_sum > three_sum:
            return two_sum
        elif three_sum > two_sum:
            return three_sum
        
def digits_sum(number):
    digits_sum = 0
    while number > 0:
        digits_sum = digits_sum + (number % 10)
        number //= 10
    return digits_sum

one, two, three = input('Введите one: '), input('Введите two: '), input('Введите three: ')
while type(one) != int:
    try:
        one = int(one)
    except Exception as e:
        print('Неверный ввод числа..')
        one = input('Введите one: ')
while type(two) != int:
    try:
        two = int(two)
    except Exception as e:
        print('Неверный ввод числа..')
        two = input('Введите two: ')
while type(three) != int:
    try:
        three = int(three)
    except Exception as e:
        print('Неверный ввод числа..')
        three = input('Введите three: ')

print(f'Число с большей суммой цифр: {rasschoyt(one,two,three)}')

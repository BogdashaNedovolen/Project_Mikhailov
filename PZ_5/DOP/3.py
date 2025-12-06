"""
Написать программу, подсчитывающую количество цифр числа, используя функцию.
"""

def rasschoyt(n):
    kolvo = 1
    while n > 0:
        n //= 10
        kolvo += 1
    return kolvo

n = input('Введите число: ')
while type(n) != int:
    try:
        n = int(n)
    except Exception as e:
        print('Неверный ввод числа..')
        n = input('Введите one: ')


print(f'Количество цифр числа - {rasschoyt(n)}')

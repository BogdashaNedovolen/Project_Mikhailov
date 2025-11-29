"""
Составить функцию решения задачи. Из заданного числа вычли сумму его цифр. 
Из результата вновь вычли сумму его цифр и т.д. 
Через сколько таких действий получится нуль?
"""

def rasschoyt(n):
    if n == 0:
        return 0
    
    count = 0
    current = n

    while current != 0:
        digit_sum = 0
        temp = current

        while temp > 0:
            digit_sum = digit_sum + (temp % 10)
            temp = temp // 10

        current = current - digit_sum
        count = count + 1

        if current < 0:
            current = -current

    return count

n = input('Введите число: ')
while type(n) != int:
    try:
        n = int(n)
    except Exception as e:
        print('Неверный ввод числа..')
        n = input('Введите первое число: ')
print(f'Количество действий: {rasschoyt(n)}')

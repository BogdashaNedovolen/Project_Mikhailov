"""
Дано целое число N (> 0). 
Найти сумму N^2 + (N+1)^2 + (N+2)^2 + ... + (2N)^2
"""

number = input('Введите число: ')

while type(number) != int:
    try:
        number = int(number)
        if number <= 0:
            print("Число должно быть > 0!")
            number = input("Введите число: ")
        else:
            break
    except ValueError:
        print("Неправильно ввели!")
        number = input("Введите число: ")

sum_square = 0

current = number
while current <= 2*number:
    sum_square += current**2
    current += 1

print(f"Результат: {sum_square}")

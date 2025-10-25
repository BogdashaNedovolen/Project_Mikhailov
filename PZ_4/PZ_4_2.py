"""
Дано целое число N (>1). Найти наибольшее целое число K, 
при котором выполняется неравенство 3^K < N
"""

number = input('Введите число: ')

while type(number) != int:
    try:
        number = int(number)
        if number <= 1:
            print("Число должно быть > 1!")
            number = input("Введите число: ")
        else:
            break
    except ValueError:
        print("Неправильно ввели!")
        number = input("Введите число: ")

K = 0
square = 3**K

while square < number:
    K += 1
    square = 3**K


K = K - 1 # Для наибольшего числа

print(f'Наибольшее число K: {K}')

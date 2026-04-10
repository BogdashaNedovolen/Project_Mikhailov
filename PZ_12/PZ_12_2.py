"""
В матрице найти среднее арифметическое положительных элементов.
"""

import random

rows = 5
cols = 5

matrix = [[random.randint(-9, 9) for x in range(cols)] for x in range(rows)]

positive = [x for row in matrix for x in row if x > 0]
mid = sum(positive) / len(positive) if positive else 0

print("Заданная матрица:")
for row in matrix:
    print(row)

print('Положительные числа: ', positive)

print(f'Среднее арифметическое положительных чисел: {mid:1.2f}')

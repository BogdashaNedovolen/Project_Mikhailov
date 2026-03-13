"""
В последовательности на n целых чисел найти и вывести:
- максимальный среди отрицательных
- элементы кратные двум
- их сумму
"""

from functools import reduce

base = [3, -5, -1, 5, -3, 1, 8, -8]

max_neg = reduce(lambda x, y: x if x > y else y, filter(lambda x: x < 0, base))
print(max_neg)

kratni = list(filter(lambda x: x % 2 == 0, base))
print(kratni)

summa = reduce(lambda x, y: x + y, base)
print(summa)

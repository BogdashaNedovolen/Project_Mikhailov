"""
В матрице элементы третьей строки заменить элементами из одномерного
динамического массива соответствующей размерности.
"""
import random

rows = 5
cols = 5

matrix = [[random.randint(-9, 9) for x in range(cols)] for x in range(rows)]
third_string = [random.randint(10, 99) for x in range(cols)]

print("Заданная матрица:")
for row in matrix:
    print(row)

print(f"\nОдномерный массив для замены: {third_string}")

matrix[2] = third_string

print("\nПолучившаяся матрица:")
for row in matrix:
    print(row)

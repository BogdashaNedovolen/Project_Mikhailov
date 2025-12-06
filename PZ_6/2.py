"""
Дан список размера N. 
Найти количество промежутков монотонности
(участки, на которых элементы возрастают или убывают)
"""
###
direction_ravno = 0
direction_down = 0
direction_up = 0
direction = None
###

import random

N = int(input('N = '))

a = []

count = 0
while count < N:
    a.append(int(random.randint(-10,10)))
    count += 1

if N < 2:
    direction_up = direction_down = direction_ravno = 0
else:
    for i in range(1,N):
        if a[i] == a[i-1]:
            direction_ravno += 1
        elif a[i] > a[i-1]:
            direction_up += 1
        elif a[i] < a[i-1]:
            direction_down += 1

print(f'Список: {a}')
print(f'Кол-во участков, на которых возрастает: {direction_up}')
print(f'Кол-во участков, на которых убывает: {direction_down}')



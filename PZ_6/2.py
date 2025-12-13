"""
Дан список размера N. 
Найти количество промежутков монотонности
(участки, на которых элементы возрастают или убывают)
"""
import random
###
dir = 0
dir_up = 0
dir_down = 0
new_dir = 0
###

N = int(input('N = '))

a = []

count = 0
while count < N:
    a.append(int(random.randint(0,20)))
    count += 1

if N < 2:
    print(f'Список: {a}')
    print(f'Кол-во участков, на которых возрастает: 0')
    print(f'Кол-во участков, на которых убывает: 0')
else:
    for i in range(1,N):
        if a[i] == a[i-1]:
            new_dir = 0
        elif a[i] > a[i-1]:
            new_dir = 1
        elif a[i] < a[i-1]:
            new_dir = -1
        
        if dir == 0:
            dir = new_dir
            if new_dir == 1:
                dir_up += 1
            else:
                dir_down += 1
        elif new_dir != dir:
            dir = new_dir
            if new_dir == 1:
                dir_up += 1
            else:
                dir_down += 1
    print(f'Список: {a}')
    print(f'Кол-во участков, на которых возрастает: {dir_up}')
    print(f'Кол-во участков, на которых убывает: {dir_down}')

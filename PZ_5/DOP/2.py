"""
Рассчитать и вывести периметр и площадь прямоугольника. 
Расчеты оформить в функции.
"""

def raschoyt(x,y,choice):
    if choice == 0:
        P = x*2 + y*2
        return P
    else:
        S = x*y
        return S

x, y = input('Введите x: '), input('Введите y: ')
while type(x) != int:
    try:
        x = int(x)
    except Exception as e:
        print('Неверный ввод числа..')
        x = input('Введите x: ')
while type(y) != int:
    try:
        y = int(y)
    except Exception as e:
        print('Неверный ввод числа..')
        y = input('Введите two: ')

print(f'Периметр прямоугольника - {raschoyt(x,y,0)}. Площадь прямоугольника - {raschoyt(x,y,1)}')

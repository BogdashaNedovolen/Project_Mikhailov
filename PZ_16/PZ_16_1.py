"""
Создайте класс "Здание" с атрибутами "адрес" и "количество этажей". Напишите
метод, который выводит информацию о здании в формате "Адрес: адрес, Количество
этажей: этажи".
"""

class Building:
    def __init__(self, address, floors):
        self.address = address
        self.floors = floors

    def info(self):
        print(f'Адрес: {self.address}. Количество этажей: {self.floors}')


address = input('Введите адрес: ')
while True:
    try:
        floors = int(input('Введите количество этажей: '))
        break
    except ValueError:
        print('Пожалуйста, введите число для количества этажей.')

# house = Building('ул. Ленина, 10', 5)
house = Building(address, floors)
house.info()

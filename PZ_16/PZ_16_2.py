"""
Создайте базовый класс "Животное" со свойствами "вид", "количество лап", "цвет
шерсти". От этого класса унаследуйте класс "Собака" и добавьте в него свойства
"кличка" и "порода".
"""

class Animal:
    def __init__(self, type, paws, color):
        self.type = type
        self.paws = paws
        self.color = color

    def info(self):
        print(f'Вид: {self.type}. Количество лап: {self.paws}. Цвет: {self.color}.')
    
class Dog(Animal):
    def __init__(self, type, paws, color, name, subtype):
        Animal.__init__(self,type, paws, color)

        self.name = name
        self.subtype = subtype

bobik = Dog('Собака', 4, 'Коричневый', 'Бобик', 'Дворняга')
bobik.info()

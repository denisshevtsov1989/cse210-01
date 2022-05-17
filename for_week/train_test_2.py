"""
# Пример 1
#  Пишем название класса
class Person():
    pass


Person.money = 150

obj1 = Person()
obj2 = Person()
obj1.name = 'Bob'
obj2.name = 'Masha'

print(obj1.name, 'has', obj1.money, 'dollars.')
print(obj2.name, 'has', obj2.money, 'dollars.')
"""
"""
# Пример 2

class Person():
    name = ''
    money = 0


# Создаём объект
obj1 = Person()
obj2 = Person()

obj1.name = 'Bob'
obj1.money = 150

obj2.name = 'Masha'

print(obj1.name, 'has', obj1.money, 'dollars.')
print(obj2.name, 'has', obj2.money, 'dollars.')
"""
"""
# Пример 3


class Person():
    name = ""
    money = 0

    def out(self):
        print(self.name, 'has', self.money, 'dollars.')

    def changemoney(self, newmoney):
        self.money = newmoney


obj1 = Person()  # Экземпляр класса
obj2 = Person()  # Создание экземпляра класса
obj1.name = 'Bob'  # Создание атрибута экземпляра класса
obj2.name = 'Masha'  # Создание атрибута экземпляра класса
obj1.out()  # Экземпляр метода
obj2.out() # Экземпляр метода
obj1.changemoney(150) # Экземпляр метода
obj1.out() # Экземпляр метода
"""
"""
# Пример 4

print('Пример 4')

"""
# class Critter():  # Написание класса


"""
    def talk(self):  # Написание метода
        print("Привет. Я животое - экземпляр класса Critter.")


# основная часть
# создание объекта и вызова метода
crit = Critter()  # Создание экземпляра класса
crit.talk()
input("/nНажмите на Enter, чтобы выйти")

"""

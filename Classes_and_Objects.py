# пример "простого" класса
#class MyFirstClass:
#    pass
#my_first_object = MyFirstClass()
#print(my_first_object)
#print(x for x in range(10))
#class MyClass:
#    parent = 'MyClass'
#    ''' Это мной созданный класс '''
#    def __init__(self):
#        self.creator = 'Joe'
#        pass
#obj = MyClass()
#print(obj.__dict__, obj.creator)
#obj.date = '06-03-2025'
#print(obj.__dict__)
#obj2 = MyClass()
#obj2.date = '24.03.2025'
#print(obj.parent, print(obj2.parent))
#task 1
#class Person:
#    def __init__(self):
#        self.name = 'Joe'
#        self.bod = '23-12-1957'
#        self.mobile = '1-24-7546-87'
#        self.city = 'New Yorke'
#    def set_info(self):
#        self.name = input('Введите имя')
#        self.bod = input('Введите дата рождения')
#        self.mobile = input('Введите номер телефона')
#        self.city = input('Введите город')
#
#    def get_info(self):
#        print(f'Имя: {self.name}\nдата рождения: {self.bod}\nномер телефона: {self.mobile}\nгород: {self.city}')
#
#    def update_info(self):
#        change = input('1-изменить имя\n2-изменить дату рождения\n3-изменить номер телефона\n4-изменить город')
#        if change == '1':
#            self.name = input('Введите новое имя')
#        elif change == '2':
#            self.bod = input('Введите новую дату рождения')
#        elif change == '3':
#            self.mobile = input('Введите новый номер телефона')
#        elif change == '4':
#            self.city = input('Введите новый город')
#        else:
#            print('Такой команды нет')
#
#user1 = Person()
##print(user1.__dict__)
#user1.update_info()
#user1.get_info()


#Создайте класс «Город». Необходимо хранить в полях класса: название города,  название
#страны, количество жителей в городе, телефонный код города. Реализуйте методы класса
#для ввода данных, вывода данных, реализуйте доступ к
#отдельным полям через методы класса
'''Решение отсутствует'''

class Car:
    def __init__(self, price, color):
        self.tone = color
        self.sale = price
car = Car(100_000, 'red')
car2 = Car(100_0004, 'green')
car3 = Car(1030_000, 'red')
print(car.__dict__, car2.__dict__, car3.__dict__)
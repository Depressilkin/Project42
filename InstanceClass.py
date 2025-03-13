# статические методы
class MyClass:
    var = 0
    def example_method(self):
        print('Метод экземпляра класса')
    
    @staticmethod # статический - значит принадлежащий только классу (не экземплярам)
    def static_method(name):
        print('Статический метод класса', name)

obj = MyClass()
#obj.example_method()
#MyClass.static_method('MyClass')

#class User:
#    def __init__(self, name, last_name, mobile, email, age):
#        self.name = name
#        self.last_name =  last_name
#        self.mobile = mobile
#        self.email = email
#        self.age = age
#    
#    def other_method(self):
#        print('Некоторый метод')
#
#class Student(User):
#    def __init__(self, name, last_name, mobile, email, age, group):
#        super().__init__(name, last_name, mobile, email, age)
#        self.group = group
#
#    def lesson(self):
#        print('Придти на занятия')
#
#class Teacher(User):
#    def __init__(self, name, last_name, mobile, email, age, theme):
#        super().__init__(name, last_name, mobile, email, age)
#        self.theme = theme
#    
#    def lesson(self):
#        print('Провести на занятия')
#
#student = Student('Joe', 'Byden', '4254325', 'superjoe@mail.com', 78, 'Python42')
#print(student.__dict__)
#student.lesson()
#
#teacher = Teacher('Donald', 'Trump', '4254325', 'superdon@mail.com', 78, 'Python')
#teacher.other_method()
#
##функция issubclass()
#print(issubclass(Student, User))
#
##функция isinstance
#print(isinstance(student, Student))
#print(isinstance(teacher, Student))
#print(isinstance(student, User))
#print(isinstance(False, int))

#К уже реализованному классу «Человек» добавьте
#статический метод, который при вызове возвращает количество созданных объектов класса «Человек».
#
#class Person:
#    count = 0
#
#    @staticmethod
#    def get_count():
#        print(f'Количество созданных экземпляров класса {Person.count}')
#
#    def __init__(self):
#        self.name = 'Joe'
#        self.bod = '23-12-1957'
#        self.mobile = '1-24-7546-87'
#        self.city = 'New Yorke'
#        Person.count += 1
#
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
#obj1 = Person()
#obj2 = Person()
#Person.get_count()
#obj3 = Person()
#Person.get_count()
#
#class Figure:
#    count = 0
#    def __init__(self, name, *l): # (a = None, b = None, c = None, d = None)
#        self.name = name.lower()
#        self.lenght = l
#
#    def s(self):
#        if self.name == 'треугольник':
#            p = round(sum(self.lenght) / 2, 2)
#            a = self.lenght[0]
#            b = self.lenght[1]
#            c = self.lenght[2]
#            self.square = (p * round(p - a,2) * round(p - b,2) * round(p - c,2)) ** 0.5
#            Figure.count += 1
#        elif self.name == 'прямоугольник':
#            a = list(set(self.lenght))[0]
#            b = list(set(self.lenght))[1]
#            self.square = a * b
#            Figure.count += 1
#        elif self.name == 'квадрат':
#            self.square = self.lenght[0] ** 2
#            Figure.count += 1
#        elif self.name == 'ромб':
#            self.square = self.lenght[0] * self.lenght[1] * 0.5
#            Figure.count += 1
#        else:
#            print('Некорректный ввод')
#    @staticmethod
#    def get_count():
#        print(f'Количество подсчетов {Figure.count}')
#
#figure1 = Figure('Треугольник',25, 25, 49)
#figure2 = Figure('Квадрат', 3, 3, 3, 3)
#figure1.s()
#figure2.s()
#Figure.get_count()

#Создайте класс для подсчета максимума из четырех
#аргументов, минимума из четырех аргументов, среднеарифметического из четырех аргументов, факториала
#аргумента. Функциональность необходимо реализовать
#в виде статических методов.

#class MathClass:
#    @staticmethod
#    def max(a, b, c , d):
#        print(max(a, b, c , d))
#    
#    @staticmethod
#    def min(a, b, c , d):
#        print(min(a, b, c , d))
#    
#    @staticmethod
#    def average(a, b, c , d):
#        print( sum([a, b, c , d]) / 4)
#    
#    @staticmethod
#    def fact(a):
#        fact = 1
#        while a != 1:
#            fact *= a
#            a -= 1
#        print(fact)
#MathClass.max(22, 34, 23, 5)
#MathClass.min(22, 34, 23, 5)
#MathClass.average(22, 34, 23, 5)
#MathClass.fact(5)


#Создайте класс Human, который будет содержать
#информацию о человеке.
#Спомощью механизма наследования, реализуйте класс
#Builder (содержит информацию о строителе), класс Sailor
#(содержит информацию о моряке), класс Pilot (содержит
#информацию о летчике).
#Каждый из классов должен содержать необходимые
#для работы методы.
#class Human:
#    def __init__(self, name, last_name, age):
#        self.name = name
#        self.last_name =  last_name
#        self.age = age
#    def work(self):
#        print('*работает работу*')
#    
#class Builder(Human):
#    def __init__(self, name, last_name, age, company):
#        super().__init__(name, last_name, age)
#        self.company = company
#    def process(self):
#        print("Строит")
#class Sailor(Human):
#    def __init__(self, name, last_name, age, ship):
#        super().__init__(name, last_name, age)
#        self.ship = ship
#    def process(self):
#        print("Ходит по воде")
#class Pilot(Human):
#    def __init__(self, name, last_name, age, plane):
#        super().__init__(name, last_name, age)
#        self.plane = plane
#    def process(self):
#        print("Летит по воздуху")
#builder = Builder('Иван', 'Иванов', 34, 'РУСМОСТСТРОЙ')
#sailor = Sailor('Петр', "Петров", 45, "Титаник")
#pilot = Pilot("Сергей", "Сергеев", 65, "Airbus A320")
#print(builder.company)
#sailor.process()
#pilot.process()

class Passport:
    def __init__(self,  name, last_name, bod, country, number):
        self.name = name
        self.last_name = last_name
        self.bod = bod
        self.country = country
        self.number = number 

class ForeignPassport(Passport):
    def __init__(self, name, last_name, bod, country, number):
          super().__init__(name, last_name, bod, country, number)
          self.visa = {}
    
    def open_visa(self, location):
         self.visa[location] = True
        
    def closed_visa(self, location):
         self.visa[location] = False
 
person = ForeignPassport('Joe', 'Byden', '30.7.1987', 'USA', '3425647875')
person.open_visa('Russia')
person.open_visa('China')
print(person.visa)
person.closed_visa('Russia')
print(person.visa)

#Создать базовый класс «Животное» и производные
#классы «Тигр», «Крокодил», «Кенгуру».
#С помощью конструктора установить имя каждого животного и его характеристики.
#Создайте для каждого класса необходимые
#методы и поля

# атрибуты: название или имя, тип, наличие шерсти, среда обитания
# методы: голос, способ питания.
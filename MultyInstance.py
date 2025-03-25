#class FirstSuper:
#    def __init__(self, a):
#        self.a = a
#
#    def m2(self):
#        return 'Hello'
#
#    def meth(self):
#        return f'FirstSuper'
#
#class SecondSuper:
#    def __init__(self, b):
#        self.b = b
#
#    def meth(self):
#        return f'SecondSuper'
#
#class Sub(SecondSuper, FirstSuper):
#    def __init__(self, a, c, b):
#        super().__init__(a)
#        FirstSuper.__init__(self,b)
#        self.c = c
#    
#objct = Sub(1, 2, 3)
#print(objct.meth())
#print(objct.m2())
#print(objct.a)

#Используя понятие множественного наследования,
#разработайте класс «Окружность, вписанная в квадрат».

#class Square:
#    def __init__(self, a):
#        self.a = a
#    def s_square(self):
#        return self.a ** 2
#class Circle:
#    def __init__(self, r):
#        self.r = r
#    def s_circle(self):
#        return   self.r ** 2 * 3.14
#
#class SquaredOffArea(Square,Circle):
#    def __init__(self, a, r):
#        super().__init__(a)  
#        Circle.__init__(self, r)
#    def check_area(self):
#        if self.a == 2 * self.r:
#            print('Окружность вписана в квадрат')
#        else:
#            print('Окружность не вписана в квадрат')
#figure = SquaredOffArea(4, 2)
#figure.check_area()
#figure2 = SquaredOffArea(324,43)
#figure2.check_area()

#Используя механизм множественного наследования
#разработайте класс “Автомобиль”. Должны быть классы
#«Колеса», «Двигатель», «Двери», "Кузов"
#class Wheel:
#    def __init__(self, d):
#        self.d = d
#
#class Engine:
#    def __init__(self, power, type):
#        self.power = power
#        self.engine_type = type
#    
#    def sound_engine(self):
#        if self.engine_type == 'electric':
#            return f'shh-hhh-hhh'
#        else:
#            return f'JRRR-RRRR-R'
#class Door:
#    def __init__(self, color):
#        self.door_color = color
#
#class Dodywork:
#    def __init__(self, type, color, hatch):
#        self.bodywork_type = type
#        self.bodywork_color = color
#        self.hatch = hatch
#
#class Auto(Dodywork, Engine, Wheel, Door):
#    def __init__(self, bodywork_type, bodywork_color, hatch, power, engine_type, d, door_color, doors_count,wheels_count):
#        super().__init__(bodywork_type, bodywork_color, hatch)
#        Engine.__init__(self,power, engine_type)
#        Wheel.__init__(self,d)
#        Door.__init__(self,door_color)
#        self.doors_count = doors_count
#        self.wheels_count = wheels_count
#
#    def sound_engine(self):
#        return super().sound_engine()
#    
#    def signal(self):
#        return f'Beep-Beep'
#
#lada_iskra = Auto('sedan', 'red', False, 160, "ice", 16, 'red', 4, 4)
#print(lada_iskra.__dict__, lada_iskra.sound_engine(), lada_iskra.signal())
#tesla_e = Auto('crossover', 'grey', True, 300, "electric", 17, 'grey', 5, 4)
#print(isinstance(tesla_e, Door))

#Создать базовый класс «Домашнее животное» и производные классы«Собака», «Кошка», «Попугай», «Хомяк».
#С помощью конструктора установить имя каждого животного и его характеристики. Реализуйте для каждого
#из классов методы:
#■ Sound — издает звук животного (пишем текстом в
#консоль);
#■ Show — отображает имя животного;
#■ Type — отображает название его подвида;

#class Pet:
#    def __init__(self, nick, coating):
#        self.nick  = nick
#        self.coating = coating
#        self.paws = None 
#        self.sound_content = None
#        self.type = None
#    
#    def sound(self):
#        return self.sound_content
#    
#    def show(self):
#        return self.nick
#
#    def get_type(self):
#        return self.type
#
#class Dog(Pet):
#    def __init__(self, nick, coating, paws, sound_content, type):
#        super().__init__(nick, coating)
#        self.paws = paws
#        self.sound_content = sound_content
#        self.type = type
#
#    def sound(self):
#        return super().sound()
#    def show(self):
#        return super().show()
#    def get_type(self):
#        return super().get_type()
#
#class Cat(Pet):
#    def __init__(self, nick, coating, paws, sound_content, type):
#        super().__init__(nick, coating)
#        self.paws = paws
#        self.sound_content = sound_content
#        self.type = type
#
#    def sound(self):
#        return super().sound()
#    def show(self):
#        return super().show()
#    def get_type(self):
#        return super().get_type()
#    
#class Snake(Pet):
#    def __init__(self, nick, coating, sound_content, type):
#        super().__init__(nick, coating)
#        self.sound_content = sound_content
#        self.type = type
#    
#    def sound(self):
#        return super().sound()
#    def show(self):
#        return super().show()
#    def get_type(self):
#        return super().get_type()
#
#class Turtle(Pet):
#    def __init__(self, nick, coating, paws, type):
#        super().__init__(nick, coating)
#        self.paws = paws
#        self.type = type
#    def show(self):
#        return super().show()
#    def get_type(self):
#        return super().get_type()
#
#pet = Dog("Шарик", "шерсть", "4", "гаав-гаав", "собака")
#pet = Cat('Матроскин',"шерсть", "4", "мяу", "кошка" )
#pet = Snake('Каа', "Чешуя", "Шш-шшш--шшш", "Питон")
#pet = Turtle("Рафаэль", "Панцирь", 4, "Черепаха")
#print(pet.__dict__, pet.show(), pet.get_type(), pet.sound(), sep='\n')
#

#Создать базовый класс Employer (служащий) с функцией Print(). Она должна выводить информацию о служащем. 
# В случае базового класса это может быть строка This is Employer class
#Создайте от него три производных класса: President,
#Manager, Worker. Переопределите функцию Print() для
#вывода информации, соответствующей каждому типу
#служащего.

class Employer:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age 
        self.sex = sex
    '''Employer'''
    def print(self):
        return f'This is {str(self.__class__)[17:-2]} class'

    def __str__(self):
        return self.name
    
    def __int__(self):
        return self.age

class President(Employer):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)

class TopManager(Employer):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)

class Worker(Employer):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)

user1 = President('Joe', 32, 'Male')
user2 = TopManager('Anna', 53, 'Female')
user3 = Worker('Gertruda', 32, 'Female')
for user in [user1, user2, user3]:
    print(int(user))
#Для классов из задания 4 реализуйте магический
#метод str, а также метод int (должен возвращать возраст
#служащего
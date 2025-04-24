##ПАТТЕРНЫ ПРОЕКТИРОВАНИЯ
##ПОРОЖДАЮЩИЙ (Singleton, Fabric, Abstract Fabric)
##СТРУКТУРНЫЙ (Facade) 
##ПОВЕДЕНЧЕСКИЙ (iterator)
#
##Создайте классическую реализацию паттерна Singleton.
##Протестируйте работу созданного класса.
##__init__ - команда определения экземпляра __new__ - команда-конструктор
#
#class Singletone:
#    _instance = None
#    def __new__(cls):
#        if cls._instance is None: # если экземпляра-одиночки нет
#            cls._instance = super(Singletone, cls).__new__(cls) #создать экземляр одиночку
#        else:
#            print('Экземпляр-одиночка уже создан')
#        return cls._instance
#
#class NotSingletone:
#    pass
#
#refery = Singletone()
#print(refery)
#refery2 = Singletone()
#print(refery2)
#print(refery is refery2)
#
#obj1 = NotSingletone()
#obj2 = NotSingletone()
#print(obj1 is obj2, obj1, obj2)
#
##pattern Fabric
#
#class Fabric:
#    def __init__(self, name, age, professional):
#        self.name = name
#        self.age = age
#        self.professional = professional
#    
#    def get_info(self):
#        return f'Name: {self.name}, Professional: {self.professional}'
#
#class Driver(Fabric):
#    def __init__(self, name, age, professional):
#        super().__init__(name, age, professional)
#
#class Pilot(Fabric):
#    def __init__(self, name, age, professional):
#        super().__init__(name, age, professional)
#
#user1 = Driver('Dominic Taretto', 45, 'Speedster')
#user2 = Pilot('Alasheev', 76, 'test pilot')
#print( user1, user2)
#print(issubclass(Driver, Fabric), issubclass(Pilot, Fabric))
#
##Создайте реализацию паттерна Abstract Factory. Протестируйте работу созданного класса.
#from abc import ABC, abstractmethod
#class AbstractFactory(ABC):
#    @abstractmethod
#    def create_factory(self,name):
#        if name == 'Lada':
#            factory = LadaFactory()
#            return factory
#        elif name == 'Sukhoi':
#            factory = SukhoiFactory()
#            return factory
#
#class LadaFactory(AbstractFactory):
#    def __init__(self):
#        self.name = 'Фабрика компании Лада'
#
#class SukhoiFactory(AbstractFactory):
#    def __init__(self):
#        self.name = 'Фабрика компании Сухой'
#    def create_factory(self,name):
#        return super().create_factory(name)
#f = SukhoiFactory()
#factory_from_Irkutsk = f.create_factory('Sukhoi')
#
#print(factory_from_Irkutsk)

#Пользователь вводит с клавиатурынабор чисел и путь
#кфайлу для сохранения полученных данных. Необходимо:
#■ Сохранить все полученные числа.
#■ Найти максимум, минимум. Эти значения сохранить
#в том же файле.
#■ Отобразить числа.
#■ Отобразить максимум и минимум.
#■ Создать класс для логгирования операций. При создании объекта класса нужно уточнить куда производится
#логгирование: экран или файл. В программе можно
#создать только один объект класса. Все действия
#объекта этого класса.

class Logger:
    _instance = None
    logger_location = None
    def __new__(cls):
        if cls._instance is None:
            cls.logger_location = input('Куда вести запись логирования:\n1-в файл\n2-в терминал')
            cls._instance = super(Logger, cls).__new__(cls)
        else:
            print('Логгер уже создан')
        return cls._instance

    def logging(self, message):
        if self.logger_location == '2':
            print(message)
        else:
            with open('Logging.txt', 'a', encoding='utf-8') as file:
                file.write(message + '\n')
    
    def log_input_digits(self): 
        self.logging('Были добавлены числа')

    def log_extrem_digits(self, maxx, minx):
        self.logging(f'Выполнен Поиск максимального и минимального. Макс {maxx}, мин {minx}')

    def log_render(self, list_digits):
        self.logging(f'Выполнен рендер массива {list_digits}, макс.элемент {max(list_digits)} и мин.элемента {min(list_digits)}')

class Digits:
    def __init__(self, path='Digits.txt', logger=None):
        array = input('Введите числа через пробел')
        self.path = path
        self.logger = logger
        self.list_digits = list(map(int, array.split(' ')))
        with open(path, 'a', encoding='utf-8') as file:
            for digit in self.list_digits:
                file.write(str(digit)+'\n')
        logger.log_input_digits()
    
    def get_extrem(self):
        maxx = max(self.list_digits)
        minx = min(self.list_digits)
        with open(self.path, 'a', encoding='utf-8') as file:
            file.write(f'Максимальный элемень  {maxx}, Минимальный {minx}')
        self.logger.log_extrem_digits(maxx, minx)

    def render(self):
        print(f'Массив чисел: {self.list_digits}.\nMax: {max(self.list_digits)}, min: {min(self.list_digits)}')
        self.logger.log_render(self.list_digits)

logger = Logger()
print(logger)
array = Digits(logger=logger)
array.get_extrem()
array.render()
#FACADE - суть паттерна в объединении сложной структуры классов в один интерфейс
#Создайте реализацию паттерна Facade. Протестируйте
#работу созданного класса. 
#Симулировать выпуск цифрового продукта. Продукт является 
# результатом действия трех составных: дизайн, программирование, тестирование 

#class Designe: 
#    def get_designe():
#        return f'Результат дейятельности отдела дизайна'
#    
#class Programmer:
#    def get_programmer():
#        return f'Результат дейятельности отдела разработчиков'
#    
#class Tester:
#    def get_tester():
#        return f'Результат дейятельности отдела тестирования'
#
#class WebStudio: #наш Фасад
#    def __init__(self, name):
#        self.name = name
#    
#    def get_designe(self):
#        return Designe.get_designe()
#
#web_studio = WebStudio('Студия цифровых продуктов')
#
#print(web_studio.get_designe())

# Adapter - позволяет несовместимым объектам работать вместе

#Создайте реализацию паттернаAdapter. Протестируйте
#работу созданного класса. Есть два кашелька в rub  и tng, нужно сделать адаптер для конвертации валют
#
#class WalletRub:
#    def __init__(self, cashe):
#        self.cashe = cashe
#    
#    def check_balance(self):
#        print(f'{self.cashe} RUB')
#
#class WalletTng:
#    def __init__(self, cashe):
#        self.cashe = cashe
#    
#    def check_balance(self):
#        print(f'{self.cashe} TNG')
#
#class AdapterRubToTng:
#    def __init__(self, cashe):
#        self.cashe = cashe * 6.26
#    
#    def check_balance(self):
#        print(f'{self.cashe} TNG')
#
#my_wallet_ru = WalletRub(100)
#my_wallet_ru.check_balance()
#
#kzt_freund_wallet_tng = WalletTng(12)
#kzt_freund_wallet_tng.check_balance()
#
#my_wallet_kzt = AdapterRubToTng(my_wallet_ru.cashe)
#my_wallet_kzt.check_balance()

#Strategy
##Создайте реализацию паттерна Strategy. Протестируйте
#работу созданного класса. Пользователь выбирает стратегию продажи или аренды недвижимости

#class User:
#    def __init__(self):
#        pass
#    
#    def start(self, strategy):
#        print(strategy)
#
#class StrategyA:
#    list_product = ['площадь 20кв.м', 'площадь 230 кв.м']
#    def strategy():
#        return StrategyA.list_product
#
#class StrategyB:
#    list_product = ['площадь 2400кв.м', 'площадь 3000 кв.м']
#    def strategy():
#        return StrategyB.list_product
#    
#user = User()
#user.start(StrategyA.strategy())
#print('two hours later')
#user.start(StrategyB.strategy())

#iterator позволяет итерировать (перебирать) элементы объекта класса сохраняя все принципы инкапсуляции
#Есть список (каталог) товаров, создать класс и метод вывода каталога товаров

#class Market:
#    def __init__(self, list_product):
#        self.list_product = list_product
#        self.index = 0
#    
#    def __iter__(self):
#        return self
#    
#    def __next__(self):
#        if self.index < len(self.list_product):
#            product = self.list_product[self.index]
#            self.index += 1
#            return product
#        else:
#            raise StopIteration
#
#products = ['Чокопай', 'Яшкино', 'Орео', "Тук"]
#wb = Market(products)
#for product in wb:
#    print(product)

#В каждом учебном заведении есть студенты.Студенты
#входят в состав групп. Вам необходимо создать эмуляцию учебного процесса. Приложение должно позволять
#добавлять, удалять, изменять информацию о студентах
#и группах. При реализации используйте паттерн Iterator
#(для отображения студентов, входящих в группу) и другие
#необходимые паттерны.

class Student:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def update(self):
        menu = input('Обновить\n1-имя\n2-возраст')
        new_info = input('введите новое значение')
        if menu == '1':
            self.name = new_info
        else:
            self.age = int(new_info)

class Group:
    def __init__(self, name):
        self.name = name
        self.list_students = []
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.list_students):
            product = self.list_students[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
    
    def add_student(self, student):
        self.list_students.append(student)
    
std1, std2, std3 = Student('Joe', 15), Student('Leo', 19), Student('Max', 15)
group1 = Group('Python42')
group1.add_student(std1)
group1.add_student(std2)
group1.add_student(std3)
print('Группа', group1.name)
for student in group1:
    print(student.name, student.age)
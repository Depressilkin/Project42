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
    
    def add_student(self, name, age):
        self.list_students.append(Student(name, age))
    
    def delete_student(self, name_student):
        for index_student in range(len(self.list_students)):
            if self.list_students[index_student].name == name_student:
                student = self.list_students[index_student]
                self.list_students.pop(index_student)
                del student
                return self.list_students

    def update(self, new_name):
        self.name = new_name
        return self

    def render_group(self):
        print(f'Group "{self.name}"')
        num = 1
        for student in self.list_students:
            print(f'{num}. {student.name}, age {student.age}')
            num += 1

class Academy:
    def __init__(self, name):
        self.name = name
        self.list_groups = []
        self.index = 0
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.list_groups):
            product = self.list_groups[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
    
    def add_group(self, name):
        self.list_groups.append(Group(name))
    
    def delete_group(self, name_group):
        for index_group in range(len(self.list_groups)):
            if self.list_groups[index_group].name == name_group:
                group = self.list_groups[index_group]
                self.list_groups.pop(index_group)
                del group
                return self.list_groups

    def add_student(self, name_group, name_student, age_student):
        for group in self.list_groups:
            if name_group == group.name:
                group.add_student(name_student, age_student)


academy = Academy('TOP')

while True:
    print('МЕНЮ')
    menu = input('1-добавить группу\
                 \n2-добавить студента в группу\
                 \n3-вывод групп\n4-вывод списка группы\
                 \n5-удалить группу\n6-удалить студента\
                 \n7-изменить инфо группы\
                 \n8-изменить инфо студента\
                 \n0-выход')
    if menu == '1':
        name_group = input('Введите название группы')
        academy.add_group(name_group)
    elif menu == '2':
        info = input('Введите название группы, имя студента, возраст через запятую')
        name_group, name_student, age_student = info.split(',')
        academy.add_student(name_group, name_student, age_student)
    elif menu == '3':
        print(f'Академия {academy.name}, {academy.list_groups}')
        for group in academy:
            print(group.name)
    elif menu == '4':
        name_group = input('Введите название группы')
        for group in academy:
            if group.name == name_group:
                group.render_group()
                break
        else:
            print('такой группы нет')
    
    elif menu == '5':
        name_group = input('Введите название группы')
        academy.delete_group(name_group)
    
    elif menu == '6':
        name_group, name_student = input('Введите через запятую название группы и имя студента').split(',')
        for group in academy:
            if group.name == name_group:
                group.delete_student(name_student)
                break
        else:
            print('Группа не найдена')
    
    elif menu == '7':
        name_group = input('Введите название группы')
        new_name_group = input('Введите новое название группы')
        for group in academy:
            if group.name == name_group:
                group.update(new_name_group)
    
    elif menu == '8':
        name_group, name_student = input('Введите через запятую название группы и имя студента').split(',')
        for group in academy:
            if group.name == name_group:
                for student in group:
                    if name_student == student.name:
                        student.update()

    elif menu == '0':
        print('Конец программы')
        break
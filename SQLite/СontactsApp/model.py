import sqlite3 as s

class Abonent:
    def __init__(self, name, surname, sex, dob, phone, address):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.dob = dob
        self.phone = phone
        self.address = address
    
class PhoneBook:
    def __init__(self):
        self.phone_book = []

    def add_abonent(self):
        name = input('Введите имя')
        surname = input('Введите фамилию')
        sex = input('Введите пол')
        dob = input('Введите дату рождения в формате дд-мм-гггг')
        phone = input('Введите номер телефона')
        address = input('Введите адрес')
        abonent = Abonent(name, surname, sex, dob, phone, address)
        return abonent

    def del_abonent(self):
        delete_id = input('введите id для удаления абонента')
        return delete_id
    
    def update(self):
        try:
            update_id = input('Укажите id для изменения')
            update_row = int(input(f'Введите номер поле для изменения: \n1-имя\n2-фамилию\n3-пол\n4-дату рождения\n5-номер телефона\n6-адреc'))
            update_row = [None, 'name', 'surname', 'sex', 'dob', 'phone', 'address'][update_row]
            update_value = input('Введите новое значение')
            result = (update_id, update_row, update_value)
            return result
        except:
            print('Ошибка ввода')

class Loader:
    def __init__(self):
        self.path = 'DataBase.db'

    def create_data_base(self):
        with s.connect(self.path) as file:
            cursor = file.cursor()
            cursor.execute('''
CREATE TABLE phone_book(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL, 
surname TEXT NOT NULL, 
sex TEXT NOT NULL, 
dob TEXT NOT NULL, 
phone TEXT NOT NULL, 
address TEXT NOT NULL)
''')
            
    def print_abonents(self):
        try:
            with s.connect(self.path) as file:
                cursor = file.cursor()
                cursor.execute('''
                               SELECT * FROM phone_book
                               ''')
                data = cursor.fetchall()
                for i in data:
                    print(i)
        except:
            print('Проблемы с базой данных')

    def add_abonent(self, abonent):
        try:
            with s.connect(self.path) as file:
                cursor = file.cursor()
                cursor.execute('''
INSERT INTO phone_book(name, surname, sex, dob, phone, address) VALUES (?, ?, ?, ?, ?, ?)
                           ''',(abonent.name, abonent.surname, abonent.sex, abonent.dob, abonent.phone, abonent.address))
        except:
            print('Проблемы с базой данных')

    def del_abonent(self, delete_id):
        try:
            with s.connect(self.path) as file:
                cursor = file.cursor()
                cursor.execute('''
DELETE FROM phone_book WHERE id = ?
                           ''', (delete_id,))
        except:
            print('Проблемы с базой данных')
        
    def update_abonent(self, result):
        print(result)
        match result[1]:
            case 'name':
                self.set_name(result)
            case 'surname':
                self.set_surname(result)
            case 'sex':
                self.set_sex(result)
            case 'dob':
                self.set_dob(result)
            case 'phone':
                self.set_phone(result)
            case 'address':
                self.set_address(result)
    
    def set_name(self, result):
        try:
            with s.connect(self.path) as file:
                cursor = file.cursor()
                cursor.execute('''
UPDATE phone_book SET name = ? WHERE id = ?''', (result[2], result[0]))
        except:
            print('Проблемы с базой данных')

    def set_surname(self, result):
        try:
            with s.connect(self.path) as file:
                cursor = file.cursor()
                cursor.execute('''
UPDATE phone_book SET surname = ? WHERE id = ?''', (result[2], result[0]))
        except:
            print('Проблемы с базой данных')

    def set_sex(self, result):
        try:
            with s.connect(self.path) as file:
                cursor = file.cursor()
                cursor.execute('''
UPDATE phone_book SET sex = ? WHERE id = ?''', (result[2], result[0]))
        except:
            print('Проблемы с базой данных')

    def set_dob(self, result):
        try:
            with s.connect(self.path) as file:
                cursor = file.cursor()
                cursor.execute('''
UPDATE phone_book SET dob = ? WHERE id = ?''', (result[2], result[0]))
        except:
            print('Проблемы с базой данных')
    
    def set_phone(self, result):
        try:
            with s.connect(self.path) as file:
                cursor = file.cursor()
                cursor.execute('''
UPDATE phone_book SET phone = ? WHERE id = ?''', (result[2], result[0]))
        except:
            print('Проблемы с базой данных')    

    def set_address(self, result):
        try:
            with s.connect(self.path) as file:
                cursor = file.cursor()
                cursor.execute('''
UPDATE phone_book SET address = ? WHERE id = ?''', (result[2], result[0]))
        except:
            print('Проблемы с базой данных')

class Menu:
    def __init__(self):
        self.phone_book = PhoneBook()

    def main(self, loader):
        #loader.create_data_base()
        while True:
            menu = input('1-вывести список абонентов\n2-добавить абонента\n3-удалить абонента\n4-редактировать\n0-выход')
            if menu == '1':
                loader.print_abonents()
            elif menu == '2':
                loader.add_abonent(self.phone_book.add_abonent())
            elif menu == '3':
                loader.del_abonent(self.phone_book.del_abonent())
            elif menu == '4':
                loader.update_abonent(self.phone_book.update())


menu = Menu()
loader = Loader()
menu.main(loader)

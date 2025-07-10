import sqlite3 as s
from generator import hospital_info 
with s.connect('SQLite/Hospital2.db') as db:
    cursor = db.cursor()
#    cursor.execute('''
#CREATE TABLE IF NOT EXISTS Departments(
#    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#    building INTEGER NOT NULL CHECK(building >=1 and building <= 5),
#    name TEXT NOT NULL UNIQUE)
#''')
#    cursor.execute('''
#CREATE TABLE IF NOT EXISTS Doctors(
#    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#    phone INTEGER NOT NULL,
#    name TEXT NOT NULL,
#    salary REAL NOT NULL)
#''')
#    cursor.execute('''
#CREATE TABLE IF NOT EXISTS Wards(
#    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#    building INTEGER NOT NULL CHECK(building >=1 and building <= 5),
#    floor INTEGER NOT NULL CHECK(floor >= 1),
#    number INTEGER NOT NULL
#    )
#''')
#    
#
#    cursor.execute('''
#CREATE TABLE IF NOT EXISTS Balance(
#    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#    amount REAL NOT NULL,
#    id_department INTEGER NOT NULL,
#    data INTEGER NOT NULL,
#    FOREIGN KEY (id_department) REFERENCES Departments(id))              
#''')
    
#    cursor.execute('''
#CREATE TABLE IF NOT EXISTS Vacations(
#    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#    id_doctor INTEGER NOT NULL,
#    start_vacation TEXT NOT NULL,
#    length_time INTEGER NOT NULL CHECK(length_time <= 28),
#    FOREIGN KEY (id_doctor) REFERENCES Doctors(id))             
#''') 
#    for i in hospital_info[0]:
#        cursor.execute('''
#    INSERT INTO Departments(building, name) VALUES (?, ?)
#''', (*i,))
#        
#    for i in hospital_info[1]:
#        cursor.execute('''
#    INSERT INTO Doctors(name, phone, salary) VALUES (?, ?, ?)
#''', (*i,))
#    
#    for i in hospital_info[2]:
#        cursor.execute('''
#    INSERT INTO Wards(building, floor, number) VALUES (?, ?, ?)
#''', (*i,))
#    
#    for i in hospital_info[3]:
#        cursor.execute('''
#    INSERT INTO Balance(amount, id_department, data) VALUES (?, ?, ?)
#''', (*i,))
    
#    for i in hospital_info[4]:
#        cursor.execute('''
#    INSERT INTO Vacations(id_doctor, start_vacation, length_time) VALUES (?, ?, ?)
#''', (*i,))

#Задание
#1. Вывести имена врачей и их зарплаты.
#2. Вывести названия депортаментов, и их суммарный баланс.
#3. Вывести все балансы за последний год.
#4. Вывести названия отделений, которые получали бюджет в размере больше 280_000 за 2024.
#5. Вывести имена и зарплаты врачей, которые уходили в отпуск в июне прошлого года.
#6. Вывести названия отделения без повторений, и их максимальный баланс за 5 лет.
#7. Вывести имена врачей с указанием телефонов, которые не были в отпуске в этом году.
#8. Найти врачей, которые отдыхали за 2023 календарный год более 28 дней."

    #TASK 1
#    cursor.execute('''
#SELECT name, salary FROM Doctors
#                   ''')
#    data = cursor.fetchall()
#    for line in data:
#        print(f'имя: {line[0]}, его зарплата:{line[1]} руб.')

    #TASK 2
#    cursor.execute(
#    '''SELECT Departments.name, SUM(Balance.amount)
#FROM Departments, Balance
#WHERE  Departments.id = Balance.id_department
#GROUP BY Balance.id_department ''')
#    data = cursor.fetchall()
#    for line in data:
#        print(f'название отделения: {line[0]}, его суммарный бюджет за 5 лет:{line[1]} руб.')
    
    #TASK 3
#    cursor.execute(
#    '''SELECT id, amount FROM Balance WHERE data LIKE "%25" ''')
#    data = cursor.fetchall()
#    for line in data:
#        print(f'id отделения: {line[0]}, его бюджет 2025:{line[1]} руб.')

    #TASK 4
#    cursor.execute(
#    '''SELECT Departments.name, Balance.amount
#FROM Departments, Balance
#WHERE  Departments.id = Balance.id_department AND Balance.data LIKE "%24" AND Balance.amount > 280000
#GROUP BY Balance.id_department ''')
#    data = cursor.fetchall()
#    for line in data:
#        print(f'название отделения: {line[0]}, бюджет по условию:{line[1]} руб.')
    #TASK 5
#    cursor.execute(
#    '''SELECT Doctors.name, Doctors.salary
#FROM Doctors, Vacations
#WHERE Vacations.start_vacation LIKE "%6-2024" AND Doctors.id = Vacations.id_doctor
#GROUP BY Doctors.id ''')
#    data = cursor.fetchall()
#    for line in data:
#        print(f'Доктор: {line[0]}, зарплата:{line[1]} руб.')
 
 #TASK 6
#    cursor.execute(
#    '''SELECT Departments.name, avg(Balance.amount)
#FROM Departments, Balance
#WHERE Departments.id = Balance.id_department
#GROUP BY Departments.id
#''')
#    data = cursor.fetchall()
#    for line in data:
#        print(f'Название отделения: {line[0]}, средний бюджет:{line[1]} руб.')

#TASK 7
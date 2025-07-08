#from generator import list_student
import sqlite3 as sql
#print(list_student)
with sql.connect('SQLite/Journal.db') as db:
    cursor = db.cursor()
#    cursor.execute('''
#    CREATE TABLE IF NOT EXISTS 'Students'(
#    'id' INTEGER  PRIMARY KEY AUTOINCREMENT,
#    'name' TEXT, 
#    'age' INTEGER,
#    'city' TEXT,
#    'country' TEXT,
#    'mail' TEXT,
#    'phone' TEXT, 
#    'group' TEXT, 
#    'aver_value' REAL, 
#    'min_theme' TEXT, 
#    'max_theme' TEXT) ''')

# Заполнение Таблицы INSERT INTO
#    for stdnt in list_student:
#        cursor.execute('''
#        INSERT INTO 'Students'('name', 'age', 'city', 'country', 'mail', 'phone', 'group', 'aver_value', 'min_theme', 'max_theme') \
#                   VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ''', (*stdnt, ))
    #TASK 1
#    cursor.execute('''
#SELECT name, aver_value FROM Students WHERE aver_value > 3.5 and aver_value < 4.5
#''')
#    stds = cursor.fetchall()
#    for std in stds:
#        print(std)
    # TASK 2
#    cursor.execute('''
#SELECT name, age FROM Students WHERE age >= 20
#''')
#    stds = cursor.fetchall()
#    for std in stds:
#        print(std)
    #TASK 3
#    cursor.execute('''
#SELECT name, age FROM Students WHERE age >= 18 and age <= 27
#''')
#    stds = cursor.fetchall()
#    for std in stds:
#        print(std)
    # TASK4
#    cursor.execute('''
##SELECT name, age, "group" FROM Students WHERE name = 'Ivan'
##''')
##    stds = cursor.fetchall()
#    for std in stds:
#        print(std###)
#TASK 5
#    cursor.execute('''
#SELECT name, phone FROM Students WHERE phone LIKE "%8%8%8"
#''')
#    stds = cursor.fetchall()
#    for std in stds:
#        print(std)
#TASK 6
#    cursor.execute('''
#SELECT name, mail FROM Students WHERE mail LIKE "i%"
#''')
#    stds = cursor.fetchall()
#    for std in stds:
#        print(std)

#TASK 2.1, 2.2
#    cursor.execute('''
#SELECT name, MAX(aver_value) FROM Students
#''')
#    stds = cursor.fetchall()
#    for std in stds:
#        print(std)

#TASK 2.3
    cursor.execute('''
SELECT DISTINCT city, COUNT(*) FROM Students GROUP BY city
''')
    stds = cursor.fetchall()
    for std in stds:
        print(std)

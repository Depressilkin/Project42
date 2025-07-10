import sqlite3 as sq

with sq.connect('SQLite/Example.db') as db: #открытие потока на БД
    cursor = db.cursor() # курсор - объект связывающий БД и интерпретатор
    # Cоздание БД
    #cursor.execute('''CREATE TABLE IF NOT EXISTS first_db( 
    #               id INTEGER,
    #               name TEXT) ''') # SQL запрос
    
    # Получение данных из ДБ
    #cursor.execute('''SELECT * FROM Journal ''')
    #journal = cursor.fetchall()
    #print(journal)
    ##TASK 1
    #for student in journal:
    #    print(f'Name: {student[0]}\nAge: {student[1]}\nAverValue: {student[2]}\n***')
    #TASK 2
    #cursor.execute('SELECT ФИО FROM Journal')
    #name_list = cursor.fetchall()
    #for name in name_list:
    #    print(name)
    #TASK 3
    #cursor.execute('SELECT Оценка FROM Journal')
    #name_list = cursor.fetchall()
    #for name in name_list:
    #    print(name)
    #TASK 4
    #cursor.execute('SELECT ФИО FROM Journal WHERE Оценка > 4')
    #name_list = cursor.fetchall()
    #for name in name_list:
    #    print(name[0])
    

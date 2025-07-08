from random import choice, randint
def create_student():
    #name
    list_name = ["Alexei", "Ivan", "Dmitry", "Sergey", "Andrey", "Vladimir", "Mikhail", "Nikolay", "Yuri", "Viktor", "Pavel", "Oleg", "Artem", "Kirill", "Roman", "Egor", "Vasily", "Gennady", "Leonid", "Fedor", "Semyon", "Timur", "Valery", "Yevgeny", "Vladislav", "Gleb", "Ilya"]
    name = choice(list_name)
    #age
    age = randint(17, 30)
    #city
    list_city = ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "Nizhny Novgorod", "Kazan", "Chelyabinsk", "Omsk", "Samara", "Rostov-on-Don", "Ufa", "Krasnoyarsk", "Perm", "Voronezh", "Volgograd", "Krasnodar", "Saratov", "Tolyatti", "Tyumen", "Izhevsk", "Barnaul", "Ulyanovsk"]
    city = choice(list_city)
    #country
    list_country = ['Russia', 'Belorussia', 'Kazahstan', 'Ukraine']
    country = choice(list_country)
    #mail
    mail = name.lower()+str(age)+'@mail.ru'
    #phone
    phone = '+7' + str(randint(10000, 99999))
    #group
    list_group = ['Web', 'Designe', 'Test', 'Python', 'Computer_science', 'SMM']
    group = choice(list_group)
    #aver_value
    aver_value = randint(20, 50) / 10
    #min_theme
    list_theme = ['Web designe', 'Computer_science', 'Coging', 'Math', 'Eng', 'Startup']
    min_theme = choice(list_theme)
    #max_theme
    max_theme = choice(list_theme)
    return name, age, city, country, mail, phone, group, aver_value, min_theme, max_theme

def create_departament():
    list = []
    for i in range(1, 6):
        building = i
        name = ['Хирургия', "Психиатрия", "Морг", "Вирусология", "Педиатрия"][i - 1]
        list.append([building, name])
    return list

def create_doctors():
    list_name = ["Alexei", "Ivan", "Dmitry", "Sergey", "Andrey", "Vladimir", "Mikhail", "Nikolay", "Yuri", "Viktor", "Pavel", "Oleg", "Artem", "Kirill", "Roman", "Egor", "Vasily", "Gennady", "Leonid", "Fedor", "Semyon", "Timur", "Valery", "Yevgeny", "Vladislav", "Gleb", "Ilya"]
    name = choice(list_name)
    phone = '+7' + str(randint(10000, 99999))
    salary = randint(17_500, 300_000)
    return name, phone, salary

def create_wards():
    list = []
    for i in range(1, 6):
        building = i
        for y in range(1, 10):
            floor = y
            for x in range(10):
                number = str(floor) + str(x)
                list.append([building, floor, int(number)])
    return list

def create_balance():
    list = []
    for date in range(2020, 2026):
        for department in range(1, 6):
            amount = randint(100_000, 800_000)
            list.append([amount, department, date])
    return list

def create_vacations(year):
    id_doctor = randint(1, 20)
    day = randint(1, 28)
    month = randint(1, 12)
    start_vacation = f'{day}-{month}-{year}'
    length_time = randint(1, 28)
    return [id_doctor, start_vacation, length_time]


import sqlite3 as sql
def create_artist(list):
    for artist in list:
        with sql.connect('SQLite/Musipedia/Music.db') as db:
            cursor = db.cursor()
            cursor.execute('''
INSERT INTO artist(name) VALUES (?)
''', (artist,))

def create_track():
    with sql.connect('SQLite/Musipedia/Music.db') as db:
        cursor = db.cursor()
        cursor.execute('''
SELECT id_artist, id, id_music_style FROM album
''')
        data = cursor.fetchall()
    for album in data:
        track = 1
        while track < 10:
            name_track = 'Track #' + str(track)
            with sql.connect('SQLite/Musipedia/Music.db') as db:
                cursor = db.cursor()
                cursor.execute('''
INSERT INTO track(name, id_artist, id_album, id_music_style, length_track) VALUES (?, ?, ?, ?, ?)
''', (name_track, *album, 180))
            track += 1
create_track()


# Упаковка (оператор *)
#var1 = 34
#var2 = 'Python'
#var3 = True
#*my_list, = var1, var2, var3
#print(my_list)
#
## Распаковка *
#list = [34, 'Hello', False] * 2
##a, b, c = list
##a, *b = list
#c, *a, b = list
#print(a, b, c)
#
#def f(*args):
#    print(args[2:5])
#
#f(23,32,6,7,98,34,65,8)
#
#Распаковка **

#def f(**kwargs):
#    print(kwargs)
#
#f(param1=34, param2='Python', param3=True)
#f(age=34, nick='Python', param3=True)

#Распаковка в цикле
#list_users = [
#    ['Joe', 'Byden'],
#    ['Donald', 'Trump'],
#    ['Micky', 'Mouse']
#]

#for name, last_name in list_users:
#    print(f'Name: {name}; Last name: {last_name}\n')
#line = -7, 10
#print(line)
#for i in range(*line):
#    print(i)

#print(*range(10))

#Есть некоторый словарь, который хранит названия
#стран и столиц. Название страны используется в качестве
#ключа, название столицыв качестве значения. Необходимо
#реализовать: добавление данных, удаление данных, поиск
#данных, редактирование данных, сохранение и загрузку
#данных (используя упаковку и распаковку).

#def add_data(country_dict):
#    data = input('Введите страну и столицу через пробел')
#    country, capital = data.split(' ')
#    if country in country_dict.keys():
#        print('Такая страна уже есть')
#    else:
#        country_dict[country] = capital
#    return country_dict
#
#def delete_data(country_dict):
#    data = input('Введите страну для удаления!')
#    if data in country_dict.keys():
#        del country_dict[data]
#        print(f'Страна {data} успешно удалена')
#    else:
#        print('Ошибка! Такой страны нет')
#    return country_dict
#
#def searche_data(country_dict):
#    data = input('Введите название страны или столицы')
#    for country, capital in country_dict.items():
#        if data == country or data == capital:
#            print(f'Результат поиска:\n {country} {capital}')
#            break
#    else:
#        print('Ничего не найдено!')
#    return country_dict
#
#def update_data(country_dict):
#    data = input('введите название страны и новое название столицы')
#    country, capital = data.split(' ')
#    country_dict[country] = capital
#    return country_dict
#
#def save_data(country_dict):
#    data = ''
#    for key, value in country_dict.items():
#        data += f'{key}:{value}\n'
#    with open('country_dict.txt','w') as file:
#        file.write(data)
#    return country_dict
#
#def load_data(country_dict):
#    with open('country_dict.txt', 'r') as file:
#        for line in file:
#            country, capital = line.split(':')
#            country_dict[country] = capital[:-1]
#    return country_dict
#
#
#country_dict = {}
#load_data(country_dict)
#while True:
#    print(country_dict)
#    choice = int(input('База стран и столиц\nМеню:\n1-добавить\n2-удалить\n3-поиск\n4-редактировать\n5-сохранение\n6-загрузка\n0-выход'))
#    if choice == 0:
#        save_data(country_dict)
#        break
#    elif choice == 1:
#        add_data(country_dict)
#    elif choice == 2:
#        delete_data(country_dict)
#    elif choice == 3:
#        searche_data(country_dict)
#    elif choice == 4:
#        update_data(country_dict)
#    elif choice == 5:
#        save_data(country_dict)
#    elif choice == 6:
#        load_data(country_dict)

#Задание 2
#Есть некоторый словарь, который хранит названия
#музыкальных групп(исполнителей) и альбомов. Название группы используется в качестве ключа, название
#альбомов в качестве значения. Необходимо реализовать:
#добавление данных, удаление данных, поиск данных,
#редактирование данных, сохранение и загрузку данных
#(используя упаковку и распаковку).
class Music:
    music_dict = {}

    def add_band(self, name_band):
        band = Band(name_band)
        self.music_dict[band.name] = band.disc_phia

# Удалить класс бэнд и оставить мьюзик, добавить в мьюзик методы

class Band:
    def __init__(self, name):
        self.name = name
        self.disc_phia = []

    def add_album(self, name_album):
        self.disc_phia.append(name_album)

spotify = Music()
spotify.add_band('Depeche Mode')
print(spotify.music_dict)
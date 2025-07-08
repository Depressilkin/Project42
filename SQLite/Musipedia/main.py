import sqlite3 as sql

class Menu:
    def __init__(self):
        self.migrate = Migrate()
    def main(self):
        while True:
            value = input('ИСКАТЬ:\n1-трек\n2-исполнитель\n3-альбом\n4-вывод всех исполнителей\n5-вывести полную информацию о всех треках\n6-альбомы Билли Айлиш')
            match value:
                case ('1'):
                    track = input('введите название трека')
                    self.migrate.get_track(track)
                case ('2'):
                    artist = input('введите название исполнителя')
                    self.migrate.get_artist(artist)
                case ('3'):
                    album = input('введите название альбома')
                    self.migrate.get_album(album)
                case ('4'):
                    self.migrate.get_all_artists()
                case ('5'):
                    self.migrate.get_full_info_track()
                case ('6'):
                    self.migrate.get_albums_billy_eilish()

class Migrate:
    def __init__(self):
        self.path = 'SQLite/Musipedia/Music.db'
    
    def get_track(self, name_track):
        try:
            with sql.connect(self.path) as db:
                cur = db.cursor()
                cur.execute('''
SELECT track.name, artist.name FROM track, artist
WHERE track.name = ? AND track.id_artist = artist.id
''', (name_track,))
                data = cur.fetchall()
                if data:
                    print('Результат поиска:')
                    for track in data:
                        print(f'{track[0]} - {track[1]}')
                else:
                    print('По запросу ничего не найдено')
        except:
            print('Ошибка с базой данных')

    def get_artist(self, name_artist):
        try:
            with sql.connect(self.path) as db:
                cur = db.cursor()
                cur.execute('''
SELECT track.name, artist.name
FROM track
JOIN artist ON artist.id = track.id_artist
WHERE artist.name = ?
''', (name_artist,))
                data = cur.fetchall()
                if data:
                    print(f'Результат поиска исполнителя {name_artist}:')
                    for track in data:
                        print(f'{track[0]}')
                else:
                    print('По запросу ничего не найдено')
        except:
            print('Ошибка с базой данных')

    def get_album(self, name_album):
        try:
            with sql.connect(self.path) as db:
                cur = db.cursor()
                cur.execute('''
SELECT album.name AS "name_album", album.data, artist.name AS "name_artist"
FROM album
JOIN artist ON album.id_artist = artist.id
WHERE album.name = ?
                            ''', (name_album,))
            data = cur.fetchall()
            if data:
                print('Результат поиска:')
                for album in data:
                    print(f'Испольнитель: {album[2]}, дата релиза: {album[1]}, название альбома {name_album}') 
            else:
                print('Ничего не найдено')
        except:
            print('Ошибка базы данных')
        

    def get_all_artists(self):
        try:
            with sql.connect(self.path) as db:
                cur = db.cursor()
                cur.execute('''
SELECT * FROM all_artists
                            ''')
            data = cur.fetchall()
            for artist in data:
                print(*artist)
        except:
            print('Упс, что-то пошло не так')
    
    def get_full_info_track(self):
        try:
            with sql.connect(self.path) as db:
                cur = db.cursor()
                cur.execute('''
SELECT * FROM full_info_track
                            ''')
            data = cur.fetchall()
            for track in data:
                print(f'Название: {track[0]}, испольнитель: {track[1]}, альбом: {track[2]}, длительность: {track[3]} сек.')
        except:
            print('Упс, что-то пошло не так')

    def get_albums_billy_eilish(self):
        try:
            with sql.connect(self.path) as db:
                cur = db.cursor()
                cur.execute('''
SELECT * FROM get_albums_billy_eilish
                            ''')
            data = cur.fetchall()
            print('Альбомы исполнителя Billy Eilish')
            for track in data:
                print(f'Название альбома: {track[0]}, дата выхода: {track[1]}')
        except:
            print('Упс, что-то пошло не так')

menu = Menu()
menu.main()
import sqlite3 as sql

with sql.connect('SQLite/Musipedia/Music.db') as db:
    cursor = db.cursor()
    cursor.execute('''
CREATE TABLE IF NOT EXISTS music_style(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL UNIQUE) ''')
    cursor.execute('''
CREATE TABLE IF NOT EXISTS artist(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL ) ''')
    cursor.execute('''
CREATE TABLE IF NOT EXISTS publisher(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL ) ''')
    cursor.execute('''
CREATE TABLE IF NOT EXISTS album(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
id_music_style INTEGER,
data TEXT NOT NULL, 
id_artist INTEGER,
id_publisher INTEGER,
FOREIGN KEY (id_music_style) REFERENCES music_style(id),
FOREIGN KEY (id_artist) REFERENCES artist(id),
FOREIGN KEY (id_publisher) REFERENCES publisher(id))''')
    
    cursor.execute('''
CREATE TABLE IF NOT EXISTS track(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
id_artist INTEGER,
id_album INTEGER,
id_music_style INTEGER,
length_track TEXT NOT NULL, 
FOREIGN KEY (id_music_style) REFERENCES music_style(id),
FOREIGN KEY (id_artist) REFERENCES artist(id),
FOREIGN KEY (id_album) REFERENCES album(id))''')
#    cursor.execute('''
#CREATE VIEW all_artists
#AS SELECT name FROM artist
#                   ''')
#    cursor.execute('''
#CREATE VIEW full_info_track
#AS SELECT track.name, artist.name, album.name, track.length_track
#FROM track, artist, album
#WHERE artist.id = track.id_artist AND  album.id = track.id_album''')
    cursor.execute('''
CREATE VIEW get_albums_billy_eilish
AS SELECT album.name, album.data
FROM album
WHERE album.id_artist = 3''')
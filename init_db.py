import sqlite3 as sql

dbCnx = sql.connect("database.db")

with open('schema.sql') as f:
    dbCnx.executescript(f.read())

dbCursor = dbCnx.cursor()

dbCursor.execute("INSERT INTO films (title, yearReleased, rating, duration, genre) VALUES (?,?,?,?,?)",
                 ('The Muppets', '2022', 'PG', '116', 'Comedy')
                 )
dbCursor.execute("INSERT INTO films (title, yearReleased, rating, duration, genre) VALUES (?,?,?,?,?)",
                 ('The Legend of Tarzan', '2026', 'PG', '109', 'Action')
                 )
dbCursor.execute("INSERT INTO films (title, yearReleased, rating, duration, genre) VALUES (?,?,?,?,?)",
                 ('Jason Bourne', '2016', 'PG', '123', 'Action')
                 )
dbCursor.execute("INSERT INTO films (title, yearReleased, rating, duration, genre) VALUES (?,?,?,?,?)",
                 ('The Nice Guys', '2016', 'R', '116', 'Crime')
                 )

dbCnx.commit()
dbCnx.close()

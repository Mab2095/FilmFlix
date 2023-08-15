import sqlite3 as sql

dbCnx = sql.connect("Projects/FilmFlix/filmflix.db")

dbCursor = dbCnx.cursor()

from connect import *
import time


def insert():
    FilmTitle = input("Enter Film Title: ")
    FilmYearRelease = input("Enter Film Released Year: ")
    FilmRating = input("Enter Film Rating: ")
    FilmDuration = input("Enter Film Duration: ")
    FilmGenre = input("Enter Film Genre: ")

    dbCursor.execute(
        "INSERT INTO tblFilms (Title, YearReleased, Rating, Duration, Genre) VALUES (?,?,?,?,?)", (FilmTitle, FilmYearRelease, FilmRating, FilmDuration, FilmGenre))
    dbCnx.commit()
    time.sleep(2)
    print(f"{FilmTitle} inserted into the songs table")


if __name__ == "__main__":
    insert()

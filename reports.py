from connect import *


# Show details of all films


def details():
    dbCursor.execute("SELECT * FROM tblFilms")

    allRecords = dbCursor.fetchall()

    for eachRecord in allRecords:
        print(eachRecord)


if __name__ == "__main__":
    details()

# Show all Animation Films


def genre():
    dbCursor.execute("SELECT * FROM tblFilms WHERE Genre = 'Animation' ")

    allRecords = dbCursor.fetchall()

    for eachRecord in allRecords:
        print(eachRecord)


if __name__ == "__main__":
    genre()

# Show Films from 2023


def year():
    dbCursor.execute("SELECT * FROM tblFilms WHERE YearReleased = 2023")

    allRecords = dbCursor.fetchall()

    for eachRecord in allRecords:
        print(eachRecord)


if __name__ == "__main__":
    year()

# Show Films Rated PG


def rating():
    dbCursor.execute("SELECT * FROM tblFilms WHERE Rating = 'PG' ")

    allRecords = dbCursor.fetchall()

    for eachRecord in allRecords:

        print(eachRecord)


if __name__ == "__main__":
    rating()

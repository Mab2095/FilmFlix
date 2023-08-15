from connect import *
import time


def update():
    idField = input("Enter the FilmID of the Film to be updated: ")

    fieldName = input(
        "Enter Title, YearReleased, Rating, Duration or Genre as Field Name: ")

    fieldValue = input(f"Enter the value for {fieldName}: ").title()

    fieldValue = "'"+fieldValue+"'"
    print(fieldValue)

    dbCursor.execute(
        f"UPDATE tblFilms SET {fieldName} = {fieldValue} WHERE filmID = {idField}")
    dbCnx.commit()

    time.sleep(2)
    print(f"Record {idField}  updated successfully, in FilmFlix table. ")


if __name__ == "__main__":
    update()

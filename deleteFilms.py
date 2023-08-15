from connect import *
import time


def delete():
    idField = input("Enter the FilmID of the Film to be deleted: ")

    dbCursor.execute(f"DELETE from tblFilms WHERE filmID = {idField} ")
    dbCnx.commit()

    time.sleep(2)
    print(f"Record {idField} deleted successfully, from Filmflix table. ")


if __name__ == "__main__":
    delete()

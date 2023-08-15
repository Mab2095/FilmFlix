import addFilms
import updateFilms
import deleteFilms
import showAll
import reportsMenu


def filmsMenuOptions():
    options = 0

    optionsList = ["1", "2", "3", "4", "5", "6"]

    userChoices = "FilmFlix\n Options Menu:\n1. Add Film.\n2. Delete Film.\n3. Update Film.\n4. Show all Films.\n5. Report.\n6. Exit."

    while options not in optionsList:
        print(userChoices)
        options = input("Enter an option from the FilmFlix choices above: ")

        if options not in optionsList:
            print(f"{options} is not a valid choice in the FilmFlix menu!")

    return options


mainProgram = True
while mainProgram:
    mainMenu = filmsMenuOptions()

    if mainMenu == "1":
        addFilms.insert()
    elif mainMenu == "2":
        deleteFilms.delete()
    elif mainMenu == "3":
        updateFilms.update()
    elif mainMenu == "4":
        showAll.show()
    elif mainMenu == "5":
        reportsMenu.runReportsMenu()
    else:
        mainProgram = False
        input("Press ENTER key to EXIT")

import reports


def filmsReportMenuOptions():
    options = 0

    optionsList = ["1", "2", "3", "4", "5"]

    userChoices = "FilmFlix Reports\n Reports Menu:\n1. Show details of all films.\n2. Show all Animation Films.\n3. Show Films Rated PG\n4. Show Films from 2023.\n5. Exit."

    while options not in optionsList:
        print(userChoices)
        options = input(
            "Enter an option from the FilmFlix Report choices above: ")

        if options not in optionsList:
            print(f"{options} is not a valid choice in the FilmFlix Report menu!")

    return options


def runReportsMenu():
    secondaryProgram = True
    while secondaryProgram:
        mainMenu2 = filmsReportMenuOptions()

        if mainMenu2 == "1":
            reports.details()
        elif mainMenu2 == "2":
            reports.genre()
        elif mainMenu2 == "3":
            reports.rating()
        elif mainMenu2 == "4":
            reports.year()
        else:
            secondaryProgram = False
            input("Press ENTER key to EXIT")

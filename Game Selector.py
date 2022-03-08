import random

def newList():
    gamesList = []
    numberOfGames = input("\nHow many games do you want to pick from? ")
    gamesNumber = int(numberOfGames)

    while gamesNumber < 2:
        print("\nYou need more than one game in your list.")
        numberOfGames = input("\nHow many games do you want to pick from? ")
        gamesNumber = int(numberOfGames)

    for i in range(gamesNumber):
         gamesList.append(input("Enter a game: "))
    print("New list created successfully. \n")
    return gamesList

def chooseGame(listOfGames):
    selectedGame = random.choice(listOfGames)
    print(selectedGame + " won.")
    return selectedGame

print("Welcome to Poonanji's game selector. For a list of commands, type 'help'.\nFirst, create a new list. ")
currentList = newList()
while True:
    userinput = input("Enter command: ")

    if userinput.lower() == "help":
        print("Here's a list of commands:\nnew\nchoose\nexit" )

    elif userinput.lower() == "new":
        currentList = newList()

    elif userinput.lower() == "choose":
        veto = 'y'
        while veto == 'y':
            selectedGame = chooseGame(currentList)
            veto = input("Does anyone veto " + selectedGame + " ? y/n ")
            if veto.lower() == 'y':
                makeNewListQuestion = input("Select from a new list? y/n ")
                if makeNewListQuestion.lower() == 'y':
                    currentList = newList()

    elif userinput == "exit":
        exit()
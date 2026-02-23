# This File is for the stand alone hangman game. It will be copy and pasted into TIArcade when finished.

# for clearing screen
def clear():
    for i in range(10):
        print()

# called once upon running
def startUp():
    print("welcome to Hangman\n Play With a friend or against TI-84\n\n1: Human\n2: TI-84")
    gameMode = int(input("Game Mode(Enter num): "))


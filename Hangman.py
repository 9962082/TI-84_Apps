import random
# This File is for the stand alone hangman game. It will be copy and pasted into TIArcade when finished.

# for clearing screen
def clear():
    for i in range(10):
        print()

# called once upon running
def startUp():
    print("welcome to Hangman\n Play With a friend or against TI-84\n\n1: Human\n2: TI-84")
    gameMode = int(input("Game Mode(Enter num): "))
    return gameMode

def hangman(isComputer):
    wordList = ["python", "java", "hangman", "programming", "computer", "science", "mathematics", "algorithm", "function", "variable", "algebra", "mitosis"]
    clear()
    if isComputer:
        correctWord = random.choice(wordList)
    else:
        correctWord = input("Player 1, enter a word: ").strip().lower()
    guessedLetters = []
    guessedWord = ["-"] * len(correctWord)
    guessesLeft = 6
    clear()
    while True:
        current = "".join(guessedWord)
        if current == correctWord:
            print("You win! Word:", correctWord)
            break
        if guessesLeft <= 0:
            print("No guesses left. Word was:", correctWord)
            break
        print("Guesses Left: ", guessesLeft)
        print("Incorrect Letters: ", guessedLetters)
        print(current)
        print()
        guessedLetter = input("Letter: ").strip().lower()
        if not guessedLetter or len(guessedLetter) != 1:
            print("Please enter a single letter.")
            continue
        if guessedLetter in guessedLetters or guessedLetter in guessedWord:
            print("Already guessed.")
            continue
        inWord = False
        for i in range(len(correctWord)):
            if correctWord[i] == guessedLetter:
                inWord = True
                guessedWord[i] = guessedLetter
        if not inWord:
            guessedLetters.append(guessedLetter)
            guessesLeft -= 1
        clear()

while True:
    gameMode = startUp()
    if gameMode == 1:
        hangman(False)
    elif gameMode == 2:
        try:
            hangman(True)
        except NameError:
            print("computerHangman() is not implemented.")
    else:
        print("invalid input")
    again = input("Play again? (y/n): ").strip().lower()
    if again != 'y':
        break
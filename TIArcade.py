import time
import math
import random

#clear screen fuction
def clear():
    for i in range(10):
        print()

#loading screen lasting seconds passed in as secs
def loading(secs):
    print("LOADING.", end="")
    for i in range(secs):
        print(".", end="\r")
        time.sleep(.7)

#startup screen that only runs when app is opened
def startup():
    start = str(input("Welcome to the TI Arcade! \n Press ENTER to start!\n\n\n\n\nTI Arcade v1.0\nBuild 2026.01"))
    if start != "":
        loading(5)
        clear()

#runs after startup and after quiting a game
def game_selector():
    games = ["blackJack", "reflex", "hangman", "battle"]
    print("Please enter the number of the game you want to play.")
    for i in range(0, len(games)):
        print(i+1, ". ", games[i])
    print()
    game_selected = str(input("Select a game: "))
    clear()
    loading(8)
    clear()
    if game_selected == "1":
        blackjack()
    elif game_selected == "2":
        reflex()
    elif game_selected == "3":
        hangman()
    elif game_selected == "4":
        battle()
    else:
        print("invalid input")

#blackjack game
#in future implement algorithm so computer hits strategicly
def blackjack():
    while True:
        print("welcome to blackjack! \n press ANY KEY to start")
        for i in range(3):
            print()
        total = 0
        starting_card_1 = random.randint(1, 12)
        starting_card_2 = random.randint(1,12)
        print("You are dealt a ", starting_card_1, " and a ", starting_card_2, ".")
        while total <= 21:
            hit = str(input("would you like to hit or stay?(y/n): "))
            print()
            if hit == "y":
                new_card = random.randint(1,12)
                print("you are dealt a ", new_card)
                total += new_card
            elif hit == "n":
                break
            else:
                print("invalid response")
        computer_total = random.randint(12,24)
        print("TI-84 ends with a ", computer_total)
        if computer_total > 21 and total <= 21 :
            print("The TI-84 busts. You win!")
        elif total  and computer_total >= 21:
            print("you bust. TI-84 wins!")
        elif computer_total > total:
            print("TI-84 got closer than you to 21. It wins!")
        else:
            print("you win!")
        continue_blackjack = str(input("New match?(y/n): "))
        if continue_blackjack == "y":
            continue
        if continue_blackjack =="n":
            break

#comand schedualer
startup()
while True:
    game_selector()
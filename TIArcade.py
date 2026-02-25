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
    start = str(input("Welcome to the TI Arcade! \n Press ENTER to start!\n\n\n\n\nTI Arcade v1.2\nBuild 2026.02"))
    if start == "":
        loading(5)
        clear()

#runs after startup and after quiting a game
def game_selector():
    games = ["blackJack", "reflex", "hangman", "pocket protocol"]
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
        try:
            reflex()
        except NameError:
            print("Reflex game is still in development. Please select another game.")
    elif game_selected == "3":
        while True:
            print("welcome to Hangman\n Play With a friend or against TI-84\n\n1: Human\n2: TI-84")
            gameMode = int(input("Game Mode(Enter num): "))
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
    elif game_selected == "4":
        try:
            battle()
        except NameError:
            print("Battle game is still in development. Please select another game.")
    else:
        print("invalid input")

#blackjack game
#in future implement algorithm so computer hits strategicly
def blackjack():
    while True:
        print("welcome to blackjack! \n press ANY KEY to start\n\n\n")
        player_total = random.randint(1, 12) + random.randint(1, 12)
        print("You are dealt a total of {}.").formart(player_total)
        
        while player_total <= 21:
            hit = input("would you like to hit?(y/n): ").strip().lower()
            if hit == "y":
                new_card = random.randint(1, 12)
                player_total += new_card
                print("you are dealt a {}. Total: {}\n").format(new_card, player_total)
            elif hit == "n":
                break
            else:
                print("invalid response\n")
        
        computer_total = random.randint(12, 24)
        print("TI-84 ends with a {}").format(computer_total)
        
        # Determine winner
        if player_total > 21 and computer_total > 21:
            print("Both bust! It's a tie!")
        elif player_total > 21:
            print("you bust. TI-84 wins!")
        elif computer_total > 21:
            print("The TI-84 busts. You win!")
        elif player_total > computer_total:
            print("you win!")
        elif computer_total > player_total:
            print("TI-84 got closer than you to 21. It wins!")
        else:
            print("It's a tie!")
        
        if input("New match?(y/n): ").strip().lower() != "y":
            break

#hangman game
def hangman(isComputer):
    wordList = ["python", "java", "hangman", "programming", "computer", "science", "mathematics", "guitar", "running", "variable", "biology", "mitosis", "playstation", "nintendo", "school", "book", "library", "coffee", "tea", "water", "bottle", "phone", "keyboard", "mouse", "monitor", "desk", "chair", "window", "door", "car", "bicycle", "airplane"]
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

#battle game

class Character:
    # constructor
    def __init__(self, name, max_hp, attack, defense, speed, max_heals):
        self.name = name

        # core stats
        self.hp = max_hp
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

        # Temporary stats
        self.is_defending = False
        self.heals_left = max_heals
    
    def attack_opponent(self, opponent):
        damage = self.attack
        if opponent.is_defending:
            damage = damage * (1 - opponent.defense)
        opponent.hp -= damage

    def defend(self):
        self.is_defending = True

    def heal(self):
        if self.heals_left > 0:
            heal_amount = self.max_hp // 4
            self.hp = min(self.hp + heal_amount, self.max_hp)
            self.heals_left -= 1

class Battle:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer
    
    def player_turn(self):
        print("your HP: {}/{} | Computer HP: {}/{}\nHeals left: {}\n".format(self.player.hp, self.player.max_hp, self.computer.hp, self.computer.max_hp, self.player.heals_left))
        print("Choose your action:\n1. Attack\n2. Defend\n3. Heal")
        action = input("Enter the number of your action: ").strip()
        
        if action == "1":
            self.player.attack_opponent(self.computer)
            print("You attack the computer!")
        elif action == "2":
            self.player.defend()
            print("You defend!")
        elif action == "3":
            self.player.heal()
            print("You heal!")
        else:
            print("Invalid action. Please try again.")
            self.player_turn()
    
    def computer_turn(self):
        if self.computer.hp <= self.computer.max_hp // 4 and self.computer.heals_left > 0:
            choices = ["attack", "attack", "attack", "defend", "defend", "defend", "heal", "heal","heal", "heal"]
        elif self.computer.hp <= self.computer.max_hp // 4:
            choices = ["attack", "attack", "attack", "defend", "defend",  "defend", "defend", "defend", "defend", "defend"]
        else:
            choices = ["attack", "attack", "attack", "attack", "defend", "defend", "defend", "heal","heal", "heal"]
        action = random.choice(choices)
        if action == "attack":
            self.computer.attack_opponent(self.player)
            print("The computer attacks you!")
        elif action == "defend":
            self.computer.defend()
            print("The computer defends!")
        elif action == "heal" and self.computer.heals_left > 0:
            self.computer.heal()
            print("The computer heals!")
        else:
            self.computer.attack_opponent(self.player)
            print("The computer attacks you!")

def choose_hero(hero_choice):
    if hero_choice == "1":
        player = Character("Warrior", 100, 20, 0.5, 10, 1)
    elif hero_choice == "2":
        player = Character("Goblin", 80, 15, 0.3, 20, 3)
    elif hero_choice == "3":
        player = Character("Wizard", 60, 25, 0.2, 15, 5)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        player = Character("Warrior", 100, 20, 0.5, 10, 1)
    return player

def battle():
    print("Welcome to pocket protocol!\n\n in this game, you will battle against the computer in a turn-based strategy game. \nYou can choose to attack, defend, or heal on your turn, while the computer will randomly choose one of these actions.\nThe game continues until either you or the computer's health reaches zero.")
    time.sleep(15)
    clear()
    print("Please choose your hero:\n1. Warrior\n2. goblin \n3. Wizard")

    hero_choice = input("Enter the number of your hero: ").strip()
    player = choose_hero(hero_choice)
    battle = Battle(player, choose_hero(random.choice(["1", "2", "3"])))
    
    while player.hp > 0 and battle.computer.hp > 0:
        battle.player_turn()
        clear()
        if battle.computer.hp <= 0:
            print("You win!")
            break
        battle.computer_turn()
        clear()
        if player.hp <= 0:
            print("You lose!")
            break

#comand schedualer
startup()
while True:
    game_selector()
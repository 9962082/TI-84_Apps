#   battle is a turn-based strategy game where the player and the computer take turns attacking each other until one of them runs out of health.
# The player can choose to attack, defend, or heal on their turn, while the computer will randomly choose one of these actions.
# The game continues until either the player or the computer's health reaches zero.
#  
#   This is my attempt at object-oriented programming in python, and I am still learning, so the code may not be perfect. 
# I am open to feedback and suggestions for improvement.
import random
import time
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

def clear():
    for i in range(10):
        print()

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
    
def main():
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
while True:
    main()
    again = input("Play again? (y/n): ").strip().lower()
    if again != 'y':
        break
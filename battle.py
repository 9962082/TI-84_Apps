#   battle is a turn-based strategy game where the player and the computer take turns attacking each other until one of them runs out of health.
# The player can choose to attack, defend, or heal on their turn, while the computer will randomly choose one of these actions.
# The game continues until either the player or the computer's health reaches zero.
#  
#   This is my attempt at object-oriented programming in python, and I am still learning, so the code may not be perfect. 
# I am open to feedback and suggestions for improvement.

class Character:
    # constructor
    def __init__(self, name, max_hp, attack, defense, speed):
        self.name = name

        # core stats
        self.hp = max_hp
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

        # Temporary stats
        self.is_defending = False
        self.heals_left = 3
    
    def attack_opponent(self, character):
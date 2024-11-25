### File #5

import time

#Type "Normal" for regular speed or "Fast" for debugging speed
quick = "Normal"
if quick == "Fast":
    typing = 0.0001
    typing1 = 0.0001
    typing2 = 0.0001
elif quick == "Normal":
    typing = 0.048 #Typing speed for regular text
    typing1 = 0.1 #Typing speed for background context
    typing2 = 0.024 #Typing speed for lists

#Does the time stuff
def typewriter(text, speed = typing):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()
def typewriter_input(prompt, speed = typing):
    for char in prompt: 
        print(char, end='', flush=True)
        time.sleep(speed)
    return input()

#Creates the player
class Player: 
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health
        self.attacks = {}
        self.healing_items = {}
    
    def perform_attack(self, attack_name):
        if attack_name:
            damage = self.attacks[attack_name]
            return damage
        else:
            typewriter("\nThe attack you are looking for is not avaliable. ")
            return 0
    
    def heal(self, item_name):
        if item_name in self.healing_items:
            healing = self.healing_items[item_name]
            self.health += healing
            del self.healing_items[item_name]
            return healing
        else:
            typewriter("\nInvalid healing item.")
            return 0

#Creates the enemy
class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

name = "PlayerName"
player = Player(name)
enemy = Enemy(name = "Mara the Rival", health = 50)

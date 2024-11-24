### File #4

from PartnerProjectClasses import *
import random


def difficulty():
    global level
    typewriter("\nChoose your difficulty level: ", speed = typing2)
    typewriter("1. Easy", speed = typing2)
    typewriter("2. Normal", speed = typing2)
    typewriter("3. Hard", speed = typing2)
    while True:
        level = typewriter_input("\nEnter the number of your choice: ")
        if level == "1":
            break
        elif level == "2":
            break
        elif level == "3":
            break
        else:
            typewriter("\nInvalid choice. Please enter a number between 1 and 3.")

guardian = Enemy(name="The Guardian", health=100)
def battle():
    while player.health > 0 and guardian.health > 0:
        #The player's turn.
        typewriter("\n\nIt's your turn. ")
        typewriter("\nChoose your attack: ")

        attack_list = list(player.attacks.keys())
        for i in range(len(attack_list)):
            typewriter(f"{i + 1}. {attack_list[i]}")
        
        while True:
            try:
                choice = int(typewriter_input("\nEnter the number of the attack you want to use: "))
                if 1 <= choice <= len(attack_list): #Calls the attack
                    attack_name = attack_list[choice - 1]
                    break
                else:
                    typewriter("\nInvalid choice. Please enter a valid nymber")
            except ValueError:
                typewriter("\nInvalid choice. Please enter a valid number")
        
        damage = player.perform_attack(attack_name) #Performs the attack
        guardian.health -= damage #Removes the damage from the guardian's health
        typewriter(f"\n\n{player.name} attacks {guardian.name} for {damage} damage. ")
        typewriter(f"\n{player.name} has {player.health} health left and {guardian.name} has {guardian.health} health left. ")

        if guardian.health <= 0: #Says the guardian has been defeated
            typewriter(f"\n{guardian.name} has been defeated! You have saved your brother!")
            break

        #POSSIBLE CODE
        if player.health < guardian.health:  # Optionally trigger healing when health is low
            print("\n\nYour health is becoming low. You can use one of the following healing items: ")
            health_list = list(player.healing_items.keys())
            for i in range(len(health_list)):
                typewriter(f"{i + 1}. {health_list[i]}")
        
            while True:
                try:
                    choice = int(typewriter_input("\nEnter the number of the healing item you want to use: "))
                    if 1 <= choice <= len(health_list): #Calls the healing item
                        item_name = health_list[choice - 1]
                        break
                    else:
                        typewriter("\nInvalid choice. Please enter a valid nymber")
                except ValueError:
                    typewriter("\nInvalid choice. Please enter a valid number")
            damage = player.heal(item_name) #Performs the heal
            player.health += damage
        
        if level == 1:
            damage = random.randint(3, 9) #Damages the player a random amount of damage
        if level == 2:
            damage = random.randint(8, 13) #Damages the player a random amount of damage
        if level == 3:
            damage = random.randint(12, 15) #Damages the player a random amount of damage
        
        player.health -= damage #Removes the damage from the player's health
        typewriter(f"\n\n{guardian.name} attacks you for {damage} damage. ")
        typewriter(f"\n{player.name} has {player.health} health left and {guardian.name} has {guardian.health} health left. ")


        if player.health <= 0: #Says the player has been defeated
            typewriter(f"\nYou have been defeated by {guardian.name}. Game over.")
            break

### File #3

from PartnerProjectFightScene import *
from PartnerProjectClasses import *
import os

def Name():
    global name
    name = typewriter_input("Enter your name: ").capitalize()

#Clears the screen for a better user experience
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#Sets up the characters abilities

#Puzzles
def riddle_puzzle():
    answer = name
    while True:
        response = typewriter_input("\nImagine you are the bus driver. 10 people get off at the first stop, 5 people get on at the next, 3 people get off and 7 people get on at the next. What does the bus driver go by:  ").capitalize()
        if response == answer:
            typewriter("\nCorrect! The door opens allowing you to proceed.")
            break
        else:
            typewriter("\nIncorrect, try again.")        

def number_lock_puzzle():
    correct_code = "120"
    while True:
        response = typewriter_input("\nWhat is 5!: ")
        if response == correct_code:
            typewriter("\nCorrect! The cabinet opens, revealing valuable supplies and a weapon.")
            break
        else:
            typewriter("\Incorrect, try again.")

#The inventory for all the items
inventory = []
visitedLocations = []
def visit_location(location):
    if location not in visitedLocations:
        visitedLocations.append(location)
        typewriter(f"\nThe locations you have entered are the following: ")
        for i, loc in enumerate(visitedLocations, start=1):
            typewriter(f"- {loc}", speed = 0.024)
    else:
        typewriter(f"\nThe locations you have entered are the following: ")
        for i, loc in enumerate(visitedLocations, start=1):
            typewriter(f"- {loc}", speed = 0.024)


#Function to manage inventory - DIFFERENT
def attack_inventory(item, damage):
    if item not in player.attacks:
        if len(player.attacks) >= 3:
            while True:
                choice = typewriter_input("\nYour attack inventory is full. Remove an item? Y/N: ").upper()
                if choice == "Y":
                    typewriter("\nYour current attack inventory:")
                    attack_list = list(player.attacks.items())
                    for i, (attack_item, attack_damage) in enumerate(attack_list):
                        typewriter(f"{i + 1}. {attack_item} ({attack_damage} damage)", speed = typing2)

                    while True:
                        try:
                            remove_choice = int(typewriter_input("\nEnter the number of the item you want to remove: "))
                            if 1 <= remove_choice <= len(attack_list):
                                item_to_remove = attack_list[remove_choice - 1][0]
                                del player.attacks[item_to_remove]
                                player.attacks[item] = damage
                                typewriter(f"\nYou removed {item_to_remove} and added {item}.")
                                return
                            else:
                                typewriter("\nInvalid choice. Please select a valid number.")
                        except ValueError:
                            typewriter("\nInvalid input. Please enter a number.")
                elif choice == "N":
                    return
                else:
                    typewriter("\nPlease enter Y or N.")
        else:
            player.attacks[item] = damage
            typewriter(f"\n\nYou have added {item} to your inventory. It deals {damage} damage.")
    else:
        typewriter(f"\nYou already have {item} in your inventory.")

def healing_inventory(item, healing_value):
    if item not in player.healing_items:
        if len(player.healing_items) >= 3:
            while True:
                choice = typewriter_input("\nYour healing inventory is full. Remove an item? Y/N: ").upper()
                if choice == "Y":
                    typewriter("\nYour current healing inventory:")
                    heal_list = list(player.healing_items.items())
                    for i, (heal_item, heal_value) in enumerate(heal_list):
                        typewriter(f"{i + 1}. {heal_item} ({heal_value} HP)", speed = typing2)

                    while True:
                        try:
                            remove_choice = int(typewriter_input("\nEnter the number of the healing item you want to remove: "))
                            if 1 <= remove_choice <= len(heal_list):
                                item_to_remove = heal_list[remove_choice - 1][0]
                                del player.healing_items[item_to_remove]
                                player.healing_items[item] = healing_value
                                typewriter(f"\nYou removed {item_to_remove} and added {item}.")
                                return
                            else:
                                typewriter("\nInvalid choice. Please select a valid number.")
                        except ValueError:
                            typewriter("\nInvalid input. Please enter a number.")
                elif choice == "N":
                    return
                else:
                    typewriter("\nPlease enter Y or N.")
        else:
            player.healing_items[item] = healing_value
            typewriter(f"\nYou have added {item} to your healing inventory. It restores {healing_value} health.")
    else:
        typewriter(f"\nYou already have {item} in your healing inventory.")

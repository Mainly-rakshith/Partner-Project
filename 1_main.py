### File #1

"""
==================================================================================================================================
========================================================================================================================
Program By: Rakshith Jayakarthikeyan
========================================================================================================================
VERSIONS:
1.0 - Initial Release
- Included player and enemy classes
- Very basic introduction of the game and user
- Defined bunch of room functions such as managing inventory of items, riddles, and next locations
- Last room included the final fight of the game with attack mechanics

1.1 - Update 
- Included typewriter function to make certain messages appear to be "texted" in the terminal output
- Included .sleep function to allow user to read the terminal output
- Included visited inventory so game doesn't allow user to enter final room unless required rooms have been visited
- Changed manage inventory to attack inventory and added a healing inventory for healing items to be used in fight

1.2 - Updates 2 [Pre-Thanksgiving Break]
- Includes code being encased in multiple appropriately named files to improve organization
- Includes gender based terminal outputs
- Includes game difficulty; changes computer's attack strength based on input
- Clears screen after game and player background
- Upgraded riddle to make it less confusing and more challenging

========================================================================================================================
To Do:
- Ask how to do assign a gender based on the user's name. 

Known Issues:
- Some attack effects [damage/healing] are not balanced. Adjust for gameplay fairness.
- Keeps printing "PlayerName" instead of the user's name whenever player's name is printed in terminal output.

Future Enhancements:
- Implement multiplayer mode.
- Design some animations 

Code Considerations:
- Be mindful of the game's memory usage when adding new features.
- Code being used in majority of files must be called in the files following the one using it

Developer Notes:
- When trying to debug the game, you can change the variable "quick" to change the typing speed in PartnerProjectClasses

Updated To GitHub Last On:
- 11/23/2024 -- 8:13 PM

========================================================================================================================
==================================================================================================================================
"""


from PartnerProjectRooms import *
from PartnerProjectExtraFunctions import *
from PartnerProjectFightScene import *
from PartnerProjectClasses import *

#Call the name function
Name()

while True:
    gender = typewriter_input("\nEnter your gender (M/F): ").upper()
    if gender == "M":
    #Lets the character choose the class of character and their ability
        while True:
            typewriter("\nWhat class of character would you like to choose?")
            typewriter("""1. King
2. Prince
3. Lord""", speed = typing2)
            classofcharacter = typewriter_input("\nEnter the number of the class you would like to have: ")
            if classofcharacter == "1":
                classofcharacter = "King"
                break
            elif classofcharacter == "2":
                classofcharacter = "Prince"
                break
            elif classofcharacter == "3":
                classofcharacter = "Lord"
                break
            else:
                typewriter("\nInvalid choice. Please enter a number between 1 and 3.")
        break
    elif gender == "F":
        #Lets the character choose the class of character and their ability
        while True:
            typewriter("\nWhat class of character would you like to choose?")
            typewriter("""\n1. Queen
2. Princess
3. Lady""", speed = typing2)
            classofcharacter = typewriter_input("\nEnter the number of the class you would like to have: ")
            if classofcharacter == "1":
                classofcharacter = "Queen"
                break
            elif classofcharacter == "2":
                classofcharacter = "Princess"
                break
            elif classofcharacter == "3":
                classofcharacter = "Lady"
                break
            else:
                typewriter("\nInvalid choice. Please enter a number between 1 and 3.")
        break
    else:
        typewriter(f"\nInvalid choice. {gender} is not a gender.")


while True:
    typewriter("\n\nWhat ability would you like to have?")
    typewriter("""1. Athletisism
2. Intelligence
3. Trickster""", speed = typing2)
    abilities = typewriter_input("\nEnter the number of the ability you would like to have: ")
    if abilities == "1":
        abilities = "athletisism"
        break
    elif abilities == "2":
        abilities = "intelligence"
        break
    elif abilities == "3":
        abilities = "trickster"
        break
    else:
        typewriter("\nInvalid choice. Please enter a number between 1 and 3.")

intro = typewriter_input("\nWould you like to get background on the characters of the game? Y/N: ").upper()

if intro == "Y":    
    if gender =="M":
        typewriter(f"""
The main character of the game is {name}. {name} is a {classofcharacter} who has 100 health, 75 strength, 25 stamina, 135 speed, and 40 attack power. 
He has a motivation to find his lost sibling and goes through numerous challenges and encounters Mara and the Guardian.

Mara is a rival scavenger. She is a side character that has 50 health, 40 stength, 15 stamina, 75 speed, and 20 attack power. 
She used to be part of a community that fell apart but now is looking to seek power

The Guardian is a mentor. He is a side character who has 100 health, 75 stength, 25 stamina, 135 speed, and 40 attack power. 
He was once a scholar but is now a mysterious person who has knowledge of the old world. """, speed = typing2)
        time.sleep(5)
    elif gender == "F":
        typewriter(f"""
The main character of the game is {name}. {name} is a {classofcharacter} who has 100 health, 75 strength, 25 stamina, 135 speed, and 40 attack power. 
She has a motivation to find her lost sibling and goes through numerous challenges and encounters Mara and the Guardian.

Mara is a rival scavenger. She is a side character that has 50 health, 40 stength, 15 stamina, 75 speed, and 20 attack power. 
She used to be part of a community that fell apart but now is looking to seek power

The Guardian is a mentor. He is a side character who has 100 health, 75 stength, 25 stamina, 135 speed, and 40 attack power. 
He was once a scholar but is now a mysterious person who has knowledge of the old world. """, speed = typing2)
        time.sleep(5)
else:
    pass

#Gives the user an intro and information about each character
typewriter(f"""

Welcome to the start of your adventure {name}! 

You are a {classofcharacter} with {abilities}. 

Your health is 100.

The main objective in this game is to find your brother in a post-apocalyptic adventure. 

Along the way in each location, you may find one item in each room.

Each time your inventory is greater than or equal to 3, you will have an option to remove any items from your inventory.""", speed = typing1)

#Starts the game
while True:
    startGame = typewriter_input("\nWould you like to start the game? Y/N: ").upper()
    if startGame == "Y":
        difficulty()
        clear_screen()
        overgrownLibrary()
        break
    elif startGame == "N":
        typewriter("\nType 'Y' whenever you are ready to start the game. ")
    else:
        typewriter("\nPlease enter a valid option. ")

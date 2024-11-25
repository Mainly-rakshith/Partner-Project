### File #2

from PartnerProjectExtraFunctions import *
from PartnerProjectFightScene import *
from PartnerProjectClasses import *

#The starting location for the game and also the addition of a pepper spray. 
def overgrownLibrary():
    global inventory
    attack_inventory("Pepper spray", 5) #Adds pepper spray to inventory along with the damage it causes
    healing_inventory("Chug jug", 15)
    #Print the visited locations function where it gives a list of visited locations
    visit_location("Overgrown library") #Moves to the location the user chooses
    next_location("Overgrown library") #Moves to the location the user chooses

#The second location for the game and also the addition of a taser. 
def burnedOutSchool():
    global inventory
    attack_inventory("Taser", 10) #Adds ________ to inventory along with the damage it causes
    healing_inventory("Flowberry fizz", 12)
    visit_location("Burned out school") #Moves to the location the user chooses
    next_location("Burned out school") #Moves to the location the user chooses

#The third location for the game and also the addition of a baton
def crumblingHospital():
    global inventory
    attack_inventory("Baton", 7) #Adds ________ to inventory along with the damage it causes
    healing_inventory("Big pot", 12)
    visit_location("Crumbling hospital") #Moves to the location the user chooses
    next_location("Crumbling hospital") #Moves to the location the user chooses

#The fourth location for the game and also the attraction of a knife
def abandonedCitySquare():
    global inventory
    attack_inventory("Knife", 8) #Adds ________ to inventory along with the damage it causes
    healing_inventory("Slurp juice", 13)
    visit_location("Abandoned city square") #Moves to the location the user chooses
    next_location("Abandoned city square") #Moves to the location the user chooses

#The fifth location for the game and also the attraction of a handgun
def ruinedFactory():
    global inventory
    #Say if this location isn't in visited locations, it prints what is below
    if "Ruined factory" not in visitedLocations:
        typewriter("\n\nYou have found your apprentice, Mara. She will come along with you on your journey.")
        riddle_puzzle()
    attack_inventory("Handgun", 12) #Adds ________ to inventory along with the damage it causes
    healing_inventory("Flopper", 8)
    visit_location("Ruined factory") #Moves to the location the user chooses
    next_location("Ruined factory") #Moves to the location the user chooses

#The sixth location for the game and also the attraction of a axe
def hiddenGarden():
    global inventory
    attack_inventory("Axe", 11) #Adds ________ to inventory along with the damage it causes
    healing_inventory("Slurpfish", 8)
    visit_location("Hidden garden") #Moves to the location the user chooses
    next_location("Hidden garden") #Moves to the location the user chooses

#The seventh location for the game and also the attraction of a bow and arrow
def collapsedSubwayTunnel():
    global inventory
    attack_inventory("Bow and arrow", 13) #Adds ________ to inventory along with the damage it causes
    healing_inventory("Med kit", 10)
    visit_location("Collapsed subway tunnel") #Moves to the location the user
    next_location("Collapsed subway tunnel") #Moves to the location the user chooses

#The eight location for the game and also the attraction of a machine gun
def floodedBunker():
    global inventory
    attack_inventory("Machine gun", 15) #Adds ________ to inventory along with the damage it causes
    healing_inventory("Med mist", 10)
    visit_location("Flooded bunker") #Moves to the location the user chooses
    next_location("Flooded bunker") #Moves to the location the user chooses
    

#The ninth location for the game and also the attraction of a sniper rifle
def radioTower():
    global inventory
    attack_inventory("Sniper rifle", 14) #Adds ________ to inventory along with the damage it causes
    healing_inventory("Small pot", 8)
    visit_location("Radio tower") #Moves to the location the user chooses
    next_location("Radio tower") #Moves to the location the user chooses

#The final location for the game and also the attraction of a invisibility cloak
def guardiansLair():
    global inventory
    required_locations = {"Crumbling hospital", "Collapsed subway tunnel", "Radio tower"}
    visited_set = set(visitedLocations)
    if required_locations.issubset(visited_set):
        typewriter("\nYou are at an old place where the Guardian lives; the final battle happens here.")
        number_lock_puzzle()
        attack_inventory("Nuclear bomb", 15)
        healing_inventory("Guzzle juice", 10)
        clear_screen
        typewriter(f"\nThe final battle begins! {player.name} vs {guardian.name}. ")
        battle()
    else:
        #Print a list of missing locations not visited
        missing_locations = required_locations - visited_set
        typewriter("\nYou are missing the following locations:")
        for location in missing_locations:
            typewriter(f"- {location}", speed = typing2)
        floodedBunker()


#Make a list for the options of the next locations. - DIFFERENT
def next_location(current_room):
    rooms = {
        "Overgrown library": {"Description": "\nYou are at a quiet, creepy place with lots of plants and old books full of forgotten knowledge.", "directions": {"East (Abandonded City Square)": abandonedCitySquare, "Southeast (Ruined Factory)": ruinedFactory, "South (Burned-out School)": burnedOutSchool}},
        "Burned out school": {"Description": "\nYou are at a scary reminder of the town's past with burned walls and reminders of a lost world.", "directions": {"North (Overgrown Library)": overgrownLibrary, "Northeast (Abandoned City Square)": abandonedCitySquare, "East (Ruined Factory)": ruinedFactory, "Southeast (Hidden Garden)": hiddenGarden, "South (Crumbling Hospital)": crumblingHospital}},
        "Crumbling hospital": {"Description": "\nYou are at a lonely, falling-apart hospital with broken and old medical stuff and notes from people who died before the disaster.", "directions": {"North (Burned-out School)": burnedOutSchool, "Northeast (Ruined Factory)": ruinedFactory, "East (Hidden Garden)": hiddenGarden}},
        "Abandoned city square": {"Description": "\nYou are at a central place for people looking for possessions, but watch out for traps and other people also looking for belongings.", "directions": {"West (Overgrown Library)": overgrownLibrary, "Southwest (Burned-out School)": burnedOutSchool, "South (Ruined Factory)": ruinedFactory, "Southeast (Flooded Bunker)": floodedBunker, "East (Collapsed Subway Tunnel)": collapsedSubwayTunnel}},
        "Ruined factory": {"Description": "\nThe room you are in is filled with broken machines, dangerous traps, and a place to find cool stuff.", "directions": {"North (Abandoned City Square)": abandonedCitySquare, "Northeast (Collapsed Subway Tunnel)": collapsedSubwayTunnel, "East (Flooded Bunker)": floodedBunker, "Southeast (Radio Tower)": radioTower, "South (Hidden Garden)": hiddenGarden, "Southwest (Crumbling Hospital)": crumblingHospital, "West (Burned-out School)": burnedOutSchool, "Northwest (Overgrown Library)": overgrownLibrary}},
        "Hidden garden": {"Description": "\nYou are at a wild place with plants that can help you heal.", "directions": {"West (Crumbling Hospital)": crumblingHospital, "Northwest": burnedOutSchool, "North (Ruined Factory)": ruinedFactory, "Northeast (Flooded Bunker)": floodedBunker, "East (Radio Tower)": radioTower}},
        "Collapsed subway tunnel": {"Description": "\nThe room you are in is a dark, shaky tunnel full of random creatures; be really careful if you go near it.", "directions": {"West (Abandoned City Square)": abandonedCitySquare, "Southwest (Ruined Factory)": ruinedFactory, "South (Flooded Bunker)": floodedBunker, "Southeast (Guardian's Lair)": guardiansLair}},
        "Flooded bunker": {"Description": "\nYou are at an old underground base with old supplies that could last a soldier 3 years. ", "directions": {"North (Collapsed Subway Tunnel)": collapsedSubwayTunnel, "East (Guardian's Lair)": guardiansLair, "South (Radio Tower)": radioTower, "Southwest (Hidden Garden)": hiddenGarden, "West (Ruined Factory)": ruinedFactory, "Northwest (Abandoned City Square)": abandonedCitySquare}},
        "Radio tower": {"Description": "\nYou are at a tall place where old signals can be found, but there are lots of people trying to keep it safe.", "directions": {"West (Hidden Garden)": hiddenGarden, "Northwest (Ruined Factory)": ruinedFactory, "North (Flooded Bunker)": floodedBunker, "Northeast (Guardian's Lair)": guardiansLair}}
    }
    
    while True:
        typewriter(rooms[current_room]["Description"])
        typewriter("\n\nPossible directions:")
        
        # Display the available directions with numbers
        direction_list = list(rooms[current_room]["directions"].keys())
        for i, direction in enumerate(direction_list):
            typewriter(f"{i + 1}. {direction}", speed = typing2)
        
        # Get user input by number
        try:
            choice = int(typewriter_input("\nEnter the number of the direction you'd like to go: "))
            if 1 <= choice <= len(direction_list):
                selected_direction = direction_list[choice - 1]
                next_room = rooms[current_room]["directions"][selected_direction]
                next_room()  # Call the function for the next room
                break
            else:
                typewriter("\nInvalid choice. Please select a valid number.")
        except ValueError:
            typewriter("\nInvalid input. Please enter a number.")

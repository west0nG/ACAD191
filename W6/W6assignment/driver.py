'''
Weston Guo
ACAD 191, Fall 2025
westongu@usc.edu
Homework 4
'''

from hero import Hero

# Global list to store all heroes
heroes = []

#main function
def __main__():
    continueMenu = True
    while continueMenu == True:
        printMenu()
        option = input(">")
        if option == "1":
            loadHeroes()
        elif option == "2":
            printRoster()
        elif option == "3":
            herofight()
        elif option == "4":
            quit()
        else:
            print("Please enter a valid option.")
            print("****************************************")#for formatting
    return None

def printMenu():
    print("Choose an option:\n1. Load Heroes\n2. Print Hero Roster\n3. Hero Fight!\n4. Quit")
    return None

#will be done in the later assignment
def herofight():
    print("Stay tuned for the fight of the century!")
    print("****************************************")#for formatting
    return None

#loads heroes from heroes.txt file
def loadHeroes():
    try:
        with open("heroes.txt","r") as file:
            for line in file:
                # Skip empty lines
                if line.strip():
                    hero = Hero(line)
                    heroes.append(hero)
            print(f"{len(heroes)} heroes loaded.")
            print("****************************************")#for formatting
    except FileNotFoundError:
        print("File not found.")
    return None


def printRoster():
    print(f"The following {len(heroes)} heroes are loaded...")
    for hero in heroes:
        print("****************************************")#for formatting
        hero.printPowers()
    print("****************************************")#for formatting
    return None

def quit():
    print("Goodbye!")
    continueMenu = False
    return None

if __name__ == "__main__":
    __main__()

    
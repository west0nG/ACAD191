'''
Weston Guo
ACAD 191, Fall 2025
westongu@usc.edu
Lab 6
'''
from die import Die

def rollDice(dice):
    total = 0
    for die in dice:
        total += die.roll()
    return total

def printDice(Dice):
    for i, die in enumerate(Dice, 1):
        print(f"#{i} : {die}")

def main():
    Dice = []
    continueRoll = True
    sides = int(input("How many sides does your dice have? "))
    amount = int(input("How many dice do you have? "))

    for i in range(amount):
        die = Die(sides)
        Dice.append(die)

    while continueRoll ==True:
        roll = input("Roll (y/n)?")
        if roll == "y":
            rollDice(Dice)
            printDice(Dice)
        elif roll == "n":
            print("Goodbye!")
            continueRoll = False
        else:
            print("Please enter y or n.")

if __name__ == "__main__":
    main()


        
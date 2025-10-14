'''
Weston Guo
ACAD 191, Fall 2025
westongu@usc.edu
Homework 4
'''

class Hero:
    def __init__(self, input_string: str):
        parts = input_string.strip().split('|')
        self._heroName: str = parts[0]
        self._power: list[str] = parts[1].split(',')
        self._maxHP: int = int(parts[2])
        self._currentHP: int = int(parts[2])
        return None

    def getName(self):
        return self._heroName

    def getHealth(self):
        return self._currentHP

    def __str__(self):
        powers = '\n'.join(self._power)
        return powers

    def printHealth(self):
        print(f"{self._heroName} has the {self._currentHP} health points.")

    def printPowers(self):
        print(f"{self._heroName} has the following powers...\n{str(self)}")

#test function
def __main__():
    hero = Hero("Iron Man|Fly,Power,Money|7")

    print(hero.getName())
    print(hero.getHealth())
    print(hero.__str__())
    hero.printPowers()

if __name__ == "__main__":
    __main__()




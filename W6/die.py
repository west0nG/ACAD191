'''
Weston Guo
ACAD 191, Fall 2025
westongu@usc.edu
Lab 6
'''
import random

class Die:


    def __init__(self, sides=6):
        self.__sides = sides
        self.__result = 0

    def roll(self):
        self.__result = random.randint(1, self.__sides)
        return self.__result

    def __str__(self):
        return str(self.__result)
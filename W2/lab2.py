'''
Weston Guo
ACAD 191, Fall 2025
westongu@usc.edu
Lab 2
'''

userInput = input("Enter a phrase you want! Enter nothing to exit.")
vowelCount = 0
while userInput != "":
    for character in userInput:
        if character in "aeiouAEIOU":
            vowelCount += 1
    print(f"There are {vowelCount} vowels in {userInput}")
    vowelCount = 0 
    userInput = input("Enter a phrase you want! Enter nothing to exit.")

'''
Weston Guo
ACAD 191, Fall 2025
westongu@usc.edu
Lab 4
'''

import random



# create a dictionary to store the factors
factorDictionary = {}
for i in range(2,62):
    factorDictionary[i] = 0

#print(factorDictionary)

userInput = input("Give me a number: ")
while userInput != "":
    # generate an array of random numbers
    randomNumberArray = []
    for i in range(int(userInput)):
        randomNumberArray.append(random.randrange(0,45000))
    #print(randomNumberArray)

    for randomNumber in range(len(randomNumberArray)):
        for factor in range(2,62):
            if randomNumberArray[randomNumber] % factor == 0:
                factorDictionary[factor] += 1

    # program output
    print(f"For {userInput} random numbers, the factors frequencies are:")
    for factor in range(2,62):
        if factorDictionary[factor] > 0:
            print(str(factor) + " : " + str(int(factorDictionary[factor])*"*"))
    
    for factor in range(2,62):
        factorDictionary[factor] = 0

    userInput = input("Give me a number: ")




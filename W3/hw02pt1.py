'''
Weston Guo
ACAD 191, Fall 2025
westongu@usc.edu
Assignment 2
'''
import random

wordList = ["love","typical","microsoft","google","amazon","meta","stanford","usc","ucla","iya"]\

wordListJumbled = []
for word in wordList:
    letters = list(word)
    jumbled = ''
    while True:
        availableLetters = letters[:]
        jumbledLetters = []
        while availableLetters:
            chosenLetter = random.choice(availableLetters)
            jumbledLetters.append(chosenLetter)
            availableLetters.remove(chosenLetter)
        jumbled = ''.join(jumbledLetters)
        if jumbled != word:
            break
    wordListJumbled.append(jumbled)

wordDictionary = {}
for i in range(len(wordList)):
    wordDictionary[wordListJumbled[i]] = wordList[i]

count = 1
randomJumbledWord = random.choice(wordListJumbled)
while True:

    print("The jumbled word is: '" + randomJumbledWord + "'")
    userInput = input("Please enter your guess: ")
    if userInput == wordDictionary[randomJumbledWord]:
        print("You got it!")
        print("It took you " + str(count) + " tries.")
        break
    else:
        print("Incorrect!")
        count += 1




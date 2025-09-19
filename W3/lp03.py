'''
Weston Guo
ACAD 191, Fall 2025
westongu@usc.edu
Lab 3
'''


fictionWords = ["gren", "fral", "drel", "fron", "glud", "zarp", "nark"]


inputString = input("What shall I censor? ")

while inputString != "":
    words = inputString.split()
    censoredWords = []
    for word in words:
        if word.lower() in fictionWords:
            censoredWords.append("BEEP")
        else:
            censoredWords.append(word)
    
    censoredText = "".join(censoredWords)
    print(censoredText)
    
    inputString = input("What shall I censor? ")

print("Goodbye!")
'''
Weston Guo
ACAD 191, Fall 2025
westongu@usc.edu
Assignment 2 - Part 2: Caesar Cipher
'''

messageInput = input("Enter a message: ")
shiftAmount = int(input("Enter a number to shift by (0-25): "))

originalMessage = messageInput

alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


cipherList = alphabetList[shiftAmount:] + alphabetList[:shiftAmount]


print("Encrypting message....")
encryptedMessage = ""
for singleChar in messageInput:
    if singleChar.isalpha():
        lowerChar = singleChar.lower()
        if lowerChar in alphabetList:
            charIndex = alphabetList.index(lowerChar)
            encryptedChar = cipherList[charIndex]
            if singleChar.isupper():
                encryptedChar = encryptedChar.upper()
            encryptedMessage += encryptedChar
        else:
            encryptedMessage += singleChar
    else:
        encryptedMessage += singleChar

print(f"Encrypted message: {encryptedMessage}")


print("Decrypting message....")
decryptedMessage = ""
for singleChar in encryptedMessage:
    if singleChar.isalpha():
        lowerChar = singleChar.lower()
        if lowerChar in cipherList:
            charIndex = cipherList.index(lowerChar)
            decryptedChar = alphabetList[charIndex]
            if singleChar.isupper():
                decryptedChar = decryptedChar.upper()
            decryptedMessage += decryptedChar
        else:
            decryptedMessage += singleChar
    else:
        decryptedMessage += singleChar

print(f"Decrypted message: {decryptedMessage}")
print(f"Original message: {originalMessage}")

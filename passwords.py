from time import sleep as s
from random import randint as ri
from timeit import default_timer as timer
import sys

mostCommonPasswords = [
    "1", "12", "123", "1234", "13245", "123456", "1234567", "13245678",
    "123456789", "password", "11", "111", "1111", "11111", "111111", "1111111",
    "sunshine", "qwerty", "iloveyou", "princess", "admin", "welcome", "666666",
    "abc123", "football", "123123", "monkey", "654321", "!@#$%^&*", "charlie",
    "aa123456", "donald", "password1", "qwerty123"
]
charArray = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4",
    "5", "6", "7", "8", "9", "0"
]

done = False
guessedPasswords = []
totalGuesses = 0
red = '\033[93m'
green = '\033[92m'

inputPassword = input("What is your pasword?\n")

startOf = timer()
for password in mostCommonPasswords:
    if not done:
        bigboi = False
        if len(password) > 7:
            bigboi = True

        if password == inputPassword:
            if bigboi:
                print("%s			-	Correct\r" % password, end='')
            elif len(password) > 3:
                print("%s				-	Correct\r" % password, end='')
            else:
                print("%s					-	Correct\r" % password, end='')
            done = True
        else:
            if bigboi:
                print("%s			-	Incorrect\r" % password, end='')
            elif len(password) > 3:
                print("%s				-	Incorrect\r" % password, end='')
            else:
                print("%s					-	Incorrect\r" % password, end='')

while not done:
    finalPass = []
    passLength = ri(1, 20)

    guessAmount = 1
    for i in range(passLength):
        randomInt = ri(0, len(charArray) - 1)
        randomChar = charArray[randomInt]
        finalPass.append(randomChar)

    finalPass = "".join(finalPass)

    while finalPass in guessedPasswords:
        finalPass = []
        passLength = ri(1, 20)
        guessAmount = guessAmount + 1
        for i in range(passLength):
            randomInt = ri(0, len(charArray) - 1)
            randomChar = charArray[randomInt]
            finalPass.append(randomChar)
        finalPass = "".join(finalPass)

    guessedPasswords.append(finalPass)
    totalGuesses = totalGuesses + 1
    if finalPass == inputPassword:
        if passLength > 15:
            print("%s	-	Correct		-	%s	-	%s\r" %
                  (finalPass, guessAmount, totalGuesses), end='')
        elif passLength > 10:
            print("%s		-	Correct		-	%s	-	%s\r" %
                  (finalPass, guessAmount, totalGuesses), end='')
        elif passLength > 7:
            print("%s		-	Correct		-	%s	-	%s\r" %
                  (finalPass, guessAmount, totalGuesses), end='')
        elif passLength > 5:
            print("%s			-	Correct		-	%s	-	%s\r" %
                  (finalPass, guessAmount, totalGuesses), end='')
        else:
            print("%s			-	Correct		-	%s	-	%s\r" %
                  (finalPass, guessAmount, totalGuesses), end='')
        endOf = timer()
        print("Guessed in %ss" % (endOf - startOf))
        done = True

    else:
        if passLength > 15:
            print("%s	-	Incorrect	-	%s	-	%s\r" %
                  (finalPass, guessAmount, totalGuesses), end='')
        elif passLength > 10:
            print("%s		-	Incorrect	-	%s	-	%s\r" %
                  (finalPass, guessAmount, totalGuesses), end='')
        elif passLength > 7:
            print("%s		-	Incorrect	-	%s	-	%s\r" %
                  (finalPass, guessAmount, totalGuesses), end='')
        elif passLength > 5:
            print("%s			-	Incorrect	-	%s	-	%s\r" %
                  (finalPass, guessAmount, totalGuesses), end='')
        else:
            print("%s			-	Incorrect	-	%s	-	%s\r" %
                  (finalPass, guessAmount, totalGuesses), end='')

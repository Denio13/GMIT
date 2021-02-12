#The program to generate a random number between 0 and 100 to guess 

#Author: Denis Sarf


import random # importing the random module

numberToGuess = random.randint(0, 100)
print(numberToGuess) #check a random number

guess = int(input("Please guess the number:"))

while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else: #  it cant be equal or too low, so it must be too high
        print("too high")
    guess = int(input("Please guess again:"))

print("Well done! Yes the number was ", numberToGuess)


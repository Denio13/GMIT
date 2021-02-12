# Program that asks the user to enter in a number and
# the program will show the number is even or odd 

#Author: Denis Sarf


number = int(input("Enter an integer:"))

if (number % 2) == 0:
    print ("{} is an even number".format(number))
else:
    print("{} is an odd number".format(number))
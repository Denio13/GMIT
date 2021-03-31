# The program that takes asks a user to input a string and outputs every second letter in reverse order
# Author: Denis Sarf

# input the string
string = input("Please enter a string:")

# take every second letter
str_second_letter = string[1::2]

# output letters in reverse order 
print(str_second_letter[::-1])
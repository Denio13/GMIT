# The program that takes asks a user to input a string and outputs every second letter in reverse order
# Author: Denis Sarf


string = input("Please enter a sentence:")

str_second_letter = string[1::2]
reverse_string = str_second_letter[::-1]

print(reverse_string)
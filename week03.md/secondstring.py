#The program that takes asks a user to input a string and outputs every second letter in reverse order
#Author: Denis Sarf

#requesting input as a string and at the same time assigning variables "string". 
string = input("Please enter a string:")

#taking every second letter from input "string" 
# and assigning variables "str_second_letter".
str_second_letter = string[1::2]

#output "str_second_letter" and at the same time to make 
# a reverse order ([::-1] - output begins with the last letters) 
print(str_second_letter[::-1])
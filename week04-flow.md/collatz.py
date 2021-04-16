#This program that asks the user to input any positive integer 
# and outputs the successive values of the following calculation

#Author: Denis Sarf

#requesting inputs as an integer number and assigning variable "number".
number = int(input("Please enter a positive integer: "))

#checking that if the number is greater than 0 then continue to calculate. 
# If the number is less or equal than 0 then 'while' loop prints "Wrong!!" 
# and requesting to input again the positive number
while number <= 0:
    print("Wrong!!!")
    number = int(input("Please enter again a positive integer: "))

# creating an empty list where we will put all answers
numbers = []

#the 'while' loop takes the current value "number" and, 
# if it is even, divides it by two, but if it is odd, 
# multiply it by three and add one. the statement will run until it equals 1.
# All the answers will append to the empty list "numbers", and the last step is to print all those numbers 
while number != 1:
    if (number % 2) == 0:
        number = number / 2
    else:
        number = (number * 3) + 1
    numbers.append(int(number))
print(numbers)

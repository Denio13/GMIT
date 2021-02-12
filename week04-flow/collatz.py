# This program that asks the user to input any positive integer 
# and outputs the successive values of the following calculation

#Author: Denis Sarf


number = int(input("Please enter a positive integer: "))

#check that the number is greater than 0
while number <= 0:
    print("Wrong!!!")
    number = int(input("Please enter again a positive integer: "))

numbers = []
numbers.append(int(number))

#the statement will run until it equals 1
while number != 1:
    if (number % 2) == 0:
        number = number / 2
        numbers.append(int(number))
    else:
        number = (number * 3) + 1
        numbers.append(int(number))
print(numbers)

#This function expects the input numbers as an argument and returns the estimate of its square root.
#Newton's method for approximating square roots


#Author: Denis Sarf

# import math module, the math module is a standard module 
# for using mathematical functions under this module
import math

#the function to return the square root of 
# a number using Newton's method
tolerance = 0.01
def sqrt(num):
    estimate = 1.0
    while True:
        estimate = (estimate + num / estimate) / 2
        difference = abs(num - estimate ** 2)
        if difference <= tolerance:
            return estimate

#the function requires input (a positive floating-point number) and assigning the variable "num" to it,
#  then if the "num" is empty or float number is less than 0, then the function will require to input again a float number.
# after that "num" is changed to a float "num", in "result" variable runs the function "math.sqrt(num)" with rounding to one number.
# the last step is printing the result "result"
def main():
    while True:
        num = input("Enter a positive floating-point number: ") #input a number

        if num == "" or float(num) < 0: # checking if the input is empty or a negative number was entered
           num = input("Something is wrong!!! Enter a positive floating-point number: ") #input a number
        num = float(num)
        result = round(math.sqrt(num), 1)
        #output using math module
        print("The square root of 14.5 is approx. ", result)

#this module runs as the main program.
if __name__ == "__main__": 
    main()

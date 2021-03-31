#This function expects the input numbers as an argument and returns the estimate of its square root.
#Newton's method for approximating square roots


#Author: Denis Sarf

import math


tolerance = 0.01
def sqrt(num):#Newton's method
   estimate = 1.0
   while True:
        estimate = (estimate + num / estimate) / 2
        difference = abs(num - estimate ** 2)
        if difference <= tolerance:
            return estimate


def main():

   while True:

       num = input("Enter a positive floating-point number: ") #input a number

       if num == "" or float(num) < 0: # checking if the input is empty or a negative number was entered
           num = input("Something is wrong!!! Enter a positive floating-point number: ") #input a number
       num = float(num)
       result_1 = round(math.sqrt(num), 1)
       print("Newton's method estimate is", result_1) #output Newton's method
       print("The program's estimate is", round(sqrt(num), 1)) #output using math module


if __name__ == "__main__": #this module runs as the main program.
    main()

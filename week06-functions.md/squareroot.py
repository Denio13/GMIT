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
            break
   return estimate


def main():
   while True:
       num = input("Enter a positive number or enter/return to quit: ") #input a number
       if num == "": 
           break
       num = float(num)
       result_1 = round(math.sqrt(num), 1)
       print("Newton's method estimate is", result_1) #output Newton's method
       print("The program's estimate is", round(sqrt(num), 1)) #output using math module


if __name__ == "__main__": #this module runs as the main program.
    main()

# The program takes in a float amount of dollars, and returns that absolute amount in cent
# Author: Denis Sarf

amount = float(input("Enter a number:"))
amount_cent = round(abs(amount) * 100)

print(f'The absolute value of {amount} is {amount_cent}')
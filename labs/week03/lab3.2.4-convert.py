# The program takes in a float amount of dollars, and returns that absolute amount in cent
# Author: Denis Sarf

amount = float(input("Please enter am amount:"))
amount_cent = round(abs(amount) * 100)

print(f'That amount in cent is: {amount_cent}')
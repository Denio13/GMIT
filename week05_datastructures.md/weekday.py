#The program prints today is a weekday or not. 

#Author: Denis Sarf

from datetime import datetime
#import date and time modules 

today = datetime.today().strftime('%A')
weekends = ("Saturday", "Sunday")

if today in weekends: #check "today" is in the "weekend"
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")



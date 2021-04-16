#The program prints today is a weekday or not. 

#Author: Denis Sarf


#import datetime module that supplies classes for manipulating dates and times.
from datetime import datetime 

#checking the current day and assigning the variable "today" to it
today = datetime.today().strftime('%A')

#creating a variable "weekend" with values "Saturday", "Sunday"
weekends = ("Saturday", "Sunday")

#'if' statement checks if "today"(current day) is in the "weekend" values, 
# then print "It is the weekend, yay!" and if not then print 
# "Yes, unfortunately, today is a weekday."
if today in weekends:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately, today is a weekday.")

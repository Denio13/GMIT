#This  a program that calculates  somebody's Body Mass Index (BMI)
#Author: Denis Sarf

#requesting inputs as an integer number and 
# at the same time assigning variables "weigh" and "height".
weigh = int(input("Enter your weigh:"))
height = int(input("Enter your height:"))

#conversion centimeter [cm] to meter [m] 
# with variable assignment "height_meter"
height_meter = height / 100  

#Body Mass Index is a simple calculation using a person's height and weight. 
# The formula is BMI = kg/m2 where kg is a person's weight in kilograms 
# and m2 is their height in meters squared. And rounding "round()"to two numbers
BMI = round(weigh / (height_meter ** 2), 2)    

#Print the result of the calculated BMI whit using printf format.
print(f'BMI is {BMI}.')                        

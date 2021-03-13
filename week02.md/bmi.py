#This  a program that calculates  somebody's Body Mass Index (BMI)
#Author: Denis Sarf

#Inputs for weigh and height
weigh = int(input("Enter your weigh:"))
height = int(input("Enter your height:"))

#  convert centimeter [cm] to meter [m]
height_meter = height / 100  

# The formula is BMI and calculation of BMI
BMI = round(weigh / (height_meter ** 2), 2)    

# BMI output
print(f'BMI is {BMI}.')                        

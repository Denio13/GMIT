# This program reads in a string and strips
# any leading or trailing spaces.
# It also converts all the letters to lower case
# this program also outputs the lenght of the original string
# and the normalised one
#Author: Denis Sarf


rawString = input("please enter a string:")
normalisedString = rawString.strip().lower()
lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normalisedString)

print(f"That String normalised is :{normalisedString}")
print(f"we reduced the input string from {lenghtOfRawString} to {lenghtOfNormalised} characters")
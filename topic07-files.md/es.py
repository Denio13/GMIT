# The program that reads a text file and prints the number of selected letters it contains.
# Author: Denis Sarf


# import sys — System-specific parameters and functions
import sys

#argv[1] represents the first command-line argument
filename = sys.argv[1]

#variable defining the letter "e"
selected_letter = 'e'  

#creating a variable with 0 value for collecting the amount of all "e" letters 
total = 0

#the first step is opening the .txt file with read "r" mode
# the first 'for' loop splits the text to line of words,
# then the second 'for' loop runs along the lines of words 
# and splits them into word and at the same time if the statement 
# checks if the "e" letter is inside of the word
# if the letter "e" was found then the "total" variable increases by one
with open(filename, 'rt') as f:
    for line in f:   
        words = line.split() 
        for word in words:
            if selected_letter in word:
                total += 1

# print of the all counted letters "e"
print(f'The file contains a total of {total} letters "{selected_letter}"')
# print only number
print(total) 


# The program that reads a text file and prints the number of selected letters it contains.
# Author: Denis Sarf


# import sys — System-specific parameters and functions
import sys

#argv[1] represents the first command-line argument
filename = sys.argv[1]

selected_letter = 'e'  # variable defining the letter "e"

total = 0

with open(filename, 'rt') as f: #open the file and read
    for line in f:    # the loop splits from text to words 
        words = line.split() 
        for word in words:
            # checking if selected_letter in word
            if selected_letter in word:
                total += 1

print(f'The file contains a total of {total} letters "{selected_letter}"')
print(total) # print only number


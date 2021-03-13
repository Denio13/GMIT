# The program that reads a text file and prints the number of selected letters it contains.
#Author: Denis Sarf



filename = input("Enter file name: ")  #input of the file with which the program will work

#selected_letter = input("Enter letter to be searched:")  #additional function: entering a letter to be counted

selected_letter = 'e'  #variable defining the letter "e"

total = 0

with open(filename, 'rt') as f: #open the file and read
    for line in f:    #the loop splits from text to words 
        words = line.split() 
        for i in words:
            for letter in i: #the loop checks if the letter is a selected letter or letter "e"
                if (letter == selected_letter):
                    total += 1

print(f'The file contains a total of {total} letters "{selected_letter}"')
print(total) #print only number

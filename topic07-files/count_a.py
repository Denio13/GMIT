#Author: Denis Sarf


filename = "count.txt"

def read_number():
    with open(filename) as f:
        number = int(f.read())
        return number

# test it
num = read_number()
print (num)

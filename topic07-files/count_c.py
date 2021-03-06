#Author: Denis Sarf


filename = "count.txt"

def read_number():
    with open(filename) as f:
        number = int(f.read())
        return number

def write_number(number):
    with open(filename, "wt") as f:
        #write takes a string so we need to convert
        f.write(str(number))


# main
num = read_number()
num += 1
print ("we have run this program {} times".format(num))
write_number(num)
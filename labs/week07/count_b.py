#Author: Denis Sarf

filename = "count.txt"

def write_number(number):
    with open(filename, "wt") as f:
    # write takes a string so we need to convert
        f.write(str(number))
        print(f'The number:{number} was added to the file')


# test it
write_number(3)

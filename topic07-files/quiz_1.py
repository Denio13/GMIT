#Author: Denis Sarf

# the with statement will automatically close the file
# when it is finished with it
with open("test-a.txt") as f:
    data = f.read()
    print (data)

# this is the same as
# f = open ("test1.txt")
# data = f.read()
# print(data)
# f.close()

#Answer:  Error / there are no modes 'r' and so on


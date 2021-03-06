#Author: Denis Sarf

import json


filename = "testdict.json"
sample = dict(name='fred', age=31, grades=[1,34,55])

def write_dict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj, f)

#test the function
write_dict(sample)


def read_dict():
 # this will throw an error if the file does not exist
 # it should readly just return an empty dict
 # we can do this later
    with open(filename) as f:
        return json.load(f)


# test the function
somedict = read_dict()
print(somedict)
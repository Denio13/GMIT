
#Author: Denis Sarf

def display_modules(modules):
    print ("\tName \tGrade")
    for module in modules:
        print("\t{} \t{}".format(module["name"], module["grade"]))

def do_view(students):
    for current_student in students:
        print(current_student["name"])
        display_modules(current_student["modules"])
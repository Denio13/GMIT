#The function adds students

#Author: Denis Sarf

from read_modules import read_modules

def do_add(students):
    current_student = {}
    current_student["name"]=input("Enter name :")
    current_student["modules"]= read_modules()
    students.append(current_student)

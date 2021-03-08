#Author: Denis Sarf

from display_menu import display_menu
from do_add import do_add
from read_modules import read_modules
from do_view import do_view


#main program
students = []
choice = display_menu()
while(choice != 'q'):
    # we could do this with lamda functions
    # I am keeping this basic for the moment
    if choice == 'a':
        do_add(students)
    elif choice == 'v':
        do_view(students)
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice = display_menu() 
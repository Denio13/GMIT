#Author: Denis Sarf

def read_modules():
    modules = []
    module_name = input("\tEnter the first Module name (blank to quit) :").strip()

    while module_name != "":
        module = {}
        module["name"]= module_name
        # I am not doing error handling
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        # now read the next module name
        module_name = input("\tEnter next module name (blank to quit) :").strip()
    return modules

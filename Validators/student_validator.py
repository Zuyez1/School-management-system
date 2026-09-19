import json
from Respositories import student_respository
def check_name(name):
    split_name  = name.split(" ")
    if all(x.isalpha() for x in split_name):
        return name
    else:
        return False
def check_class(clas):
    if 0<clas<=10:
        return clas
    else:
        return False
def availabilty(newcl,oldcl,name):
    content = student_respository.load_students("students.json")
    if name in content[f"c{newcl}"] or name not in content[f"c{oldcl}"]:
        return False
    else:
     return True
if __name__ == "__main__":
    while True:
        user = input("enetr name")
        clas = int(input("Enetr class"))
        print (check_class(clas))
        print (check_name(user))
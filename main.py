# version 3
from Respositories import student_respository,teacher_respository
from Validators import student_validator , teacher_validator
import json
class StudentManagment:
    def __init__(self):
        self.greet()
        self.menu()

    def menu(self):
        while True:
         print ("STUDENT DASHBOARD")
         user = input(""" (1) ADD STUDENT\n(2) REMOVE STUDENT\n(3) SHOW ALL STUDENTS\n(4) Search student\n(5) Update student \n(6) Exit""")
         if user=="1":
            self.add_stu()
         elif user == "2":
            self.remove_stu()
         elif user == "3":
            self.show()
         elif user == "4":
            self.search_student()
         elif user == "5":
           self.student_update()
         elif user == "6":
            print ("Thank you for visiting student management system")
            break
         else:
            print ("pls enter valid credentials")
    def add_stu(self):
            while True:
                try:
                    user_name = input("Enter student name: ")
                    user_c = int (input ("PLS SELECT CLASS (1-10): "))
                    if student_validator.check_class(user_c) and student_validator.check_name(user_name):
                        break
                    else:
                        print ("Enetr a valid credentials")
                except ValueError:
                    print ("You have entered text instead of numbers.....")
            student_data = student_respository.load_students("students.json")
            if user_name in student_data[f"c{user_c}"]:
                print (f"student already in Class{user_c}")
            else:
                student_data[f"c{user_c}"].append(user_name)
                student_respository.save_students("students.json",student_data)
                print ("sutudent added....")

    def remove_stu(self):
            while True:
                 try:
                  user_name = input("Enter student name: ")
                  user_c = int (input ("PLS SELECT CLASS (1-10): "))
                  if student_validator.check_class(user_c) and student_validator.check_name(user_name):
                      break
                  else :
                      print ("Enetr a valid class")
                 except ValueError:
                    print ("You have entered text instead of numbers.....")
            content = student_respository.load_students("students.json")
            if user_name not in content[f"c{user_c}"]:
                print ("student doesnot exist in the class")
            else:    
             content[f"c{user_c}"].remove(user_name) 
             student_respository.save_students("students.json",content)
             print ("student removed")
    def show (self):
        student_data = student_respository.load_students("students.json")
        for cls , students in student_data.items():
            print (f"{cls.replace("c","Class ")}={students}")
    def search_student(self):
        while True:
            student_name = input("Enter student name to search : ") 
            if student_validator.check_name(student_name):
                break
            else:
                print ("Enter a valid name")
        student_data = student_respository.load_students("students.json")
        for clas in student_data:
            if student_name in student_data[clas]:
                print (f"{student_name} found in {clas.replace("c","Class ")}")
    def student_update(self):
        def move_name (): 
            content = student_respository.load_students("students.json")
            content[f"c{old_class}"].remove(name)
            content[f"c{new_class}"].append(name)
            student_respository.save_students("students.json",content)
            print ("student saved ...")
        while True:
            try:
             user_name  = input("enter name: ")
             user_name = user_name.strip()
             user_clas = int(input("Enetr your current class 1-10: ") )
             user_new_class = int(input("Enetr your new class 1-10: "))
             name = student_validator.check_name(user_name)
             old_class = student_validator.check_class(user_clas)
             new_class = student_validator.check_class(user_new_class)
             if name and old_class and new_class:
              break
             print ("invalid credentials")
            except ValueError:
             print ("enetr number in class")
        if student_validator.availabilty(new_class,old_class,name):
            move_name()
        else:
            print ("student connot transfered")
           
    def greet(self):
        print ("WELLCOME TO THE STUDENT MANAGEMENT SYSTEM")

class TeacherManagment:
    def __init__(self):
        self.greet()
        self.menu()
    def menu(self):
        while True:
            user = input("(1) ADD TEACHER\n(2) REMOVE TEACHER\n(3) SHOW ALL TEACHER\n")
            if user == ("1"):
                self.add_teacher()
            elif user == ("2"):
                self.rem_teacher()
            elif user == ("3"):
                self.show_teacher()
            else:
                print ("pls enter a valid input")
    def add_teacher(self):
        while True: 
                teach_name = input("Enter teacher name: ")
                teach_id = (input("Enter teacher id \n Example : TXXX \n: "))
                teach_address = input("Enter teacher address: ")
                final_subject = teacher_validator.get_subjects()
                num_class = teacher_validator.get_number_class()
                if teacher_validator.check_teacher_name(teach_name) and teacher_validator.check_id(teach_id,teacher_respository.load_teacher("teachers.json")) :
                    break
                else:
                    print ("Enter valid credentials")       
        content = teacher_respository.load_teacher("teachers.json")
        content[teach_id] = {"Name":teach_name,"Address":teach_address,"Subjects":final_subject,"Classes":num_class}
        teacher_respository.save_teacher("teachers.json",content)
        print ("DATA SAVED....")
    def rem_teacher(self):
        while True:
            data = teacher_respository.load_teacher("teachers.json")
            print ("list of teachers id")
            for id in data.keys():
                print (id)
            teacher_id = input("Enetr Teacher id \n like TXXX:")
            if (teacher_validator.check_id(teacher_id,data,True)):
                print(f"\nID = {teacher_id}\n ADDRESS = {data[teacher_id]['Address']}\n Subjects = {data[teacher_id]['Subjects']}\nClass = {data[teacher_id]['Classes']}")
                choice = input("Do you want to delete this teacher ? (y,n)")
                if "y" in choice.lower():
                    del data[teacher_id]
                    teacher_respository.save_teacher("teachers.json",data)
                    print ("\n Teacher data deleted.....")
                    return
            else:
                print ("\n Teacher does not exist")
                return
    def show_teacher(self):
        content = teacher_respository.load_teacher("teachers.json")
        if content:
            for id , data in content.items():
                print(f"ID = {id}\n Name = {data['Name']} \n Address = {data['Address']} \n Subjects = {data['Subjects']} \n Classes = {data['Classes']}\n")
    def greet(self):
        print ("WELLCOME TO THE Teacher MANAGEMENT SYSTEM")
while True :
    system_choice = input("""WELLCOME TO SCHOOL MANAGEMENT SYSTEM\n
    (1) STUDENT MANAGEMENT SYSTEM
    (2) TEACHER MANAGEMENT SYSTEM
    (3) EXIT 
    """)
    if system_choice=="1":
        StudentManagment()
    elif system_choice=="2":
        TeacherManagment()
    elif system_choice=="3":
        print ("Thank you for visiting....\nPROGRAME EXITED")
        pass
    else:
        print ("Enter a valid input ")
       
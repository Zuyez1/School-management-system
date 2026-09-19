# version 3
from Respositories import student_respository,teacher_respository
from Validators import student_validator
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
        user = input("""(1) ADD TEACHER\n
                        (2) REMOVE TEACHER\n
                        (3) SHOW ALL TEACHER\n
                        (4) SHEARCH TEACHER""")
        if user == ("1"):
            self.add_teacher()
        elif user == ("2"):
            self.rem_teacher()
        elif user == ("3"):
            self.show_teacher()
        elif user == ("4"):
            self.search_teacher()
        else:
            print ("pls enter a valid input")
    def add_teacher(self):
        clas_con = []
        teach_name = input("Enter teacher name: ")
        teach_id = input("Enter teacher id: ")
        teach_address = input("Enter teacher address: ")
        def suject_validator():
           sub_con = []
           try:
            teach_sub  = int(input("Enter number of subject: "))
            if teach_sub>8 or teach_sub<=0 :
               print ("enter a valid input")
               return suject_validator()
            else:
               for i in range (teach_sub):
                           final_sub = input("Enter subject name : ")
                           if final_sub in sub_con:
                               print("subject already existed")
                           else:
                               sub_con.append(final_sub)
           except:
              return suject_validator()
        #    for i in range (teach_sub):
        #     final_sub = input("Enter subject name : ")
        #     if final_sub in sub_con:
        #         print("subject already existed")
        #     else:
        #         sub_con.append(final_sub)
           return sub_con     
        sub_con= suject_validator()        
        def validate_num_class():
         try : 
          teach_cl   = int(input("How many classes: "))
          if teach_cl>10 or teach_cl<=0:
             print ("Enetr a valid input...")
             return validate_num_class()
          else:
           return teach_cl
         except:
            print ("Enetr a valid input")
            return validate_num_class()
        teach_cl = validate_num_class() 
        for i in range (teach_cl):
            def class_validation():   
              try:
                final_cls = int(input(" which class (1-10): "))
                if final_cls>10 or final_cls<=0:
                   print ("Enter a valid input")
                   return class_validation()
                else:
                 final_cls = "Class "+str(final_cls)
                 return (final_cls)
              except:
                print("Enter a valid input")
                return class_validation()
            final_cls = class_validation()
            
            if final_cls in clas_con:
                print("Class already added")
                
            else:
                clas_con.append(final_cls)
        with open("teachers.json","r") as f :
            content=json.load(f)
        content.update({teach_name:{"id":teach_id,
                                         "Address":teach_address,
                                         "Class":clas_con,
                                         "Subject":sub_con}})   
        with open("teachers.json","w") as f :
            json.dump(content,f,indent=4) 
            print ("Data saved .....")
        choice = input("Do you want to have menu ? (y,n): ")
        if "y" in choice.lower():
         self.menu()  
        else:
            pass
    def rem_teacher(self):
        t_con=[]
        with open("teachers.json","r") as f:
            content = json.load(f)
        print ("list of teacher:")
        for teacher in content:
            t_con.append(teacher)
            print(teacher)
        def teacher_name_validation():
         t_name= input("Enter teacher name: ")
         if t_name not in t_con:
            print (f"there is no teacher named: {t_name}")
            return teacher_name_validation()
         else:
            del content[t_name]
            return (content)
        content = teacher_name_validation()
        with open("teachers.json","w") as f :
                json.dump(content,f)
        print ("Data saved")
        self.menu() 
    def show_teacher(self):
        with open("teachers.json","r") as f :
            content = json.load(f)
        for techers in content:
            print(f"Teacher name : {techers}\n Subjects {techers} teach : {content[techers]["Subject"]}")
        choice = input("Do you want to have menu ? (y,n): ")
        if "y" in choice.lower():
            self.menu()  
        else:
            pass
    def search_teacher(self):
        teach_n = input("Enter teacher name : ")

        with open ("teachers.json","r") as f :
            content = json.load(f)
        for teacher in content:
            if teach_n.lower() == teacher.lower():
                print (f"Teacher found:\nName: {teacher}\n{content[teacher]}")
                break
                
        else :
            print ("Teacher not found")
            self.menu()
    def greet(self):
        print ("WELLCOME TO THE Teacher MANAGEMENT SYSTEM")

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
       
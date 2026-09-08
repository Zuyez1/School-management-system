# version 3
import json
class StudentManagment:
    def __init__(self):
        self.greet()
        self.menu()

    def menu(self):
        user = input(""" (1) ADD STUDENT\n(2) REMOVE STUDENT\n(3) SHOW ALL STUDENTS\n(4) Search student\n(5) Update student""")
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
        else:
            print ("pls enter valid credentials")
            self.menu()
    def add_stu(self):
            def saviour():
             try:
              user_c = int (input ("PLS SELECT CLASS (1-10): "))
              user_num_stu = int(input("NUMBER OF STUDENT: "))
             except:
                print ("You have entered text instead of numbers.....")
                return saviour()
             if (user_c>10 or user_c<=0) or (user_num_stu>10 or user_num_stu<=0):
              print ("invalid input.....") 
              return saviour()
             else:
              return user_num_stu,user_c
            user_num_stu,user_c=saviour()
         
            for i in range(user_num_stu):
             user_name=input ("ENTER STUDENT NAME: ")
             with open ("students.json","r") as f:
              content = json.load(f)
              content[f"c{user_c}"].append(user_name) 
             with open ("students.json","w") as f:   
              json.dump(content,f,indent=4)
            self.menu()
    def remove_stu(self):
            def saviour():
                 try:
                  user_c = int (input ("PLS SELECT CLASS (1-10): "))
                 except:
                    print ("You have entered text instead of numbers.....")
                    print("this is running")
                    return saviour()
                 if user_c<=10 and user_c>0:
                  return user_c
                 else:
                  print ("Enetr a valid number")
                  return saviour() 
            user_c = saviour()
            def name_validation():
                user_name = input("Enter student name: ")
                lis = []
                with open("students.json","r") as f :
                    content = json.load(f)
                for name in content[f"c{user_c}"]:
                    lis.append(name)
                if user_name not in lis:
                    print ("student not found")
                    return name_validation()
                else:
                    return user_name        
            user_name = name_validation()
            with open ("students.json","r") as f:
              content = json.load(f)
              content[f"c{user_c}"].remove(user_name) 
            with open ("students.json","w") as f:   
              json.dump(content,f,indent=4)
              print ("DATA saved..")

            self.menu()
    def show (self):
        with open("students.json","r") as f:
            content=json.load(f)
            c_no=1
            for cclass in content:
                print(f"CLASS {c_no} = {content[cclass]}")
                c_no+=1
        self.menu()        
    def search_student(self):
        def name_validator():
            user_name  = input("enter name: ")
            name = user_name.split(" ")
            fname = []
            if len(name) > 1:
                for names in name:
                    if names.isalpha():
                        fname.append( names)
                return (" ".join(fname))           
            else:
                return (user_name)   
        student_name = name_validator()
        with open ("students.json","r") as f:
           content = json.load(f)
        cl = 1
        lis = []
        for clas in content:
            if student_name in  content[clas]:
              a = (f"Student found in Class {cl}")
              lis.append(a)
              cl+=1
            else:
               cl+=1
        else:
           pass   
        if lis == [] :
           print ("not found")
        else:
           for info in lis:
              print (info)   
        self.menu()   
    def student_update(self):
        def name_validator():
            user_name  = input("enter name: ")
            name = user_name.split(" ")
            fname = []
            if len(name) > 1:
                for names in name:
                    if names.isalpha():
                        fname.append( names)
                    else:
                       print ("your name contain numbers which our program doesnot accept pls try again")
                       return name_validator
                return (" ".join(fname))           
            else:
                return (user_name)   
        def cl_validation(name):
            try:
             clas_s = int(input("Enetr class: "))
            except:
               print ("enetr a valid input")
               return cl_validation(name)
            if (clas_s) in lis:
                    try:
                     choice = int(input("(1) Change name\n(2) Move to other class"))
                    except:
                       print ("Enter a valid choice")
                       return cl_validation(name)
                    if choice == 1 :
                     first_name = input("Enetr first name: ")
                     second_name = input("Enetr second name: ")
                     if first_name.isalpha() and second_name.isalpha():
                        final_name = first_name+" "+second_name
                        with open("students.json","r") as f :
                           content= json.load(f)
                        index = content[f"c{clas_s}"].index(name)  
                        content[f"c{clas_s}"][index]=final_name
                        with open ("students.json","w") as f :
                           json.dump(content,f,indent=4)
                        print ("Name changed successfully....")   
                     else:
                        print ("invalid input")
                        return cl_validation(name)
                    elif choice==2:
                     try: 
                      choccie = int(input("Enter class to move a student: "))
                     except ValueError:
                        print ("pls ennetr numbers (1-10)")
                        return cl_validation(name)
                     if choccie==clas_s:
                        print("Student is already in class")
                        return cl_validation(name)
                     elif choccie>10 or choccie<=0:
                        print ("Classes we have are from 1-10 pls enter in this range")
                        return cl_validation(name)
                     else:
                        with open("students.json","r") as f :
                           content = json.load(f)
                        content[f"c{clas_s}"].remove(name)
                        content[f"c{choccie}"].append(name)
                        with open("students.json","w") as f :
                           json.dump(content,f,indent=4)  
                        print ("student moved to new class.....")    
                    else:
                        print ("invalid input")
                        return cl_validation(name)                        
            else:
                print("class not matched")
                return self.menu()      
        student_name = name_validator()
        with open ("students.json","r") as f:
           content = json.load(f)
        cl = 1
        lis = []
        for clas in content:
            if student_name in  content[clas]:
              a = (f"Student found in Class {cl}")
              print (a)
              lis.append(cl)
              cl+=1
            else:
               cl+=1
        else:
           pass   
        if lis == [] :
           print ("Student not found")
           self.menu()
        else:
           cl_validation(student_name)            
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
       
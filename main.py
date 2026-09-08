import json
students = {"c1":[],
            "c2":[],
            "c3":[],
            "c4":[],
            "c5":[],
            "c6":[],
            "c7":[],
            "c8":[],
            "c9":[],
            "c10":[],}


class StudentManagment:
    def __init__(self):
        self.greet()
        self.menu()

    def menu(self):
        user = input(""" (1) ADD STUDENT\n(2) REMOVE STUDENT\n(3) SHOW ALL STUDENTS""")
        if user=="1":
            self.add_stu()
        elif user == "2":
            self.remove_stu()
        elif user == "3":
            self.show()
        else:
            print ("pls enter valid credentials")
            self.menu()
    def add_stu(self):
        user_c = int (input ("PLS SELECT CLASS (1-10): "))
        user_num_stu = int(input("NUMBER OF STUDENT: "))
        for i in range(user_num_stu):
            user_name=input ("ENTER STUDENT NAME: ")
            with open ("students.json","r") as f:
              content = json.load(f)
              content[f"c{user_c}"].append(user_name) 
            with open ("students.json","w") as f:   
             json.dump(content,f,indent=4)
        user = input("do you want to add or remove more students:")
        if "y" in user.lower():
          self.menu()  
        else:
            pass
    def remove_stu(self):
        user_c = int (input ("PLS SELECT CLASS (1-10): "))
        with open ("students.json","r") as f:
            content = json.load(f)
        print(content[f"c{user_c}"])    
        user_num_stu = int(input("NUMBER OF STUDENT: "))
        for i in range(user_num_stu):
         user_name=input ("ENTER STUDENT NAME: ")
         with open ("students.json","r") as f:
                      content = json.load(f)
                      content[f"c{user_c}"].remove(user_name) 
         with open ("students.json","w") as f:   
                     json.dump(content,f,indent=4)
        user = input("do you want to add or remmove more students:")
        if "y" in user.lower():
         self.menu()  
        else:
         pass
    def show (self):
        with open("students.json","r") as f:
            content=json.load(f)
            c_no=1
            for cclass in content:
                print(f"CLASS {c_no} = {content[cclass]}")
                c_no+=1
        self.menu()        
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
        sub_con = []
        clas_con = []
        teach_name = input("Enter teacher name: ")
        teach_id = input("Enter teacher id: ")
        teach_address = input("Enter teacher address: ")
        teach_sub  = int(input("Enter number of subject: "))
        for i in range (teach_sub):
            final_sub = input("Enter subject name : ")
            if final_sub in sub_con:
                print("subject already existed")
            else:
                sub_con.append(final_sub)
        teach_cl   = int(input("How many classes: "))
        for i in range (teach_cl):
            final_cls = input(" which class (1-10): ")
            final_cls = "Class "+final_cls
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
        t_name= input("Enter teacher name: ")
        if t_name not in t_con:
            print (f"there is no teacher named: {t_name}")
            self.rem_teacher()    
        else:
            del content[t_name]
            print(content)
            with open("teachers.json","w") as f :
                json.dump(content,f)
        choice = input("Do you want to have menu ? (y,n): ")
        if "y" in choice.lower():
            self.menu()  
        else:
            pass    
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
            if teach_n.lower() == teacher:
                print (f"Teacher found:\nName: {teacher}\n{content[teacher]}")
                break
        else :
            print ("Teacher not found")
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
    pass
else:
    print ("Enter a valid input ")
       
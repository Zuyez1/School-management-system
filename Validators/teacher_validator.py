
File_name = "teachers.json"
def check_teacher_name(name:str):
    split_name = name.split(" ")
    if all(names.isalpha() for names in split_name):
        return True
    else:
        return False
def check_id (id:str,data:dict, availability = False):
    if id[0]=="T":

        if id in data:
            return availability
        return True
    return False         
def get_subjects():
    subjects_dict = {
        1: "English",
        2: "Urdu",
        3: "Islamiyat",
        4: "Mathematics",
        5: "SST",
        6: "Character Building",
        7: "Sports",
        8: "Computer Science",
        9: "Science",
        10: "Art"
    }
    number = get_positive_number("Enetr number of subjects","Number of shubjects should contain numbers in the range of (1-10)")
    for key , subjects in subjects_dict.items():
        print (f"{key}. {subjects}")
    used_number = set()
    while number>len(used_number):
            subject_number = get_positive_number(f"Enter subject {len(used_number)+1}/{number} number : ","Subject number must contain number in the range of (1-10)")
            if subject_number  in used_number:
                print ("subject already selected...")
                continue
            used_number.add(subject_number)
    subjects_lis = [subjects_dict[i] for i in sorted(used_number)]    
    return subjects_lis 
def get_positive_number(message,error_message,minimun=1,maximum=10):
    while True:
        try:
            number = int(input(message))
            if number>=minimun and number<=maximum:
                return number
            print (error_message)
        except ValueError:
            print (error_message)
def get_number_class():
        used_number = set()
        number = get_positive_number("Enter number of clases: ","Number of classes must contain numbers in the range of (1-10)")
        while number>len(used_number):
            class_number = get_positive_number(f"Enter class {len(used_number)+1}/{number} number : ","Class number must contain number in the range of (1-10)")
            if class_number  in used_number:
                print ("class already selected...")
                continue
            used_number.add(class_number)
        classes = [f"Class {i}" for i in sorted(used_number)]    
        return classes  
if __name__ == "__main__":
    print (get_number_class())
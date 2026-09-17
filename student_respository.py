import json
def load_students(file):
    try: 
     with open (file,"r") as f :
        content =  json.load(f)
        return content
    except FileNotFoundError :
       return {
                "c1": [],
                "c2": [],
                "c3": [],
                "c4": [],
                "c5": [],
                "c6": [],
                "c7": [],
                "c8": [],
                "c9": [],
                "c10": []
                }
def save_students(file,content):
   with open (file,"w") as f :
    json.dump(content,f,indent=4)
    print("data saved...")
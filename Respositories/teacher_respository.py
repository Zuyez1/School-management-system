import json
def load_teacher(file):
    try: 
     with open (file,"r") as f :
       return json.load(f)
    except FileNotFoundError :
       return {}
def save_teacher(file,content):
   with open (file,"w") as f :
    json.dump(content,f,indent=4)
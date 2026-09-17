import json
def load_data (file):
    try:
        with open (file,"r") as f :
            content = json.load(f)
            return content
    except json.JSONDecodeError:
        with open (file,"w") as f :
            json.dump([],f)
            load_data()
def save_data (file,data):
    try:
        with open (file,"w") as f :
            json.dump(data,f)
            return ("Data saved.....")
    except json.JSONDecodeError:
            return ("error")
def log_in ():
    limit = 0
    content = load_data("exp_data.json")
    login = False
    while not login and  limit<3 :
        name = input("Enter name: ")
        pass_w = input("Enter password: ")
        for data in content:
            if name in data.get("name") and pass_w in data.get("password"):
                print ("sucess fully loged in")
                login = True
                break
        else:
            print ("Invalid credentials\nTRY AGAIN..") 
            limit+=1
    if limit == 3 :
        choice = input("DO you want to sign up ?")
        if "y" in choice.lower():
            sign_up()
        else:
            print ("thank you for vsiting ...")


def sign_up ():
    name = input("Enter name: ")
    pass_w = input("Enter password: ")
    content = load_data("exp_data.json")
    content.append({"name" : name,
                    "password" : pass_w})
    print(save_data("exp_data.json",content))
log_in()
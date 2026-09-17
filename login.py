import json
def log_in():
    name = input("Enetr name: ")
    pass_w = input("Enetr password: ")
    with open("user_credentials.json","r") as f:
        content = json.load(f)
    content.update({name:{"name":name,"password":pass_w}})
    with open("user_credentials.json","w") as f:
        json.dump(content,f,indent=4)
    print ("data saved.......")    
def sign_up():
    name = input("Enetr name: ")
    pass_w = input("Enetr password: ")
    with open("user_credentials.json","r") as f:
        content = json.load(f)
    if content.get(name):
        if content.get(name)["password"] == pass_w:
             print("log in sucess")   
        else:
             print ("wrong password")
    else:
         print ("no name existed")               
def forgot_password():
    pass
choice = {
    "log in" : log_in,
    "sign up" : sign_up,
    "forgot password": forgot_password
}

user = int(input("(1) log in\n(2) sign up"))
if user == 1:
         interface = choice.get("log in")
         interface()
elif user == 2 :
    interface = choice.get("sign up")
    interface()
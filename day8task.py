# Prepare a simple login and register system using File and function of usernames and passwords

import json

def register():
    username = input("Enter your username: ")
    file = open("credentials.txt", "r")
    content = file.read()
    file.close()

    list_credentials = content.split("-")
    for i in list_credentials:
        if i != "":
            dict_credential = json.loads(i)  
            if username in dict_credential:
                print("Username already exists. Please choose a different username.\n")
                break
    else:
        password = input("Enter your password: ")
        dict_credential = {username: password} 
        json_credential = json.dumps(dict_credential) 
        file = open("credentials.txt", "a")
        file.write(json_credential + "-")
        file.close()
        print("Registration Successful \n")
    
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    file = open("credentials.txt", "r")
    content = file.read()
    file.close()
    
    list_credentials = content.split("-")
    for i in list_credentials:
        if i != "":
            dict_credential = json.loads(i)
            if username in dict_credential and dict_credential[username] == password:
                print("Login Successful \n")
                break
    else:
        print("Login failed\n")

while True:
    choice = int(input("Enter 1 for register, 2 for login, 3 for exit: "))
    match choice:
        case 1 :
            register()
        case 2:
            login()
        case 3:
            break
        case _:
            print("Invalid Input. Please try again")

# log in , register system with exception handling

# Prepare a simple login and register system using File and function of usernames and passwords

import json

def register():
    try:
        username = input("Enter your username: ")  # Enter username
        file = open("day9.txt", "r")  
        content = file.read()  
        file.close()

        list_credentials = content.split("-")
        for i in list_credentials:
            if i != "":
                dict_credential = json.loads(i)
                if username in dict_credential:
                    print("Username already exists. Please choose a different username.\n")  # Username exists
                    return

        password = input("Enter your password: ")  # Enter password
        dict_credential = {username: password}
        json_credential = json.dumps(dict_credential)
        file = open("day9.txt", "a")
        file.write(json_credential + "-")
        file.close()
        print("Registration Successful \n")  # Success

    except Exception as e:
        print("An error occurred during registration:", e)  # Error occurred

def login():
    try:
        username = input("Enter your username: ")  # Enter username
        password = input("Enter your password: ")  # Enter password
        file = open("day9.txt", "r")
        content = file.read()
        file.close()

        list_credentials = content.split("-")
        for i in list_credentials:
            if i != "":
                dict_credential = json.loads(i)
                if username in dict_credential and dict_credential[username] == password:
                    print("Login Successful\n")  # Success
                    return
        print("Login Failed\n")  # Failed

    except Exception as e:
        print("An error occurred during login:", e)  # Error occurred

while True:
    try:
        choice = int(input("Enter 1 for register, 2 for login, 3 for exit: "))  # Menu choice
        if choice == 1:
            register()
        elif choice == 2:
            login()
        elif choice == 3:
            print("Exiting program. Goodbye!")  # Exit
            break
        else:
            print("Invalid Input. Please try again\n")  # Invalid choice
    except Exception as e:
        print("An error occurred:", e)  # Error in menu input

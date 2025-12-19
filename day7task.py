# Prepare a simple login and register system using File and function only of usernames

def register():
    username = input("Enter your username: ")
    file = open("user.txt", "a")
    file.write(username + "-")
    file.close()


def login():
    username = input("Enter your username: ")
    file = open("user.txt", "r")
    content = file.read()
    file.close()

    list_content = content.split("-")

    if username in list_content:
        print("Login Successful")
    else:
        print("Login Failed")
        
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
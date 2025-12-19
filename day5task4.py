# Make a login system using registration using function

users = {
    "ram": "1234",
    "sita": "5678",
    "hari": "9999"
}

def register():
    user = input("Create username: ")
    psw = input("Create password: ")

    if user in users:
        print("Username already exists!\n")
    else:
        users[user] = psw
        print("Registration Successful!\n")

def login():
    user = input("Enter username: ")
    psw = input("Enter password: ")

    if user in users and users[user] == psw:
        print("Login Successful!\n")
    else:
        print("Login Failed!\n")


while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose 1, 2, or 3: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!\n")

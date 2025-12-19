# Prepare a login and register system using File and function of usernames password, balance and user should
# be able to check, deposit and withdraw money from his account

import json

# REGISTER FUNCTION
def register():
    username = input("Enter your username: ")

    file = open("day8.txt", "r")
    content = file.read()
    file.close()

    list_credentials = content.split("-")

    # Check if username exists
    for i in list_credentials:
        if i != "":
            dict_credential = json.loads(i)
            if username in dict_credential:
                print("Username already exists. Please choose a different username.\n")
                return

    # Register new user
    password = input("Enter your password: ")
    balance = 0  # default balance for new user

    dict_credential = {username: {"password": password, "balance": balance}}
    json_credential = json.dumps(dict_credential)

    file = open("day8.txt", "a")
    file.write(json_credential + "-")
    file.close()

    print("Registration Successful!\n")


# LOGIN FUNCTION
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    file = open("day8.txt", "r")
    content = file.read()
    file.close()

    list_credentials = content.split("-")

    for i in list_credentials:
        if i != "":
            dict_credential = json.loads(i)
            if username in dict_credential:
                if dict_credential[username]["password"] == password:
                    print("Login Successful!\n")
                    account_menu(username, dict_credential[username])  
                    return

    print("Login Failed!\n")


# ACCOUNT MENU FUNCTION
def account_menu(username, user_data):

    while True:
        print("----- ACCOUNT MENU -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Logout")

        choice = int(input("Enter choice: "))

        # CHECK BALANCE
        if choice == 1:
            print("Your balance is:", user_data["balance"], "\n")

        # DEPOSIT
        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            user_data["balance"] += amount
            print("Deposit successful!\n")
            update_user(username, user_data)

        # WITHDRAW
        elif choice == 3:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= user_data["balance"]:
                user_data["balance"] -= amount
                print("Withdrawal successful!\n")
                update_user(username, user_data)
            else:
                print("Not enough balance!\n")

        # LOGOUT
        elif choice == 4:
            print("Logging out...\n")
            break

        else:
            print("Invalid choice!\n")


# UPDATE USER DATA IN FILE
def update_user(username, updated_data):

    file = open("day8.txt", "r")
    content = file.read()
    file.close()

    list_credentials = content.split("-")
    new_content = ""

    for i in list_credentials:
        if i != "":
            dict_credential = json.loads(i)

            if username in dict_credential:
                # replace old data with updated data
                dict_credential[username] = updated_data

            new_content += json.dumps(dict_credential) + "-"

    file = open("day8.txt", "w")
    file.write(new_content)
    file.close()


# MAIN MENU
while True:
    choice = int(input("Enter 1 for Register, 2 for Login, 3 for Exit: "))

    match choice:
        case 1:
            register()
        case 2:
            login()
        case 3:
            break
        case _:
            print("Invalid Input! Try again.\n")

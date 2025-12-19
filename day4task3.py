## Update the login dictationary program using while loop

dict1 = {
    "Ram": "ram123",
    "Sita": "sita123",
    "Hari": "hari123"
}

while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in dict1:
        if password == dict1[username]:
            print("Login successful!")
            break
        else:
            print("Wrong password!")
    else:
        print("Username not found!")
# Update the login dictationary program using loop

dict1 = {
    "Ram": "ram123",
    "Sita": "sita123",
    "Hari": "hari123"
}

username = input("Enter username: ")
password = input("Enter password: ")

for user in dict1:
    if username == user:
        if password == dict1[user]:
            print("Login successful!")
        else:
            print("Wrong password!")
        break
else:
    print("Username not found!")

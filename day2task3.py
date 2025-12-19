# 5) Update the login dictationary program using IF ELSE

dict1 = {
    "Ram": "ram123",
    "Sita": "sita123",
    "Hari": "hari123"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in dict1:
    if dict1[username] == password:
        print("Login successful!")
    else:
        print("Wrong password!")
else:
    print("Username not found!")
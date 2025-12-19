# Make a simple login system without registration using functions

users = {
    "ram": "1234",
    "sita": "5678",
    "hari": "9999"
}

def login(user, psw):
    if user in users:         
        if users[user] == psw: 
            print("Login Successful!")
        else:
            print("Wrong Password!")
    else:
        print("User not found!")

username = input("Enter username: ")
password = input("Enter password: ")

login(username, password)





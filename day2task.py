# 1) Create a list of usernames, Input a username from the user, Check if the username is present in the list or not

usernames = ["Ram","Sita", "Hari"]
user = input("Enter a username: ")
if user in usernames:
    print("Username is present")
else:
    print("Username is not present")
    
# 2) Create a dictionary of usernames and passwords, extract all the usernames from the dictionary and 	input username from the user and 
# check if the username is present in the extracted list of usernames

dict1 = {
    "Ram": "ram123",
    "Sita": "sita123",
    "Hari": "hari123"
}

usernames =list(dict1.keys())

user = input("Enter a username: ")
if user in usernames:
    print("Username is present")
else:
    print("Username is not present")




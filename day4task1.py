# Make a accounting system where a user logins and he should be able to check the balance, add balance and withdraw balance. Use dictionary, IF…ELSE and loop if needed.

# User database 
users = {
    "Ram": {"password": "ram123", "balance": 1000},
    "Sita": {"password": "sita123", "balance": 1500},
    "Hari": {"password": "hari123", "balance": 800}
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users:
    if users[username]["password"] == password:
        print("Login successful!\n")

        while True:
            print("----- ACCOUNT MENU -----")
            print("1. Check Balance")
            print("2. Add Balance")
            print("3. Withdraw Balance")
            print("4. Exit")

            choice = int(input("Enter choice (1-4): "))

            # CHECK BALANCE
            if choice == 1:
                print("Your balance is:", users[username]["balance"])

            # ADD BALANCE
            elif choice == 2:
                amount = int(input("Enter amount to add: "))
                users[username]["balance"] += amount
                print("Balance added successfully!")
                print("New Balance:", users[username]["balance"])

            # WITHDRAW BALANCE
            elif choice == 3:
                amount = int(input("Enter amount to withdraw: "))
                if amount <= users[username]["balance"]:
                    users[username]["balance"] -= amount
                    print("Withdrawal successful!")
                    print("Remaining Balance:", users[username]["balance"])
                else:
                    print("Not enough balance!")

            # EXIT
            elif choice == 4:
                print("Thank you! Logging out.")
                break

            else:
                print("Invalid choice! Please choose again.")

    else:
        print("Incorrect password!")
else:
    print("Username not found!")

#calculator program using while loop

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = int(input("Choose a number (1-6): "))

    if choice == 1:
        print("Addition:", a + b)
    elif choice == 2:
        print("Subtraction:", a - b)
    elif choice == 3:
        print("Multiplication:", a * b)
    elif choice == 4:
        print("Division:", a / b)
    elif choice == 5:
        print("Modulus:", a % b)
    elif choice == 6:
        print("Exiting calculator...")
        break
    else:
        print("Invalid choice! Try again.")

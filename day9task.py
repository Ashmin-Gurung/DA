# calculator program with exception hadling

# Calculator with Exception Handling

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
except Exception as e:
    print("Invalid input! Please enter a number.")
    exit()  # Stop program if input is invalid

while True:
    try:
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exit")

        choice = int(input("Choose a number (1-6): "))

        if choice == 1:
            print("Addition:", add(a, b))
        elif choice == 2:
            print("Subtraction:", sub(a, b))
        elif choice == 3:
            print("Multiplication:", mul(a, b))
        elif choice == 4:
            try:
                print("Division:", div(a, b))
            except Exception as e:
                print("Error:", e)  # Handles division by zero
        elif choice == 5:
            try:
                print("Modulus:", mod(a, b))
            except Exception as e:
                print("Error:", e)  # Handles modulus by zero
        elif choice == 6:
            print("Exit")
            break
        else:
            print("Invalid choice! Try again.")
    except Exception as e:
        print("Invalid input! Please enter a number.")
    finally:
        print("Operation complete.\n")

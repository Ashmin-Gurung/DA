# Update the Calculator program using match

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

choice = int(input("Choose a number from 1-5: "))

match choice:
    case 1:
        print("Addition:", a + b)
    case 2:
        print("Subtraction:", a - b)
    case 3:
        print("Multiplication:", a * b)
    case 4:
        print("Division:", a / b)
    case 5:
        print("Modulus:", a % b)
    case _:
        print("Invalid choice")
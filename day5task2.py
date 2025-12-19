# Print a multiplication table of the number that is input by the user

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
    
    
# Check if the given number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even Number")
else:
    print(num, "is Odd Number")
    
    
# Check if a given number is palindrome or not
num = input("Enter a number: ")

if num == num[::-1]:
    print(num, "is a Palindrome")
else:
    print(num, "is not a Palindrome")



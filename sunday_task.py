# 1. Write a program to read a text file and print each line with line numbers.

file = open("sunday.txt", "r")

line_number = 1
for line in file:
    print(line_number, ":", line.strip()) #line_strip removes extra spaces
    line_number +=1
    
file.close()

# 2. Write a program to create a file and write five lines of text into it.

try:
    file = open("sunday.txt", "w")   
    
    for i in range(1, 6):            
        file.write(f"This is line {i}\n")
    file.close()  

except Exception as e:
    print("An error occurred:", e)
    
# 3. Write a program to count the number of words in a given text file.

file = open('sunday.txt', 'r')   

content = file.read()             
words = content.split()           # Split text into words
print("Number of words:", len(words))

file.close()      

# 4. Write a program that takes two numbers and handles the error if division by zero occurs.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

try:
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    
#5. Write a program that handles the error when trying to open a file that does not exist.

filename = input("Enter the filename to open: ")

try:
    file = open(filename, 'r')
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
    
#6. Write a program that asks the user for an integer and handles invalid input.

try:
    num=float(input("enter the number:"))
    print(num)
except ValueError:
    print("invalid input")

#7. Create a class with two attributes and print the values using objects.

class Dog:
    def __init__(self, name, action):
        self.name = name
        self.action = action
        
dog1 = Dog("Hero", "Bark")
print("Name:", dog1.name)
print("Action:", dog1.action)

#8. Create a class with methods to perform basic arithmetic operations and call them.

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

calc = Calculator()

print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))
print("Multiplication:", calc.multiply(10, 5))
print("Division:", calc.divide(10, 5))
print("Division by zero:", calc.divide(10, 0))

#9.  Create a class with a constructor that initializes two attributes and displays them.

class Cat:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def display(self):
        print("Name: ",self.name)
        print("Action: ",self.action)

cat1 = Cat("Suri", "Meow")
cat1.display()

#10. Create a parent class and a child class where the child overrides one method.

class Animal:
    def sound(self):
        print("Animal sound")
        
class Dog(Animal):
    def sound(self):
        print("Bark")

animal1 = Animal()
dog1 = Dog()

animal1.sound()
dog1.sound()
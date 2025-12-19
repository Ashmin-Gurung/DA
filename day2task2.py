# 3)Update the calculator program using IF…ELSE

a = 8
b = 4

number = int(input("Choose a number from 1-5: "))

if number == 1:
    print("Addition:", a + b)
else:
    if number == 2:
        print("Subtraction:", a - b)
    else:
        if number == 3:
            print("Multiplication:", a * b)
        else:
            if number == 4:
                print("Division:", a / b)
            else:
                if number == 5:
                    print("Modulus:", a % b)
                else:
                    print("Invalid number")
    
# 4)Find the greatest and smallest number among three numbers using IF…ELSE
# and logical operators.

a = 5
b = 10
c = 15

# Finding greatest
if a > b and a > c:
    print("Greatest number:", a)
else:
    if b > a and b > c:
        print("Greatest number:", b)
    else:
        print("Greatest number:", c)

# Finding smallest
if a < b and a < c:
    print("Smallest number:", a)
else:
    if b < a and b < c:
        print("Smallest number:", b)
    else:
        print("Smallest number:", c)

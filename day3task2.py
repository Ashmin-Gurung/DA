# updating the calculator program using loop

a = 8
b = 4

for i in range(3):    
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
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b
def floor(a, b):
    return a // b
def modulus(a, b):
    return a % b
def exponent(a, b):
    return a ** b
#4facfe

while True:
    print("======== Welcome to my calculator app =======")
    print("\n 1.Add 2.Subtract 3.Multiply 4.Divide 5.Floor 6.Modulus 7.Exponent 8.Quit")
    choice = int(input("enter your choice: "))

    if choice == 8:
        print("Goodbye, See you later")
        break
    try: 
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))


        if choice == 1:
            print("Result: ", add(a,b))

        elif choice == 2:
            print("Result: ", subtract(a,b))

        elif choice == 3:
            print("Result: ", multiply(a,b))

        elif choice == 4:
            print("Result: ", divide(a,b))

        elif choice == 5:
            print("Result: ", floor(a,b))

        elif choice == 6:
            print("Result: ", modulus(a,b))

        elif choice == 7:
            print("Result: ", exponent(a,b))
        else:
            print("invalid choice")

    except ValueError:
        print("Please enter valid number")

    except ZeroDivisionError as e:
        print(e)


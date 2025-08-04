def sum(a, b) -> float:

    if a is not int or b is not int:
        print("ERROR")
        return
    
    return a + b

def sub(a, b) -> float:

    if a is not int or b is not int:
        print("ERROR")
        return

    return a - b

def div(a, b) -> float:

    if a is not int or b is not int:
        print("ERROR")
        return

    return a / b

def mult(a, b) -> float:

    if a is not int or b is not int:
        print("ERROR")
        return

    return a * b


def menu():
    print("Select the operation: ")
    print("+")
    print("-")
    print("/")
    print("*")

    opt = input("Enter operation (+, -, /, *): ")

    if opt not in ["+", "-", "/", "*"]:
        print("Invalid operation selected.")
        return

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if opt == "+":
        result = sum(a, b)
    elif opt == "-":
        result = sub(a, b)
    elif opt == "/":
        result = div(a, b)
    elif opt == "*":
        result = mult(a, b)
    else:
        print("Unknown operation.")
        return

    print(f"Result: {result}")

a = int(input("Enter number 1 = "))
b = int(input("Enter number 2 = "))
operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    print("Result =", a + b)
elif operation == "-":
    print("Result =", a - b)
elif operation == "*":
    print("Result =", a * b)
elif operation == "/":
    if b != 0:
        print("Result =", a / b)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operation")
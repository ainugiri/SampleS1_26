def calc(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

while True:
    inp1 = int(input("Enter the first number: "))
    inp2 = int(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    result = calc(inp1, inp2, operation)
    print("The result is:", result)

    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() != "yes":
        print("Calculator stopped.")
        break
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
def calculate(a, b, operation):
    return operation(a, b)


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Choose operation: +, -, *, /")
op = input("Enter operator: ")


if op == '+':
    result = calculate(x, y, add)
elif op == '-':
    result = calculate(x, y, subtract)
elif op == '*':
    result = calculate(x, y, multiply)
elif op == '/':
    result = calculate(x, y, divide)
else:
    result = "Invalid operator"

print("Result:", result)

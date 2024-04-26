def addition(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error Division by 0"
    else:
        return a / b
print("SIMPLE CALCULATOR IN PYTHON")
print("Select the operation:")
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Division")
ch = input("Enter choice (1/2/3/4): ")
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
if ch == '1':
    print("Result:", addition(n1, n2))
elif ch == '2':
    print("Result:", subtract(n1, n2))
elif ch == '3':
    print("Result:", multiply(n1, n2))
elif ch == '4':
    print("Result:", division(n1, n2))
else:
    print("Given Incorrect Input")

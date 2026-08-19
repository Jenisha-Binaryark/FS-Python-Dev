num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

op = input("Enter operator: ")

if op == '+':
    print(f"Addition is: {num1+num2}")
elif op == '-':
    print(f"Subtraction is: {num1-num2}")
elif op == '*':
    print(f"Multiplication is: {num1 * num2}")
elif op == '/':
    print(f"Division: {num1 / num2}")
else:
    print("Invalid input")
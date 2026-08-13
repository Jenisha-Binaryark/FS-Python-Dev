num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number: "))

print("Please select the operation: \n"
    "1: Addition\n"
    "2: Subtraction\n"
    "3: Multiplication\n"
    "4: Division")

sel = int(input("Select the operation:"))

if sel == 1:
    print(f"Addition is: {num1 + num2}")
elif sel == 2:
    print(f"Subtraction is: {num1 - num2}")
elif sel == 3:
    print(f"Multiplication is: {num1 * num2}")
elif sel == 4:
    print(f"Division is: {num1 / num2}")
else:
    print("Invalid Choice")
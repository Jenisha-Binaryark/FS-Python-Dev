temp = int(input("Enter the temperature: "))
from_unit = input("Enter the unit of temperature: ")
to_unit = input("Enter unit in which you want to convert: ")

if from_unit == 'c' and to_unit == 'f':
    print(f"Fahrenheit: {(temp * 9/5) + 32}")
elif from_unit == 'f' and to_unit == 'c':
    print(f"Celsius: {(temp - 32) * 5/9}")
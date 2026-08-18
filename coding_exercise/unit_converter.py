def convert_temp(value, from_unit, to_unit):
    if from_unit == 'C' and to_unit == 'F':
        return(value * 9/5) + 32
    elif from_unit == 'F' and to_unit == 'C':
        return (value - 32) * 5/9
    elif from_unit == 'C' and to_unit == 'K':
        return value + 273.15
    elif from_unit == 'K' and to_unit == 'C':
        return value - 273.15
    else:
        return value

def convert_len(value, from_unit, to_unit):
    km_to_miles = 0.621371
    if from_unit == 'km' and to_unit == 'miles':
        return value * km_to_miles
    elif from_unit == 'miles' and to_unit == 'km':
        return value / km_to_miles
    return value

def main():
    while True:
        print("\nUnit Converter")
        print("\n1. Temperature\n2. Lenght\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            value = float(input("Enter value: "))
            from_unit = input("From (C/F/K): ").upper()
            to_unit = input("To (C/F/K): ").upper()
            result = convert_temp(value, from_unit, to_unit)
            print(f"{value}{from_unit} = {result:.2f}{to_unit}")

        elif choice == '2':
            value = float(input("Enter value: "))
            from_unit = input("From (km/miles): ").lower()
            to_unit = input("To (km/miles): ").lower()
            result = convert_len(value, from_unit, to_unit)
            print(f"{value} {from_unit} = {result:.2f} {to_unit}")

        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

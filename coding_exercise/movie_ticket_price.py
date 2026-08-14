age = int(input("Enter your age: "))
day = input("Is it a weekday or weekend? ").lower()

basePrice = 400
weekendPrice = basePrice - (10 * basePrice / 100)

if age < 12:
    price = basePrice - (50 * basePrice / 100)
    print(f"Kids discount price: {price}")
elif age >= 60:
    price = basePrice - (30 * basePrice / 100)
    print(f"Senior citizen discount price: {price}")
elif day == "weekend":
    print(f"Weekend Price: {weekendPrice}")
else:
    print(f"Ticket Price: {basePrice}")
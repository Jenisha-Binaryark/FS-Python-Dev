original_bill = float(input("Enter the amount of bill: "))
tip = int(input("Enter the percentage of tip you want to give: "))
people = int(input("Enter total number of people: "))

tip_amount = original_bill * (tip / 100)
total_bill = original_bill + tip_amount
split = total_bill/people

print(f"Tip amount: ₹{tip_amount:.2f}")
print(f"Total bill (with tip): ₹{total_bill:.2f}")
print(f"Each person owes: ₹{split:.2f}")
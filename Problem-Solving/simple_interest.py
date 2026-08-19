principal = float(input("Enter the initial amount: "))
rate = float(input("Enter the rate: "))
time = float(input("Enter the time in months: "))

si = (principal * rate * time) / 100
print(f"Interest is: Rs.{si}")
print(f"Total Amount is: Rs.{principal + si}")
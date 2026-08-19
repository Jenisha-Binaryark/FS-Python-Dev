numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(numbers)

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest number is:", largest)
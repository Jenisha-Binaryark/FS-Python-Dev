s = input("Enter a string: ")
s = s.lower()
new_s = ""
print(s)

for char in s:
    if char.isalnum():
        new_s += char
print(new_s)

reverse = new_s[::-1]
if new_s == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
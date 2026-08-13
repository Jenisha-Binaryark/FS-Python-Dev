# VARIABLES
# Basic Assignment
x = 10
y = "hello"
print(x, y)

# Dynamic Typing
a = 20
print(a)
a = "String now"
print(a)

# Assigning different values
j, k, l = 10, 20, "universe"
print(j, k , l)

# Assigning same value
h = d = t = 100
print(h,d,t)

# DATA TYPES
# Numeric
ab = 10
cd = 5.9
ef = 2 + 1j
print(type(ab))
print(type(cd))
print(type(ef))

# Sequence
jk = "Just Kidding"
hd = [100, 200, 500]
rf = (99, 25, 60)
print(type(jk))
print(type(hd))
print(type(rf))

# Boolean
age = 20
is_adult = age >= 18
print(is_adult)

# Set
fruits = {"apple", "banana", "mango", "apple"}
print(fruits)

# Dictionary
di = {1:'hello', 2:'my dear', 3:'viewer'}
print(di)
print(di.keys())
print(di.values())

#TYPE CONVERSION
# String to Integer
age = "20"
age = int(age)
print(age)
print(type(age))

# Integer to Float
num = 10
num = float(num)
print(num)

# Integer to String
txt = 100
txt = str(txt)
print(txt)
print(type(txt))

# Integer to Boolean
num = 1
print(bool(num))

# INPUT/OUTPUT
name = input("Enter your name: ")
print(f"Your name is {name}")

#FORMATTED STRING
first_name = input("Enter your first name: ")
age = int(input("Enter your age: "))
print(f"Your name is {first_name} and your age is {age}")
print("=" * 60)
print("001 python tutorial for beginners")
print("=" * 60)

print("I like pizza!")
print("It's really good!")

print("------------------------------------------------------------")

print("=" * 60)
print("002 variables")
print("=" * 60)

first_name = "Bro"
food = "pizza"
email = "hi@mail.com"

print(f"Hello {first_name}!")
print(f"You like {food}!")
print(f"Your email is {email}.")

print("------------------------------------------------------------")

age = 25
quantity = 3
num_students = 30

print(f"You are {age} years old.")
print(f"You are buying {quantity} items.")
print(f"Your class has {num_students} students.")

print("------------------------------------------------------------")

price = 10.99
distance = 6.6
print(f"The price is ${price}")
print(f"You ran {distance} km.")

print("------------------------------------------------------------")

is_student = False
for_sale = True
is_online = True

print(f"Are you a student? {is_student}")

if is_student:
    print("You are a student!")
else:
    print("You are not a student.")

if for_sale:
    print("That item is for sale!")
else:
    print("That item is not for sale.")

if is_online:
    print("You are online!")
else:
    print("You are offline.")

print("------------------------------------------------------------")

print("=" * 60)
print("003 type casting")
print("=" * 60)

name = "Bro"
age = 26
balance = 12200.25
is_student = True

print(type(name))
print(type(age))
print(type(balance))
print(type(is_student))

balance = int(balance)
print(balance)

age = float(age)
print(age)

age = str(age)
print(age)
print(type(age))
print(age + "1")

name = bool(name)
print(name)
name = ""
name = bool(name)
print(name)

print("------------------------------------------------------------")

print("=" * 60)
print("004 user input")
print("=" * 60)

# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
# age = age + 1
#
# print(f"Hello {name}!")
# print("Happy Birthday!")
# print(f"You are {age} years old.")

# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))
# area = length * width
# print(f"The area is {area}cm²")


# item = input("What item would you like to buy?: ")
# price = float(input("What is the price?: "))
# quantity = int(input("How many would you like?: "))
# total = price * quantity
# print(f"You have bought {quantity} x {item}/s.")
# print(f"Your total is ${total}.")

print("------------------------------------------------------------")


print("=" * 60)
print("005 madlibs game")
print("=" * 60)

# Madlibs games
# word game where you create a story
# by filling in blanks with random words

# adjective1 = input("Enter an adjective (description): ")
# noun1 = input("Enter a noun (person, place, thing): ")
# adjective2 = input("Enter an adjective (description): ")
# verb1 = input("Enter a verb ending with 'ing'")
# adjective3 = input("Enter an adjective (description): ")
#
# print(f"Today I went to a {adjective1} zoo.")
# print(f"In an exhibit, I saw a {noun1}.")
# print(f"{noun1} was {adjective2} and {verb1}.")
# print(f"I was {adjective3}!")



print("------------------------------------------------------------")

print("=" * 60)
print("006 arithmetic & math")
print("=" * 60)

friends = 0
friends += 3

print(friends)

friends -= 1
friends *= 3
print(friends)

friends /= 2
print(friends)

friends **= 2
print(friends)

remainder = friends % 2
print(remainder)

x = 3.14
y = -4
z = 5


result = round(x)
print(result)

result = abs(y)
print(result)

result = pow(4, 3)
print(result)

print(max(x, y, z))
print(min(x, y, z))

import math # math library
print(math.pi)
print(math.e)

x = 9
result = math.sqrt(x)
print(result)

print(math.ceil(9.1))
print(math.floor(9.9))

# import math
# radius = float(input("Enter the radius of a circle: "))
# circumference = 2 * math.pi * radius
# print(f"The circumference of a circle with radius {radius} is {circumference}")

# radius = float(input("Enter the radius of a circle: "))
# area = math.pi * radius ** 2
# print(f"The area of a circle is: {round(area, 2)}cm^2")

# a = float(input("Enter side A:"))
# b = float(input("Enter side B:"))
# c = math.sqrt(pow(a, 2) + pow(b, 2))
# print(f"The hypotenuse is: {round(c, 2)}")

print("------------------------------------------------------------")


print("=" * 60)
print("007 if statements")
print("=" * 60)

age = 100

if age >= 100:
    print("You are a very old person.")
elif age < 0:
    print("You are not a valid age.")
elif age >= 18:
    print("You are now signed up!")
else:
    print("You must be 18+ to sign up.")

# response = input("Would you like food? (Y/N): ").upper()
#
# if response == "Y":
#     print("Have some food!")
# else:
#     print("No food for you!")

# name = input("Enter your name: ")
#
# if name == "":
#     print("Please enter a name.")
# else:
#     print("Welcome, " + name + "!")


for_sale = True

if for_sale:
    print("That item is for sale!")
else:
    print("That item is not for sale.")

online = False

if online:
    print("You are online!")
else:
    print("You are offline.")

print("------------------------------------------------------------")


print("=" * 60)
print("008 calculator program")
print("=" * 60)

# operator = input("Enter an operator (+ - * /): ")
# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2nd number: "))
#
# if operator == "+":
#     result = num1 + num2
#     print(round(result))
# elif operator == "-":
#     result = num1 - num2
#     print(round(result))
# elif operator == "*":
#     result = num1 * num2
#     print(round(result))
# elif operator == "/":
#     result = num1 / num2
#     print(round(result))
# else:
#     print(f"{operator} is invalid.")

print("------------------------------------------------------------")

print("=" * 60)
print("009 weight conversion program")
print("=" * 60)

# weight = float(input("Enter your weight: "))
# unit = input("Kilograms or Pounds? (K or L): ")
#
#
# if unit == "K":
#     weight = weight * 2.205
#     unit = "Lbs."
#     print(f"Your weight is {round(weight, 1)} {unit}.")
# elif unit == "L":
#     weight = weight / 2.205
#     unit = "Kgs."
#     print(f"Your weight is {round(weight, 1)} {unit}.")
# else:
#     print(f"{unit} was not valid.")


print("------------------------------------------------------------")

print("=" * 60)
print("010 temperature conversion program")
print("=" * 60)

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round(temp * 9 / 5 + 32, 1)
    print(f"The temperature in Celsius is {temp}°F.")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is {temp}°C.")
else:
    print(f"{unit} is an invalid unit of measurement")

print("------------------------------------------------------------")
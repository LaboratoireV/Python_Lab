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
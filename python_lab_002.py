from typing import cast

print("=" * 60)
print("031 functions")
print("=" * 60)

def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"Happy Birthday to {age} years old!")

happy_birthday("Bro", 20)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount: .2f} is sue : {due_date}")

display_invoice("BroCode", 20, "2026-08-20")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def square(x):
    return x ** 2

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("bro", "code")
print(full_name)



print("------------------------------------------------------------")
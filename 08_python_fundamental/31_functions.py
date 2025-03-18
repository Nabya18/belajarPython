# function = a block of reusable code
#  place () after the function name to invoke it
# function can have parameters matching the arguments passed to it

def happy_birthday(name, age): # name is a parameter
    print(f"Happy Birthday to you, {name}!")
    print(f"You are {age} years old!")
    print("Happy Birthday, dear you!")
    print()

happy_birthday("Alice", 20) # Alice is an argument
happy_birthday("Bob", 30) # Bob is an argument
happy_birthday("Charlie", 40) # Charlie is an argument


def display_invoice(username, amount, due_date):
    print(f"Hello, {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}.")
    print()

display_invoice("Alice", 42.50, "2021-12-31")


# return = statement used to end a function
# and send a result back to the caller

def add(a, b):
    z = a + b
    return z

def subtract(a, b):
    z = a - b
    return z

def multiply(a, b):
    z = a * b
    return z

def divide(a, b):
    z = a / b
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

print()

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("alice", "wonderland")

print(full_name)
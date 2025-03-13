# while loop = exeecute some code WHILE some condition remains true

name = input("Enter your name: ")
age = int(input("Enter your age: "))
food = input("Enter a food you like? (q to quit): ")
num = int(input("Enter a number between 1 - 10: "))


while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ") # ini akan terus diulang sampai user memasukkan nama

print(f"Hello, {name}")


while age < 0:
    print("Age cannot be negative")
    age = int(input("Enter your age: "))

print(f"Your age is {age}")


while not food == "q":
    print(f"You like {food} too!")
    food = input("Enter another food you like? (q to quit): ")

print("Goodbye!")


while num < 1 or num > 10:
    print(f"{num} is not between 1 - 10")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}")
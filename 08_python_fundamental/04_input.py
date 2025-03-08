# input() = A function that prompts the user to enter data
# returns the entered data as string

name = input(" What is your name? ")
age = int(input(" How old are you? "))

age = age + 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old")


# Excercise 1 Rectangle Area Calculator
length = int(input(" Enter the length:"))
width = int(input(" Enter the width:"))
area = length * width
print(f"The area of the rectangle is {area}cm\u00b2")

# link: https://www.tutorialspoint.com/how-to-print-superscript-and-subscript-in-python


# Exercise 2 shopping cart program
item = input("What item would you like to buy? ")
price = float(input(f"what is the price of the {item}? "))
quantity = int(input("how many would you like to buy? "))
total = price * quantity

print(f"you are buying {quantity} x {item}'s")
print(f"your total is ${total}")
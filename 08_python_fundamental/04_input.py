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
print(f"The area of the rectangle is {area}")
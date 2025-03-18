"""
# Membership Operators = Used to test whether a value or variable is found in a sequence
#                       (string, list, tuple, set and dictionary)
# 1. in = Returns True if a sequence with the specified value is present in the object
# 2. not in = Returns True if a sequence with the specified value is not present in the object
# boolean
"""

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter.upper() in word:
    print(f"There is a {letter.upper()}")
else:
    print(f"{letter.upper()} was not found")


# students = {"John", "Jane", "Joe"}
#
# student = input("Enter the student's name: ")
#
# if student.capitalize() not in students:
#     print(f"{student.capitalize()} is not in the class")
# else:
#     print(f"{student.capitalize()} is in the class")


grades = {"John": "A",
          "Jane": "B",
          "Joe": "C"}

student = input("Enter the student's name: ")
student = student.capitalize()

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} is not in the class")


email = "BroCode@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")
"""
# iterables = An object/collection that can return its elements one at a time,
allowing it to be iterated over in a loop.
"""

numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers):
    print(number)


fruits = {"Apple", "Banana", "Cherry"}

for fruit in fruits:
    print(fruit)


my_dict = {"A": 1, "B": 2, "C": 3}

for key, value in my_dict.items(): # items() method returns a view object that displays a list of a dictionary's key-value tuple pairs
    print(f"{key}: {value}")
"""
# List Comprehensions = A concise way to create lists in Python
# compact and easier to read than traditional loops
# Syntax = [expression for value in iterable if condition]
"""

# traditional way
# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

print(doubles)
print(triples)
print(squares)

fruits = ["apple", "banana", "cherry", "durian", "elderberry", "fig", "grape"]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)


# with condition
numbers = [1, -2, -3, -4, -5, 6, 7, -8, 9, 10]
positive_nums = [num for num in numbers if num >= 0] # value of num if > 0
negative_nums = [num for num in numbers if num < 0] # value of num if < 0
even_nums = [num for num in numbers if num % 2 == 0] # value of num if num % 2 == 0

print(positive_nums)
print(negative_nums)
print(even_nums)


# with condition and expression
grades = [90, 55, 70, 75, 100]
passing = [grade for grade in grades if grade >= 60]

print(passing)
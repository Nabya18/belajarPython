"""
# module = A file containing code you want to include in your program
# use 'import' to include a module (built-in or your own)
# useful to break up a large program reusable separate files
# the alias 'as' can be used to rename a module, but program will execute variable if same name with module. Module name should be unique
"""

import math
from math import pi

print(math.pi)
print(pi)
print()


# my own module
import example_module as example

pi = example.pi
square = example.square(3)
cube = example.cube(3)
circumference = example.circumference(3)
area = example.area(3)

print(pi)
print(square)
print(cube)
print(circumference)
print(area)
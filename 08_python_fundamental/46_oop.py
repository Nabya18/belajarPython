"""
# object = A "bundle" of related attributes (variables) and methods (functions)
# eX. phone, cup, book
# You need a 'class' to create many object

# class = (blueprint) used to design the structure and layout of an object
"""
from car_46 import car

car1 = car("Mustang", "2024", "Red", True)
car2 = car("Civic", "2022", "Blue", False)
car3 = car("Corolla", "2023", "Green", True)

car2.describe()
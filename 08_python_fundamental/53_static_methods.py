"""
# Static methods = Methods that belong to the class rather than any object from the class (instance)
# Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that don't need access to the instance or class data
"""

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} is a {self.position}"

    @staticmethod
    def is_valid_position(position): # doesn't need self because it doesn't access any instance data
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = Employee("Eugine", "Manager") # instance method
employee2 = Employee("Squidward", "Cashier") # instance method
employee3 = Employee("Spongebob", "Cook") # instance method

print(Employee.is_valid_position("Cashier")) # static method
print(employee1.get_info()) # instance method
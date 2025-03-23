"""
# super() = Function used in a child class to call method from the parent class (superclass).
# Allows you to extend the functionality of the inherited methods
"""

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled) # call the parent class constructor
        self.radius = radius

    def describe(self):
        super().describe() # if not called, the parent class method will be overridden
        print(f"It is a circle with an area of {3.14 * self.radius ** 2} cm^2")

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.side = width

    def describe(self):
        super().describe()
        print(f"It is a square with an area of {self.side ** 2} cm^2")

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.base = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of {0.5 * self.base * self.height} cm^2")

circle = Circle("red", True, 5)
square = Square("blue", False, 6)
triangle = Triangle("green", True, 7, 8)

circle.describe() # don't need print() because it's already in the method
square.describe()
triangle.describe()
"""
# Property = Decarotor used to define a method as a property (it can be accessed like an attribute)
# benefit: Add additional logic when read, write, or delete attributes
# Gives you getter, setter, and deleter method
"""

class Rectangle:

    def __init__(self, width, height):
        self._width = width # private attribute / protected attribute
        self._height = height

    @property # getter method
    def width(self): # need to use the getter method cause it's a private attribute
        return f"{self._width:.2f}" # return the private attribute

    @property # getter method
    def height(self):
        return f"{self._height:.2f}" # return the private attribute

    @width.setter # setter method
    def width(self, new_width): # set the private attribute
        if new_width < 0:
            self._width = new_width
        else:
            print("Width must be positive")

    @height.setter # setter method
    def height(self, new_height):
        if new_height < 0:
            self._height = new_height
        else:
            print("Height must be positive")

    @width.deleter # deleter method
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter # deleter method
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle = Rectangle(10, 20)

rectangle.width = 0

del rectangle.width
del rectangle.height
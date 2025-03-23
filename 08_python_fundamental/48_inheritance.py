"""
# Inheritance = Allows a class to inherit attributes and methods from another class
# Helps with code reusability and extensibility
# class Child(Parent)

benefits:
can make change in 1 time
"""

class Animal: # Parent class / Super class
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal): # Dog class inherits from Animal class / Child class / Sub class
    def speak(self):
        print("Woof!")

class Cat(Animal): # Cat class inherits from Animal class
    def speak(self):
        print("Meow!")

class Mouse(Animal): # Mouse class inherits from Animal class
    def speak(self):
        print("Squeak!")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
cat.speak()
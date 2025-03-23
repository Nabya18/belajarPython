"""
# "Duck typing" = Another way to achieve polymorphism besides inheritance
# Object must have the minimum necessary attributes/methods
# "if it looks like a duck and quacks like a duck, it must be a duck"
"""

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Car: # must have the speak() method to be included in the list

    alive = False

    def speak(self):
        print("Honk!")

animals = [Dog(), Cat(), Car()] # even though Car is not an animal, it can still be included in the list

for animal in animals:
    animal.speak() # must have the speak() method
    print(animal.alive)
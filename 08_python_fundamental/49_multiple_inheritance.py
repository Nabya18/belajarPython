"""
# Multiple Inheritance = inherit from more than 1 parent class
# C(A, B) = C class inherits from A and B class

# multilevel inheritance = inherit from a parent which inherits from another parent
# C(B) <- B(A) <- A
"""
class Animal:

    def __init__(self, name): # this constructor method will be inherited by all child classes
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): # multiple inheritance
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

fish.eat()
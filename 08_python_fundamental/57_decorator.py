"""
# Decorator = A function that extends the behavior of another function
# without modifying the base function itself
# pass the base function as an argument to the decorator function

order of execution from the innermost to the outermost

def uppercase(func):
    def wrapper():
        print("Before calling the function.")
        result = func().upper()
        print(result)
        return result
        print("After calling the function.")
    return wrapper

def extenstion_text(func):
    def wrapper():
        print("Before calling the function.")
        result = "Ini, " + func()
        print(result)
        return result
        print("After calling the function.")
    return wrapper

# Applying the decorator to a function
@extenstion_text
@uppercase
def hello():
    return "Hello world"

hello()
"""

def add_sprinkles(func):
    def wrapper(*args, **kwargs): # because we don't know how many arguments will be passed
        print("Sprinkles are added")
        func(*args, **kwargs) #call the base function
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Fudge is added")
        func(*args, **kwargs) #call the base function
    return wrapper

@add_sprinkles # decorator, extended function
@add_fudge # decorator
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍦")

get_ice_cream("Vanilla")


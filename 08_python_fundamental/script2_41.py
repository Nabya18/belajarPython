from script1_41 import *

def favorite_drink(drink):
    print(f"My favorite drink is {drink}")

def main():
    print("This is script2")
    favorite_food("Sushi") # from script1
    favorite_drink("Tea")
    print("Goodbye!")

if __name__ == '__main__':
    main()
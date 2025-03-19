def favorite_food(food):
    print(f"My favorite food is {food}")

def main(): # without this, the code will run when imported
    print("This is script1")
    favorite_food("Pizza")
    print("Goodbye!")

if __name__ == '__main__': # we will run this script directly
    main()
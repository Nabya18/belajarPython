menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("----- MENU -----")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("----- MENU -----")

while True:
    food = input("Enter the food you want to buy: (q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("----- YOUR ORDER -----")
for food in cart:
    total += menu.get(food) # get the value of the key
    print(food, end=" ")

print() # print a new line
print(f"Your total is: ${total:.2f}")
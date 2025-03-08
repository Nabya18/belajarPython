# if = Do some code if the condition is true
# else do something else

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up") # harus diletakkan paling awal, jika tidak, tidak akan dijalankan karena sudah ada kondisi 18+
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You must enter a valid age")
else:
    print("'You must be 18+ to sign up")


response = input("Would you like food? (Y/N): ")

if response == "Y" or response == "y": # harus menggunakan == untuk membandingkan
    print("Here is your food")
else:
    print("Ok, no food for you")


name = input("Enter your name: ")

if name == "":
    print("You must enter a name")
else:
    print(f"Hello, {name}")


for_sale = True

if for_sale:
    print("The item is for sale")
else:
    print("The item is NOT for sale")
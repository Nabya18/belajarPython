# variable = a container for a value (string, integer, float, boolean)
# A variable behaves as if it was the value it contains


# String
first_name = "John"
food = "pizza"
email = "john@email.com"

print(f"Hello {first_name}!")
print(f"you like {food}!")
print(f"Your email is {email}")


# Integer
age = 25
quantity = 3
num_of_students = 100

print(f"you are {age} years old")
print(f"you are buying {quantity} pizzas")
print(f"there are {num_of_students} students in the class")


# Float
price = 10.99
gpa = 3.9
distance = 5.5

print(f"the price is ${price}")
print(f"your GPA is: {gpa}")
print(f"you are running {distance}km")


# Boolean
is_student = False
for_sale = True

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

if for_sale:
    print("The item is for sale")
else:
    print("The item is NOT for sale")
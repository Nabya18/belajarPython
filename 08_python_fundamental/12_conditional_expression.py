# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
# print or assign one of two values based on a condition
# formula = x if condition else y

num = -2
a = 8
b = 7
age = 27
temperature = 25
user_role = "admin"

print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "ADULT" if age >= 18 else "CHILD"
weather = "HOT" if temperature > 30 else "COLD"
access_level = "FULL ACCESS" if user_role == "admin" else "LIMITED ACCESS"

print(result)
print(max_num)
print(min_num)
print(status)
print(weather)
print(access_level)
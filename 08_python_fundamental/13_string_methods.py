name = input("Enter your name: ")
phone_number = input("Enter your phone number: ")

result = len(name) # this function will return the length of the string whitespace included
fresult = name.find("a") # this function will return the index of the first character in the string
rfresult = name.rfind("a") # this function will return the index of the character in the string starting from the right (reverse find) => - is no result
cresult = name.capitalize()
name = name.upper()
name.isdigit() # this function will return True if the string is all digits
name.isalpha() # this function will return True if the string is all letters (without whitespace)
phone_number.count("-") # this function will return the number of times the character appears in the string
phone_number.replace("-", " ") # this function will replace the first argument with the second argument

#print(help(str)) # this function will return the documentation of the string methods

print(result)
print(fresult)
print(rfresult)
print(cresult)


# validate user input exercise
"""
1. username is no more than 10 characters
2. username must not contain spaces
3. username must not contain digits
"""
username = input("Enter your username: ")

if len(username) > 10:
    print("Username must be less than 10 characters")
elif not username.find(" ") == -1:
    print("Username must not contain spaces")
elif not username.isalpha():
    print("Username must not contain digits")
else:
    print(f"Welcome, {username}")
"""
args = allows you to pass multiple non-key arguments (tuple type data)
kwargs = allows you to pass multiple keyword-arguments (dictionary type data)
* unpacking operator
1. Positional, 2. default, 3. keyword, 4. ARBITRARY
"""

def add(*args):
    #print(type(args))
    total = 0
    for arg in args:
        total += arg
    return total

print(add(3, 4, 5, 6, 7, 8, 9, 10))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Mr.", "John", "Smith", "III")
print()

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Main St",
              apt="100",
              city="New York",
              state="NY",
              zip="10001")

# combine *args and **kwargs -> *args must come before **kwargs
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

shipping_label("Mr.", "John", "Smith", "III",
                street="123 Main St",
                apt="100",
                city="New York",
                state="NY",
                zip="10001")
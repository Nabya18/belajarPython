"""
keyword arguments = an argument preceded by an identifier
helps with readability
order of arguments doesn't matter
1. Positional, 2. default, 3. KEYWORD, 4. arbitrary
"""

def hello(greeting, title, first, last):
    print(f"{greeting}, {title}{first} {last}!")

hello("Hello", title="Mr.", last="Smith", first="John")


print("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", sep=" - ") # sep is a keyword argument


def get_phone(country, area, first, last):
    print(f"({country})-{area}-{first}-{last}")

phon_num = get_phone(country=1, area=555, last=123, first=4567)
print(phon_num)
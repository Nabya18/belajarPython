# dictionary = a collection of {key:value} pairs
# ordered, changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

if capitals.get("China"): # get the value of the key
    print("That capital exists")
else:
    print("That capital does not exist")

capitals.update({"Germany": "Berlin"}) # add a new key-value pair or update an existing key-value pair
# capitals.pop("China") # remove the key-value pair
# capitals.popitem() # remove the last key-value pair
# capitals.clear() # remove all key-value pairs

keys = capitals.keys()

for key in keys:
    print(key)

print()

values = capitals.values()

for value in values:
    print(value)

print()

items = capitals.items()
for key, value in items:
    print(f"{key}: {value}")

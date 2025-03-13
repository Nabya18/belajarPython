# collection = single "variable" used to store multiple values
# collection types = list, tuple, set, dictionary
# List  = [] ordered and changeable. Duplicates OK
# Tuple = {} ordered and unchangeable. Duplicates OK. FASTER
# Set   = () unordered, immutable, and unindexed. Add/remove OK. No duplicates

# List
fruits = ["apple", "banana", "cherry", "durian", "elderberry", "fig", "grape"] # list
# print(fruits[::-1]) # reverse the list
# print(dir(fruits)) # return the list of methods that can be used with the list
# print(help(fruits)) # return the documentation of the list methods
# print(len(fruits)) # return the length of the list
# print("apple" in fruits) # return True if the element is in the list

print(fruits.index("banana")) # return the index of the element

fruits.append("honeydew") # add an element to the end of the list
fruits.remove("apple")
fruits.insert(0, "pineapple") # add an element to the specified index
fruits.sort() # sort the list based on the ASCII value
fruits.reverse() # reverse the list

for fruit in fruits:
    print(fruit)


# Set
fruits_set = {"apple", "banana", "cherry", "durian", "elderberry", "fig", "grape"} # set
# fruits_set.remove("apple")
fruits_set.pop() # remove the last element

print(fruits_set)


# Tuple
fruits_tuple = ("apple", "banana", "cherry", "durian", "elderberry", "fig", "grape") # tuple
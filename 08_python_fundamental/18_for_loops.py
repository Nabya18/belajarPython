# for loops = execute a block of code a specified number of times
# you can iterate over a sequence (string, list, tuple, set, dictionary, or range)

credit_card = "1234-5678-9012-3456"

for x in reversed(range(1, 11)): # reversed() function will reverse the range (start, end, step)
    print(x)

print("Happy New Year!") # this will print after the loop is done


for x in credit_card:
    print(x)


for x in range(1, 21):
    if x == 13:
        continue # skip the rest of the code and go to the next iteration
    else:
        print(x)
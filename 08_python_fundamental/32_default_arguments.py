# default arguments = A default value for certain parameters
# default is used when that argument is omitted
# make your function more flexible, reduces # of arguments
# 1. Positional, 2. DEFAULT, 3. keyword, 4. arbitrary
# Always put non-default parameters first, followed by default parameters.

def net_price(list_price, discount=0, tax=0.05): # default arguments
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0.1, 0))
print()


import time
def count(end, start=0):
    for x in range(start, end+1): # end+1 to include the end value
        print(x)
        time.sleep(1)
    print("Done!")

count(5)
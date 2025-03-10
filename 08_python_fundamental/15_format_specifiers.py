# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces for the value
# :03 = allocate and zero pad that many spaces for the value
# :< = left align
# :> = right align
# :^ = center align
# :+ = use a plus sign for positive numbers
# : = insert a space before positive numbers
# :, = use a comma as a thousand separator


price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

# many decimal places
print(f"Price 1: ${price1:.2f}") # 3.14
print(f"Price 2: ${price2:.2f}") # -987.65
print(f"Price 3: ${price3:.2f}") # 12.34

# allocate spaces
print(f"Price 1: ${price1:10}")
print(f"Price 2: ${price2:10}")
print(f"Price 3: ${price3:10}")

# zero pad
print(f"Price 1: ${price1:010}")
print(f"Price 2: ${price2:010}")
print(f"Price 3: ${price3:010}")

# left align
print(f"Price 1: ${price1:<10}")
print(f"Price 2: ${price2:<10}")
print(f"Price 3: ${price3:<10}")

# right align
print(f"Price 1: ${price1:>10}")
print(f"Price 2: ${price2:>10}")
print(f"Price 3: ${price3:>10}")

# center align
print(f"Price 1: ${price1:^10}")
print(f"Price 2: ${price2:^10}")
print(f"Price 3: ${price3:^10}")

# plus sign
print(f"Price 1: ${price1: }")
print(f"Price 2: ${price2:+}")
print(f"Price 3: ${price3: }")

# thousand separator
print(f"Price 1: ${price1:,}")
print(f"Price 2: ${price2:,}")
print(f"Price 3: ${price3:,}")

# a view flags
print(f"Price 1: ${price1:+,.2f}")
print(f"Price 2: ${price2:+,.2f}")
print(f"Price 3: ${price3:+,.2f}")
# indexing = accesiing the index of the string
# [start : end : step] -> start is inclusive, end is exclusive

credit_number = "1234-5678-9012-3456"
last_digits = credit_number[-4:] # -4 is the last 4 digits
reverse_credit_number = credit_number[::-1] # reverse the string

print(credit_number[0:4]) # 1234
print(credit_number[-1])
print(credit_number[::2]) # 13-6891-46
print(f"XXXX-XXXX-XXXX-{last_digits}") # XXXX-XXXX-XXXX-3456
print(reverse_credit_number) # 6543-2109-8765-4321
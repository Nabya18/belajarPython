# nested loop = A loop within another loop (outer, inner)
# outer loop:
#   inner loop:

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print() # this will print a new line after the inner loop is done
"""
# Python writing files (.txt, .csv, .json, .xml, etc.)
# 1. Open a file
# 2. Write or append data -> "w" = write, "a" = append
# 3. Close the file
# x -> already exist
# / or \\
"""
import json
import csv

# employees = ["John", "Jane", "Doe", "Smith"] # collection need for loop

# txt_data = "Hello, this is a text file"

# employees = {"John": "Manager",
#              "Jane": "Cashier",
#              "Doe": "Cook",
#              "Smith": "Janitor"}

employees = [["Name", "Age", "Position"],
             ["John", 25, "Manager"],
             ["Jane", 22, "Cashier"],
             ["Doe", 30, "Cook"],
             ["Smith", 40, "Janitor"]]

file_path = "text_60.txt"

# try:
#     with open(file_path, "a") as file:
#         file.write("\n" + txt_data)
#         print(f"File '{file_path}' created")
# except FileExistsError:
#     print(f"File '{file_path}' already exists")


# collection
# try:
#     with open(file_path, "w") as file:
#         for employee in employees:
#             file.write(employee + "\n")
#         print(f"File '{file_path}' created")
# except FileExistsError:
#     print(f"File '{file_path}' already exists")

# json
try:
    with open("text_60.json", "w") as file:
        json.dump(employees, file, indent=4)
        print("File 'text_60.json' created")
except FileExistsError:
    print("File 'text_60.json' already exists")

# csv
try:
    with open("text_60.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(employees)
        print("File 'text_60.csv' created")
except FileExistsError:
    print("File 'text_60.csv' already exists")
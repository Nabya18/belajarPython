# Python reading files (.txt, .csv, .json, .xml, etc.)
# content = json.load(file)
# content = csv.reader(file)


import json
import csv

file_path = "text_60.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("That file doesn't exist")
except PermissionError:
    print("You don't have permission to access that file")
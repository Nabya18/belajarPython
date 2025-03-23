"""
# File Detection = Check file exist or not
# Relative = Connect to the current directory
 Absolute = Connect to the root directory
"""
import os

print("Current Working Directory:", os.getcwd())
file_path = "text_59"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print(f"The location '{file_path}' is a file")
    elif os.path.isdir(file_path):
        print(f"The location '{file_path}' is a directory")
else:
    print(f"The location '{file_path}' doesn't exist")
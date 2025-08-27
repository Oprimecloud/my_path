# This is how it works
# Using os.getcwd()

# 1. Current Working Directory(CWD)

import os 

# Get the current working directory

print("Current working directory:", os.getcwd())

# Ensure to check the output

# 2. Absolute path example
absolute_path = r"C:\Users\User132\Desktop\my_path.py"

# Relative path example 
relative_path = "my_path.py"

print("Absolute Path:", absolute_path)
print("Relative Path:", relative_path)

# 3. joining Paths (The Right Way)

import os

folder = "C:/Users/User132/Desktop"
filename = "my_path.py"

path = os.path.join(folder, filename)
print("Full path:", path)

# This way, Python handles slashes (/ vs \) automatically.

# 4. Checking if a file or folder exists

import os
path = "my_path.py"

if os.path.exists(path):
    print("Yes. the file exists!")
else:
    print("File not found.")


# 5 Using pathlib (Mordern Way)

from pathlib import Path

# Current working directory
print("Current directory:", Path.cwd())

# create a path object 
file = Path("myfile.txt")

# Check if it exists
print("File exists:", file.exists())

# combine paths
folder = Path("C:/Users/User132/Desktop")
full_path = folder / "myfile.txt"
print("Full path:", full_path)

# 6 Navigating Folders wih pathlib
from pathlib import Path


# Get parent folder of current file
print("Parent folder:", Path.cwd().parent)

# List all files in a directory
for file in Path.cwd().iterdir():
    print(file)


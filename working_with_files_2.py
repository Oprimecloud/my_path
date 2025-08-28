# Settting up
# It’s cleaner to work inside a folder so files don’t clutter your desktop.

from pathlib import Path

workspace = Path("workspace_files")
workspace.mkdir(exist_ok=True)
file_path = workspace / "notes.txt"
file_path

# # 2. Create a file
# - There are two common ways to “create”:
# - `w` (write): creates the file if it doesn’t exist; overwrites if it does.
# - `x` (exclusive create): creates the file only if it doesn’t exist; errors if it does (safer if you don’t want to overwrite by mistake).
# - Use `w` when you’re okay with replacing old content; use `x` when you want to avoid accidental overwrites

# # (A) Create or overwrite using 'w'
# f = open(file_path, "w", encoding="utf-8")
# f.write("This is the first line in notes.txt\n")
# f.close()

# # (B) Safe-create using 'x' (uncomment to try once)
# f = open(workspace / "created_once.txt", "x", encoding="utf-8")
# f.write("This file will only be created if it doesn't exist.\n")
# f.close()

# 3. Open a file
# Opening a file prepares it for reading or writing.

# # Opening for writing again (this will overwrite!)
# f = open(file_path, "w", encoding="utf-8")
# f.write("Replaced the old content with this line.\n")
# f.close()

# Note: If you only want to add new content, don’t use 'w' — use 'a' (append).

# 4. Write to a file 
# Writing puts text into a file. write() does not add newlines automatically (you add\n yourself).

# f = open(file_path, "w", encoding="utf-8")
# f.write("Shopping List: \n")
# f.write(" - Rice\n")
# f.write(" - Beans\n")
# f.write(" - Garri\n")
# f.close()

# # 5. Append to a file
# # Append adds to tghe end without deleting what's already there.

# f = open(file_path, "a", encoding="utf-8")
# f.write(" - Groundut oil\n")
# f.write(" - Maggi\n")
# f.close()

# 6. Read from a file
# There are four common ways:
#   - read() - whole file as one string
#   - read(n)  - first n characters
#   - readline()  - one line
#   - readlines()  - list of all lines

# Read the whole file 
f = open(file_path, "r", encoding="utf-8")
content = f.read()
f.close()
print(content)

# Read Line by line
f = open(file_path, "r", encoding="utf-8")
print("First line:", f.readline().rstrip())
print("Second line:", f.readline().rstrip())
f.close()

# Read as a list of lines
f = open(file_path, "r", encoding="utf-8")
lines = f.readlines()
f.close()
print("Lines list:", [line.rstrip() for line in lines])

# Iterate over lines (memory-friendly)
f = open(file_path, "r", encoding="utf-8")
for line in f:
    print("->", line.rstrip())
f.close()

# # 7. Close the file
#  - Always close files opened with open(...).
#  - It flushes (saves) any buffered data to disk.
#  - It releases the OS handle so other programs can use the file.
#  - It avoids weird bugs (especially on Windows).
# You have seen f.close() above. But there’s a better way…

# 8. Use with `open(...) as f:` (best practice)
# The with statement automatically closes the file even if an error happens. This is the recommended way.

# write safely
with open(file_path, "w", encoding="utf-8") as f:
    f.write("My Todo List:\n")
    f.write(" - Revise Python file handling\n")
    f.write(" - practice error handling within a function\n")
    f.write(" - practice JSON & CSV\n")

# Append safely
with open(file_path, "a", encoding="utf-8") as f:
    f.write(" - Build a small project\n")

# Summary
# | Mode   | Meaning                       | Typical use     |
# | ------ | ----------------------------- | --------------- |
# | `'r'`  | Read (file must exist)        | Reading text    |
# | `'w'`  | Write (overwrite/create)      | Start fresh     |
# | `'a'`  | Append (create if missing)    | Add to end      |
# | `'x'`  | Create (error if exists)      | Safe create     |
# | `'b'`  | Binary (combine, e.g. `'rb'`) | Images/videos   |
# | `'t'`  | Text (default)                | Human-readable  |
# | `'r+'` | Read & write (no truncate)    | Update in place |

# More Context
# What Happens When Things Go Wrong?
# - Sometimes files don't exist, or we don't have permission to read them. Python will give us an error, 
# but we can catch and handle these errors gracefully. Let's see how to do that.

from pathlib import Path

workspace = Path("workspace_files")
workspace.mkdir(exist_ok=True)

# Try to read a file that doesn't exist
try:
    with open(workspace / "missing_file.txt", "r") as f:
        content = f.read()
        print("File content:", content)
except FileNotFoundError:
    print("Oops! That file doesn't exist yet.")
    print("Let's create it first!")
    
    # Now create the file
    with open(workspace / "missing_file.txt", "w") as f:
        f.write("Now I exist!")
    print("File created successfully!")

# # If you write this correctly, you should see something like this...
# """
# # Oops! That file doesn't exist yet.
# # Let's create it first!
# # File created successfully!

# checking If Files Exist Before Using Them
# Before trying to read or write files, 
# it's smart to check if they exist first.

from pathlib import Path

workspace = Path("workspace_files")
file_path = workspace / "notes.txt"

# Check if our file exists
if file_path.exists():
    print(f"Found the file: {file_path.name}")

# Get some information about the file
    file_size = file_path.stat().st_size
    print(f"File size: {file_size} bytes")

# Read and show  the content
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        print(f"Content preview: {content[:50]}...") # First 50 characters
else:
    print(f"File {file_path.name} doesn't exist")
    print("You might want to create it first!")

# # If notes.txt exists
# """
# Found the file: notes.txt
# File size: 143 bytes

# Content preview: Todo:
#  - Revise Python file handling
#  - Practice J...

# """

# # if notes.txt does not exist

# """
# File notes.txt doesn't exist
# You might want to create it first!

# ** Working with JSON Files (Storing Data)
# - JSON files are great for storing structured data like dictionaries and lists. 
# Think of them as a way to save Python data to a file.

import json
from pathlib import Path

workspace = Path("workspace_files")

# Create soem student data (like a mini database)
student_data = {
    "name": "Oyindamola",
    "age": 16,
    "courses": ["Python", "Data Science", "Web Development"],
    "grades": {"Python": "A", "Data Science": "B+", "Web Development": "A-"},
    "is_graduated": False
            }

# Save the data to a JSON file
json_file = workspace / "student_data.json"
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(student_data, f, indent=2)   #indent=2 makes it pretty and readable

print("student data saved to JSON file!")

# Now read it backk
with open(json_file, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print("\nData read from JSON file:")
print(f"Student name: {loaded_data['name']}")
print(f"Age: {loaded_data['age']}")
print(f"Cousres: {', '.join(loaded_data['courses'])}")
print(f"Python grade: {loaded_data['grades']['Python']}")

# ** Working with CSV Files -Spreadsheet like Data**
# - CSV files are like simple spreadsheets. 
# They are perfect for storing data in rows and columns.

import csv
from pathlib import Path

workspace = Path("workspace_files")
csv_file = workspace / "students.csv"

# Create sample student data
students = [
    ["Name", "Age", "Course", "Grade"],  # Header row
    ["Precious", 20, "Python", "A"],
    ["Favour", 22, "JavaScript", "B+"],
    ["Ore", 21, "Python", "A-"],
    ["Susan", 23, "Data Science", "A"]
]

# Write data to CSV file
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(students)  # Write all rows at once

print("Student data written to CSV file!")

# Read the CSV file back
print("\nReading CSV file:")
with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    
    for row_number, row in enumerate(reader):
        if row_number == 0:  # Header row
            print(f"Headers: {' | '.join(row)}")
            print("-" * 40)
        else:  # Data rows
            name, age, course, grade = row
            print(f"{name} ({age} years) - {course}: {grade}")

# Working with Multiple Files at once
# Sometimes you need to read from one file and write to another at the same time.

from pathlib import Path
workspace = Path("workspace_files")
input_file = workspace / "original.txt"
output_file = workspace / "processed.txt"

# Create an input file with text
sample_text = """hello world
python programming
file handling tutorial
learning is fun
"""

with open(input_file, "w", encoding="utf-8") as f:
    f.write(sample_text)

print("Created input file")
# Process the file: read from input, write processed version to output
with open(input_file, "r", encoding="utf-8") as infile, \
    open(output_file, "w", encoding="utf-8") as outfile:

    line_number = 1
    for line in infile:
        # Process each line: make it uppercase and add line numbers
        processed_line = f"Line {line_number}: {line.strip().upper()}\n"
        outfile.write(processed_line)
        line_number += 1
print("File processing complete!")

# Show the reslts
print("\nOriginal files:")
with open(input_file, "r", encoding="utf-8") as f:
    print(f.read())

print("\nProcessed file:")
with open(output_file, "r", encoding="utf-8") as f:
    print(f.read())

# Output to expect
"""
Created input file
File processing complete!

Original file:
hello world
python programming
file handling tutorial
learning is fun

Processed file:
Line 1: HELLO WORLD
Line 2: PYTHON PROGRAMMING
Line 3: FILE HANDLING TUTORIAL
Line 4: LEARNING IS FUN
"""

# ** Moving Around Inside a File
# # - Sometimes you want to jump 
# to a specific part of a file instead of reading from the beginning.

from pathlib import Path

workspace = Path("workspace_files")
file_path = workspace / "story.txt"

# Create a sample story file
story = """Once upon a time, there was a lady  who was very curious and inquisitive, 
she just want to know how things work behind the scene. 
Eventually she had an opportunity to hopp into the world of programming for the first time.
She started with python, now she codes in Python every day.
One day, she discovered file handling.
It opened up a whole new world of possibilities!
The end."""

with open(file_path, "w", encoding="utf-8") as f:
    f.write(story)

print("Created a story file!")

# Now let's explore moving around in the file
with open(file_path, "r", encoding="utf-8") as f:
    print("\nFile positioning demo:")
    
    # Read first 20 characters
    first_part = f.read(20)
    print(f"First 20 characters: '{first_part}'")
    
    # Check where we are now
    current_position = f.tell()
    print(f"Current position in file: {current_position}")
    
    # Jump to the beginning
    f.seek(0)
    print(f"After seeking to beginning: position {f.tell()}")
    
    # Jump to position 50 and read from there
    f.seek(50)
    rest_of_line = f.readline()
    print(f"Reading from position 50: '{rest_of_line.strip()}'")
    
    # Go back to beginning and read the first line
    f.seek(0)
    first_line = f.readline()
    print(f"First line: '{first_line.strip()}'")

# This should be enough, I think. 
# But before we call it a day. 
# Take note of the common mistakes made by beginners when it comes to file handling.

#   Common Beginner Mistakes to Avoid**
# - Forgetting to close files (use with statements!)
# - Not handling the case when files don't exist
# - Using the wrong file mode ('w' overwrites everything!)
# - Forgetting to specify encoding (use encoding="utf-8")
# - Not understanding the difference between 'r', 'w', and 'a' modes
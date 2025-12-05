

#Name: Saloni Pradhan
#Student ID: 201829493

import sys

# Show the number of non-empty lines in a text file
# Usage: python file_line_count.py <filename>
# Example: python file_line_count.py textexample.txt
# You must use the error messages precisely as defied below.

# filename is a command line argument 
if len(sys.argv) != 2:
    sys.exit("Usage: python file_line_count.py <filename.txt>")

file_name = str(sys.argv[1])


# Error message: "Usage: python file_line_count.py <filename.txt>"
#f = open(file_name, "r")
# Open the file and read its content
try:
# Error message: "File not found: python file_line_count.py {file_name}"

# count number of lines that are not blank  
    number_of_lines = 0

    f = open(file_name, "r")
    lines = f.readlines()

    for line in lines:
        if line.strip() != "":
            number_of_lines +=1

    print(f"{file_name} has {number_of_lines} lines")

# Success message: "{file_name} has {number_of_lines} lines"

# Test on the 'text_example.txt' file. The answer should be 4.
except FileNotFoundError: 

    sys.exit(f"File not found: python file_line_count.py {file_name}")
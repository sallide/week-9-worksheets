
# Name: 
# Username: 

import sys
import pandas as pd

# Show the number of non-empty lines in a text file
# Usage: python file_line_count.py <filename>
# Example: python file_line_count.py textexample.txt
# You must use the error messages precisely as defied below.

# filename is a command line argument 
file_name = str(sys.argv[1])
if len(sys.argv) != 2:
    sys.exit("Usage: python file_line_count.py <filename.txt>")
#file_name = file_name[1]

# Error message: "Usage: python file_line_count.py <filename.txt>"
#f = open(file_name, "r")
# Open the file and read its content
try:
# Error message: "File not found: python file_line_count.py {file_name}"

# count number of lines that are not blank  
    number_of_lines = 0
    number_of_lines = pd.read_csv(file_name)
 

    number_of_lines = (len(number_of_lines)+1)

    print(f"{file_name} has {number_of_lines} lines")
# success - report the number of lines


# Success message: "{file_name} has {number_of_lines} lines"

# Test on the 'text_example.txt' file. The answer should be 4.
except: 

    sys.exit(f"File not found: python file_line_count.py {file_name}")
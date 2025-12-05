
#Name: Saloni Pradhan
#Student ID: 201829493

# Lists contents of a zip archive
# usage: python ziplist.py <zipfile>
# eg. python ziplist.py testdir/test.zip
# You must use the error messages precisely as defined below.

# Hint: look at the documentation for the "zipfile" module

import sys
#from zipfile import ...   # tools in this module can be used
import zipfile
# filename is a command line argument 
file_name = ""

# Error message: "Usage: python ziplist.py <filename.zip>"
if len(sys.argv) != 2:
    sys.exit(f"Usage: python ziplist.py <file.zip>") 

file_name = str(sys.argv[1])

# Error message: "File not found: python ziplist.py {file_name}"

# Error message: "Bad zip file: python ziplist.py {file_name}"
# Hint: There is an exception for this defined in the zipfile module

# Use zipfile methods to list the contents of the zip file.
# Test your script on the zip_example.zip file. The response should be:
# README.md
# cmd_line.py
# find_file.py
# password.py
# rockpaperscissors.py

try:

    zip = zipfile.ZipFile(file_name)

    print(zip.namelist())



except FileNotFoundError: 

    sys.exit(f"File not found: python ziplist.py {file_name}")

except zipfile.BadZipFile:
    print(f"Bad zip file: python ziplist.py {file_name}", file=sys.stderr)




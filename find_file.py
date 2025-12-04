import os
import sys

my_string = sys.argv[1]

basedir = os.getcwd()

for subdir, dirs, files in os.walk(basedir):
    for file in files:
        if my_string in file:
            filepath = f"{subdir}{os.sep}{file}"
            print (filepath)
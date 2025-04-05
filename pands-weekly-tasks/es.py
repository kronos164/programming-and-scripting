import os
import sys

if len(sys.argv) > 1: # Check if a filename was provided
    file = os.path.join(sys.argv[1]) # Get the filename
    try:
        with open(file, "r", encoding="utf-8") as f: # Open and encode the file
            count = 0
            # Count the number of 'e's in the file
            for line in f:
                for char in line:
                    if char == "e":
                        count += 1
            print(count)
    # Handle file not found error
    except FileNotFoundError:
        print(f"File not found: {file}")
else:
    # Print how to use message
    print("Usage: python es.py <filename>")
    
# How to run:
# Go to the directory where the file is located and run the following command:
#       python es.py crime-and-punishment.txt
#       python es.py <filename> | in case you want to check another file
    
# References:
# https://realpython.com/python-command-line-arguments/
# https://realpython.com/read-write-files-python/
# https://docs.python.org/3/library/exceptions.html#FileNotFoundError
# https://docs.python.org/3/library/os.path.html
# https://docs.python.org/3/library/sys.html
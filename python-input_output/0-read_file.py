#!/usr/bin/python3
"""Function to read a text file and print it"""


def read_file(filename=""):
    """Function to read a file"""

    with open(filename, "r") as f:
        read_f = f.read()
        print(read_f)

#!/usr/bin/python3
"""Class MyList with an inheritance for the class list"""


class MyList(list):
    """Class MyList taking inheritance from list"""
    def print_sorted(self):
        """Method to print a sorted list"""
        sorted_list = sorted(self)
        print("{}".format(sorted_list))

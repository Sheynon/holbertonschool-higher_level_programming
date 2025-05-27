#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        sorted_list = sorted(self)
        print("{}".format(sorted_list))

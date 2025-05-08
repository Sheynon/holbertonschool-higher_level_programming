#!/usr/bin/python3
for i in range(99):
    print(f"{i} = {hex(i)}", end="\n" if i == 98 else " ")

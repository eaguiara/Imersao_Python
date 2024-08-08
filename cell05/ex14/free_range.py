#!/usr/bin/env python3
import sys

args = sys.argv[1:]

list = []

if len(args) != 2:
    print("none")
else:
    number_1 = int(args[0])
    number_2 = int(args[1])   
    x = range(number_1, number_2 + 1)
    for i in x:
        list.append(i)
    print(list)     
#!/usr/bin/env python3

import sys

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    user_input = args[0]
    parameter = input("What was the parameter? ")

    if parameter == user_input:
        print("Good job!")
    else:
        print("Nope, sorry...")
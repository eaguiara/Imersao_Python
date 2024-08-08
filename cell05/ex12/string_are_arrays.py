#!/usr/bin/env python3
import sys

def verificaUnicoCaracter(user_input):
    i = 0
    if user_input.count("z") == 1 and len(user_input) == 1:
        print(user_input)
        sys.exit(0)
    elif user_input.count("z") > 1:
        z = user_input.count("z")
        while i < z:
            print("z", end="")
            i += 1
    else:
        print("none")

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    user_input = args[0]
    verificaUnicoCaracter(user_input)
    
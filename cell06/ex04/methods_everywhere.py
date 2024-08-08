#!/usr/bin/env python3

import sys

args = sys.argv[1:]

def shrink(user_input):
    first_output = user_input[slice(0, 8)]
    print(first_output)

def enlarge(user_input):
    nova_palavra = user_input
    if len(user_input) < 8:
        for x in range(8 - len(user_input)):
            nova_palavra = nova_palavra + "Z"
    print(nova_palavra)


if len(args) < 1:
    print("none")
else:
    for x in args:
     if len(x) > 8:
         shrink(x)
     else:
         enlarge(x)    
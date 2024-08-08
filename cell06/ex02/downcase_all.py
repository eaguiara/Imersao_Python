#!/usr/bin/env python3
import sys

args = sys.argv[1:]

def downcase_it(user_input):
    for x in user_input:
     print(f"{x.lower()}")

if len(args) == 0:
    print("none")
else:
    user_input = args
    downcase_it(user_input)


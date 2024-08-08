#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) != 0:
    print("none")
else:
    i = 0
    j = 0
    while i <= 10:
        print(f"Table de {i}:", end="")

        while j <= 10:
            print(f" {i * j}", end="")
            j += 1
        i += 1
        j = 0
        print()   
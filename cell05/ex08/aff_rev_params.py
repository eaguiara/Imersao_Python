#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) <= 2:
     print("none")
else:
    args.reverse()
    for x in args:
      print(x)
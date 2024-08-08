#!/usr/bin/env python3
import sys
import re

args = sys.argv[1:]

if len(args) != 2:
    print("none")
else:
    keyword = args[0]
    text = args[1]
    count = len(re.findall(keyword, text))
    if count > 0:
        print(count)
    else:
        print("none")
#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
   for x in args:
       if x.endswith("ism"):
           continue
       else:
           print(x + "ism")

        #    count = len(re.findall(keyword, text))
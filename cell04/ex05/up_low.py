#!/usr/bin/env python3

input_value = input("")

modified_string = ""

for i in list(input_value):
    if str(i).islower():
      modified_string += str(i).upper()
    else:
      modified_string +=str(i).lower()

print(modified_string)

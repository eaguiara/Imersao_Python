#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]
print("[2, 8, 9, 48, 8, 22, -12, 2]")
new_array = []
filtered_array = []

for i in array:
    if i >= 5:  
        filtered_array.append(i)

for x in filtered_array:
    x+=2
    new_array.append(x)   

print(new_array)

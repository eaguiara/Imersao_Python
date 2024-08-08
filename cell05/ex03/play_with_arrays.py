#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

print(original_array)

# Create a copy of the original array
copy_array = []

for x in original_array:
    if x >= 5:
        copy_array.append(x)

for x in copy_array:
    x += 2
    new_array.append(x)
    
new_array2 = list(set(new_array))

print(new_array2)

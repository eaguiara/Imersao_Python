#!/usr/bin/env python3

number_1 = int(input("Give me the first number: "))
number_2 = int(input("Give me the second number: "))
print("Thank you!")

operadores= ["+", "-", "//", "*"]

for i in operadores:
    result = eval(str(number_1) + i + str(number_2))
    if i == "//":
     i ="/"   
    else:
        i = i
    print(f"{number_1} {i} {number_2} = {result}")
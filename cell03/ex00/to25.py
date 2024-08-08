#!/usr/bin/env python3

user_number = int(input("Enter a number less than 25: \n"))

if user_number > 25:
    print("Error")

i = user_number
while i <= 25:
 print(f"Inside the loop, my variable is {i}")
 i += 1
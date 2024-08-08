#!/usr/bin/env python3

def average(grades):
    
    notes = []
    total = 0

    for name, scores in grades.items():
       total += scores 
    
    media = total / len(grades)

    if(grades == class_3B):
     print(f"Average for class 3B: {media}")
    else:
        print(f"Average for class 3C: {media}")
    

class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}

class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}

average(class_3B)
average(class_3C)


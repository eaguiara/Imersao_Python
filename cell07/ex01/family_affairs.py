#!/usr/bin/env python3

def find_the_redheads(dupont_family):
    full_names = []
    for first_name, last_name in dupont_family.items():
        if last_name == "red":
         full_names.append(f"{first_name}")
        else:
            continue
    return full_names

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))
#!/usr/bin/env python3

def greetings(name):
    try:
        if name == "":
            print("Hello, noble stranger.")
        elif type(name) == str:
            print(f"Hello, {name}.")
        else:
            raise ValueError
    except ValueError:
        print("Error! It was not a name.")

greetings("Alexandra")
greetings("Wil")
greetings("")
greetings(42)
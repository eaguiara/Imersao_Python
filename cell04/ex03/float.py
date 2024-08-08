import sys

args = sys.argv[1:]

def shrink(user_input):
    first_output = user_input[:8]
    print(first_output)

def enlarge(user_input):
    if len(user_input) < 8:
        user_input += 'Z' * (8 - len(user_input))
    print(user_input)

if len(args) < 1:
    print("none")
else:
    for x in args:
        if len(x) > 8:
            shrink(x)
        else:
            enlarge(x)
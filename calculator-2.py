"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
   
    math_sequence = raw_input(">")
    
    user_input = math_sequence.split(" ")

    tokens = [user_input[0]]
    
    for i in user_input[1:]:
        tokens.append(float(i))

    if tokens[0] == 'q':
        exit()
    elif tokens[0] == "+":
        print add(tokens[1], tokens[2])
    elif tokens[0] == "-":
        print subtract(tokens[1], tokens[2])
    elif tokens[0] == "*":
        print multiply(tokens[1], tokens[2])
    elif tokens[0] == "/":
        print divide(tokens[1], tokens[2])         
    elif tokens[0] == "square":
        print square(tokens[1])
    elif tokens[0] == "cube":
        print cube(tokens[1])
    elif tokens[0] == "pow":
        print power(tokens[1], tokens[2])
    elif tokens[0] == "mod":
        print mod(tokens[1], tokens[2])
    elif tokens[0] == "x+":
        print add_mult(tokens[1], tokens[2], tokens[3])
    elif tokens[0] == "cubes+":
        print add_cubes(tokens[1], tokens[2])
    else:
        print "Invalid input. Please try again."
        continue
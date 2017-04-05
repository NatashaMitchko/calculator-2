"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

still_playing = True
while still_playing:
    user_input = raw_input('> ')
    tokenized_list = user_input.split(' ')
    if tokenized_list[0] == 'q' or tokenized_list[0] == 'quit':
        still_playing = False
    else:
        numbers_list = tokenized_list[1:]
        int_list = []
        for item in numbers_list:
            int_list.append(int(item))
        operator = tokenized_list[0]
        if operator == '+':
            print add(int_list)
        elif operator == '-':
            print subtract(int_list)
        elif operator == '*':
            print multiply(int_list)
        elif operator == '/':
            print divide(int_list)
        elif operator == 'square':
            print square(int_list)
        elif operator == 'cube':
            print cube(int_list)
        elif operator == 'pow':
            print power(int_list)
        elif operator == 'mod':
            print mod(int_list)

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
        num1 = int(tokenized_list[1])
        if len(tokenized_list) == 3:
            num2 = int(tokenized_list[2])
        operator = tokenized_list[0]
        if operator == '+':
            print add(num1, num2)
        elif operator == '-':
            print subtract(num1, num2)
        elif operator == '*':
            print multiply(num1, num2)
        elif operator == '/':
            print divide(num1, num2)
        elif operator == 'square':
            print square(num1)
        elif operator == 'cube':
            print cube(num1)
        elif operator == 'pow':
            print power(num1, num2)
        elif operator == 'mod':
            print mod(num1, num2)

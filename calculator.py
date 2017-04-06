"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


def has_spaces(user_input):
    """Checks to see if user input string contains spaces"""
    if ' ' in user_input:
        return True
    else:
        return False


def is_valid_operator(user_input):
    """Checks validity of user_input operator

    Check if first part is a valid arithmatic operator.
    """
    if has_spaces(user_input):
        operators = ['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod']
        user_input_list = user_input.split(' ')
        if user_input_list[0] in operators:
            return True
        else:
            return False
    else:
        return False


def is_valid_number(user_input):
    """Checks validity of user input numbers"""
    if has_spaces(user_input):
        user_input_list = user_input.split(' ')
        try:
            int(user_input_list[1])
            if len(user_input_list) == 3:
                try:
                    int(user_input_list[2])
                    return True
                except ValueError:
                    return False
            else:
                return True
        except ValueError:
            return False

    else:
        return False


def is_valid(user_input):
    """Checks if both operator and numbers are valid"""

    if is_valid_operator(user_input) and is_valid_number(user_input):
        return True
    else:
        return False


still_playing = True

while still_playing:
    user_input = raw_input('> ')
    if not is_valid(user_input):
        print "Input not valid. Try something like '+ 1 2' "
    else:
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

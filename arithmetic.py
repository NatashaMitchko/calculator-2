"""Math functions for calculator."""


def add(num_list):
    """Return the sum of the two input integers."""

    return num_list[0] + num_list[1]


def subtract(num_list):
    """Return the second number subtracted from the first."""

    return num_list[0] - num_list[1]


def multiply(num_list):
    """Multiply the two inputs together."""

    return num_list[0] * num_list[1]


def divide(num_list):
    """Divide the first input by the second, returning a floating point."""

    # Need to turn at least one argument to float for division to
    # not be integer division

    return float(num_list[0]) / num_list[1]


def square(num_list):
    """Return the square of the input."""

    # Needs only one argument

    return num_list[0] * num_list[0]


def cube(num_list):
    """Return the cube of the input."""

    # Needs only one argument

    return num_list[0] * num_list[0] * num_list[0]


def power(num_list):
    """Raise num_list[0] to the power of num and return the value."""

    return num_list[0] ** num_list[1]  # ** = exponent operator


def mod(num_list):
    """Return the remainder of num / num_list[1]."""

    return num_list[0] % num_list[1]

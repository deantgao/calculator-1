"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two input integers."""
    return num1 + num2


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    total = num1 - num2
    return total

def multiply(num1, num2):
    """Multiply the two inputs together."""
    total = num1 * num2
    return total


def divide(num1, num2):
    """Divide the first input by the second, returning a floating point."""
    total = num1 / num2
    return total

def square(num1):
    """Return the square of the input."""
    total = num1 * num1
    return total

def cube(num1):
    """Return the cube of the input."""
    total = num1 ** 3
    return total

def power(num1, num2):
    """Raise num1 to the power of num and return the value."""
    total = num1 ** num2
    return total

def mod(num1, num2):
    """Return the remainder of num / num2."""
    total = num1 % num2
    return total

def add_mult(num1, num2, num3):
    """Add first two numbers and multiply by the third"""
    return (num1 + num2) * num3

def add_cubes(num1, num2):
    """Cube both numbers and sum them"""
    return (num1**3) + (num2 ** 3)

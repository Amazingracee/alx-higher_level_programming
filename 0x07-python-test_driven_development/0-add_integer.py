#!/usr/bin/python3

'''Module to add two integers'''


def add_integer(a, b=98):
    '''Returns the addition of a and b
    a and b are typecasted to integers before adding them together
    Raises:
        TypeError if a and b are not integers
    '''
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))

"""A module to demonstrate exceptions."""

import sys


def convert(item):
    '''
    Convert to an integer.
    Args:
        item: some object

    Returns:
        an integer representation of the object

    Throws:
        a ValueException
    '''
    try:
        x = int(item)
        print(str.format('Conversion succeeded! x= {}', x))
    except ValueError:
        print('Conversion Failed')
        x = -1
    return x

if __name__ == '__main__':
    print(convert(sys.argv[1]))
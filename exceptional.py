"""A module to demonstrate exceptions."""

import sys


def convert(item):
    """
    Convert to an integer.
    Args:
        item: some object

    Returns:
        an integer representation of the object

    Throws:
        a ValueException
    """
    try:
        return int(item)
    except (ValueError, TypeError):
        return -1

if __name__ == '__main__':
    print(convert(sys.argv[1]))
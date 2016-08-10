"""A module to demonstrate exceptions."""

import sys

from math import log


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
    except (ValueError, TypeError) as e:
        print("Conversion Error: {}"
              .format(str(e)),
              file=sys.stderr)
        raise


def string_log(s):
    return log(convert(s))

if __name__ == '__main__':
    print(convert(sys.argv[1]))

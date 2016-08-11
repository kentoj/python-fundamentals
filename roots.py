"""Simple square roots program"""
import sys


def sqrt(x):
    """Compute square roots using the method of Heron of Alexandria.

    Args:
        x: The number to compute the square root of

    Returns:
        The square root of x.
    """

    if x < 0:
        raise ValueError("Cannot compute square root of negative number {}".format(x))
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except ValueError as e:
        print(e, file=sys.stderr)


if __name__ == '__main__':
    main()

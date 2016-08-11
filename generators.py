"""Show how generators work"""

from itertools import islice, count
from math import sqrt


def gen123():
    yield 1
    yield 2
    yield 3


g = gen123()


def gen246():
    print("About to yield 2")
    yield 2
    print("about to yield 4")
    yield 4
    print("about to yield 6")
    yield 6
    print("about to return")


h = gen246()


def take(count, iterable):
    """Take the specified number of items from the front of an iterable

    Args:
        count: The maximum number of items to retrieve.
        iterable: The source series.

    Yields:
        At most 'count' items from 'iterable'.
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def distinct(iterable):
    """Return unique items by eliminating duplicates.

    Args:
        iterable: The source series.

    Yields:
        Unique elements in order from 'iterable'.
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_take():
    items = [2, 4, 65, 8, 9]
    for item in take(3, items):
        print(item)


def run_distinct():
    items = 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 7, 8, 0, 0, 0
    for item in distinct(items):
        print(item)


def run_pipeline():
    items = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 6, 6, 6, 6, 2, 3, 6, 1, 4, 4, 1, 3, 3]
    for item in take(3, distinct(items)):
        print(item)


def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b


def run_lucas():
    for item in take(10, lucas()):
        print(item)


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


thousand_primes = islice((x for x in count() if is_prime(x)), 1000)



if __name__ == '__main__':
    run_take()
    run_distinct()
    print("pipelined")
    run_pipeline()
    print("run lucas")
    run_lucas()
    print("sum of first thousand primes", sum(thousand_primes))

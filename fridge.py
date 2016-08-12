"""Demonstrate using the open and close context manager protocol"""

from contextlib import closing


class RefrigeratorRaider:
    """Raid a refrigerator"""

    def open(self):
        print("opening fridge door")

    def take(self, food):
        print("Looking for {} in fridge...".format(food))
        if food == 'day-old potato salad':
            raise RuntimeError("Health warning!")
        print("Taking {}".format(food))

    def close(self):
        print("Closing fridge door.")


def raid(food):
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)

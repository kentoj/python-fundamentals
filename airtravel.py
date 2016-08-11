"""Model for aircraft flights"""


class Flight:
    def __init__(self, number):
        self._number = number

    def number(self):
        return self._number

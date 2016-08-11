"""Model for aircraft flights"""


class Flight:
    def __init__(self, number):
        if not number[:4].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:4].isupper():
            raise ValueError("Invalid airline code'{}'".format(number))

        if not (number[4:].isdigit() and int(number[4:]) <= 999999):
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number

    def number(self):
        return self._number

    def airline(self):
        return self._number[:4]



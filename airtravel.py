"""Model for aircraft flights"""


class Flight:
    """A flight with a specific passenger aircraft."""

    def __init__(self, number, aircraft):
        if not number[:4].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:4].isupper():
            raise ValueError("Invalid airline code'{}'".format(number))

        if not (number[4:].isdigit() and int(number[4:]) <= 999999):
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:4]

    def aircraft_model(self):
        return self._aircraft.model()

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.

        Args:
            seat: A seat designator such as '12C' or '21F'.
            passenger:

        Raises:
            ValueError: If the seat is unavailable.
        """
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {} for this flight. Valid letters: {}".format(letter, seat_letters))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in rows:
            raise ValueError("invalid row number {} for this flight. Valid row nubmers: {}".format(row, list(rows)))

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied by {}".format(seat, self._seating[row][letter]))

        self._seating[row][letter] = passenger


class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJKLMNOP"[:self._num_seats_per_row])

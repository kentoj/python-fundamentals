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

    def _parse_seat(self, seat):
        """Parse a seat designator into a valid row and letter

        Args:
            seat: A seat designator such as 11B

        Returns:
            A tuple containing an integer and a string for row and seat.
        """
        row_numbers, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {} for this flight. Valid letters: {}".format(letter, seat_letters))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in row_numbers:
            raise ValueError(
                "invalid row number {} for this flight. Valid row nubmers: {}".format(row, list(row_numbers)))

        return row, letter

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.

        Args:
            seat: A seat designator such as '12C' or '21F'.
            passenger:

        Raises:
            ValueError: If the seat is unavailable.
        """

        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied by {}".format(seat, self._seating[row][letter]))
        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate passenger to a different seat

        Args:
            from_seat: The existing seat designator for the passenger to be moved.
            to_seat: The new seat designator.
        """

        from_row, from_letter = self._parse_seat(from_seat)
        to_row, to_letter = self._parse_seat(to_seat)

        if self._seating[from_row][from_letter] is None:
            raise ValueError("Seat {} has nobody to relocate".format(from_seat))

        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} already occupied by {}".format(to_seat, self._seating[to_row][to_letter]))
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        """An iterable series of passenger seating allocations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row, letter))


class AirbusA319:
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def model(self):
        return "Airbus 319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing777:
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def model(self):
        return "Boeing777"

    def seating_plan(self):
        return range(1, 56), "ABCDEFGHJK"


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}" \
             "  Flight: {1}" \
             "  Seat: {2}" \
             "  Aircraft: {3}" \
             " |".format(passenger, flight_number, seat, aircraft)
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()


def make_flights():
    f = Flight("MSJJ26513", Boeing777("G_EUYT"))
    f.allocate_seat("1A", "Larry")
    f.allocate_seat("1B", "Lonnie")
    f.allocate_seat("1C", "Richard")

    g = Flight("MSJJ26513", AirbusA319("G_EUYT"))
    g.allocate_seat("1A", "Sally")
    g.allocate_seat("1B", "Sammie")
    g.allocate_seat("1C", "Sigurd")
    return f, g

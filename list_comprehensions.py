"""Show how to use list comprehensions and zip"""

sunday_temps = [76, 78, 86, 54, 88, 77, 66, 55, 44, 57, 58, 58, 78, 79, 69, 65]
monday_temps = [68, 67, 68, 76, 77, 66, 61, 81, 73, 61, 83, 67, 89, 78, 67, 85]
tuesday_temps = [78, 79, 70, 76, 75, 74, 73, 72, 63, 64, 65, 58, 59, 85, 59, 85]


def show_temp_tuples():
    for item in zip(sunday_temps, monday_temps):
        print(item)
    for sunday, monday in zip(sunday_temps, monday_temps):
        print("Sunday: {}, Monday: {}, Average:{}".format(sunday, monday, (sunday + monday) / 2))
    for temps in zip(sunday_temps, monday_temps, tuesday_temps):
        print("min={:4.1f}, max={:4.1f}, average={:4.1f}"
              .format(min(temps), max(temps), sum(temps) / len(temps)))


if __name__ == '__main__':
    show_temp_tuples()

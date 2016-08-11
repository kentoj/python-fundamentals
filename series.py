"""Read and print an integer series."""

import sys


def read_series(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    series = []
    for line in f:
        a = int(line.strip())
        series.append(a)
    f.close()
    return series


def main(filename):
    print(read_series(filename))


if __name__ == '__main__':
    main(sys.argv[1])

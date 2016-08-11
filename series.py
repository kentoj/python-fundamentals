"""Read and print an integer series."""

import sys


def read_series(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]


def main(filename):
    print(read_series(filename))


if __name__ == '__main__':
    main(sys.argv[1])

#!/usr/bin/env python3

""" Given a sequence of characters: return the number of A. C, T, and G's"""

import sys


def main():

    fName = sys.argv[1]

    data = ""

    with open(fName, "r") as dataSet:
        for line in dataSet:
            data += line

    (A, C, T, G) = (0, 0, 0, 0)

    for base in data:
        if (base == 'A'):
            A += 1
        if (base == 'C'):
            C += 1
        if (base == 'T'):
            T += 1
        if (base == 'G'):
            G += 1

    print('{} {} {} {}'.format(A, C, G, T))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

""" Given a string: return the number of 'A', 'T, 'C', and 'G's"""

import argparse


def main():

    # Get file name from "$ ./scriptName filename"
    parser = argparse.ArgumentParser()
    parser.add_argument("fileName", type=str)
    args = parser.parse_args()

    data = ""
    with open(args.fileName, "r") as thisFile:
        for line in thisFile:
            data += "".join(line.rstrip())

    A = 0
    C = 0
    T = 0
    G = 0

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

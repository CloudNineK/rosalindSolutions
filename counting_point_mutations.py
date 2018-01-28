#!/usr/bin/env python3

""" Calculate the Hamming distance between strings"""

import sys


def main():

    fName = sys.argv[1]
    hamming = 0

    with open(fName, 'r') as f:
        s = [k.strip() for k in f]

        for k in range(len(s[0])):
            if s[0][k] != s[1][k]:
                hamming += 1

    print(hamming)


if __name__ == "__main__":
    main()

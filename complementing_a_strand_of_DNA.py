#!/usr/bin/env python3

""" Output the complement a strand of DNA"""

import sys


def main():

    fName = sys.argv[1]

    output = ""
    with open(fName, 'r') as f:
        for line in f:
            for char in line.rstrip('\n'):
                if char == 'A':
                    output = 'T' + output

                elif char == 'T':
                    output = 'A' + output

                elif char == 'C':
                    output = 'G' + output

                elif char == 'G':
                    output = 'C' + output

    print(output)

if __name__ == "__main__":
    main()

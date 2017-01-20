#!/usr/bin/env python3

""" Convert 'A' in string to 'U'"""

import sys


def main():

    fName = sys.argv[1]

    output = ""
    with open(fName, 'r') as f:
        for line in f:
            for char in line.rstrip('\n'):
                if char == 'T':
                    output += 'U'
                else:
                    output += char

    print(output)

if __name__ == "__main__":
    main()

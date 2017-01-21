#!/usr/bin/env python3

""" Given:  At most 10 DNA strings in FASTA format

    Return: The ID of the string having the highest GC-content, followed by
            the GC-content of that string.
"""

import sys
import collections


def main():

    fName = sys.argv[1]
    output = collections.OrderedDict()

    with open(fName, 'r') as f:

        # Iterate over lines in FASTA
        # Build a dictionary containing sequences and their labels as keys
        key = ''
        for line in f:
            # Save lebel lines as keys for dictionary
            if line[0] == '>':
                key = line.rstrip('\n')[1:]

            # Save sequence as value
            elif key not in output:
                output[key] = line.rstrip('\n')

            # For multiline FASTA build sequence
            else:
                output[key] = output[key] + line.rstrip('\n')

    # Calculate GC content
    for key in output.keys():
        count = 0

        # Iterate over nucleotides and count G and C
        for char in output[key]:
            if char == 'G' or char == 'C':
                count += 1

        output[key] = (count / len(output[key])) * 100

    # Build output string
    outString = ''
    for key in output.keys():
        outString += key + '\n'
        outString += '{:f}'.format(output[key]) + '\n'

    # Strip Trailing newline character
    outString.rstrip('\n')

    print(outString)


if __name__ == "__main__":
    main()

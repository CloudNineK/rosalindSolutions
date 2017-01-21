#!/usr/bin/env python3

""" Given:  At most 10 DNA strings in FASTA format

    Return: The ID of the string having the highest GC-content, followed by
            the GC-content of that string.
"""

import sys


def main():

    fName = sys.argv[1]
    output = {}

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
    max = 0
    maxKey = ''
    for key in output.keys():
        count = 0

        # Iterate over nucleotides and count G and C
        for char in output[key]:
            if char == 'G' or char == 'C':
                count += 1

        GC = (count / len(output[key])) * 100
        if GC > max:
            max = GC
            maxKey = key

    # Build output string
    outString = ''
    outString += maxKey + '\n'
    outString += '{:f}'.format(max)

    print(outString)


if __name__ == "__main__":
    main()

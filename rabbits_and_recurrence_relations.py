#!/usr/bin/env python3

""" Given: n <= 40 and k <= 5
    Output: The number of rabbit pairs present after n months with a k litter
"""

import sys


def main():

    n, k = (int(sys.argv[1]), int(sys.argv[2]))
    n = n-1

    r = [0, 1]  # (mature, immature)

    for month in range(n):
        matured = r[1]
        progeny = r[0] * k
        r[0] = r[0] + matured  # add immature to mature rabbits
        r[1] = progeny  # update immature rabbits

    print(r[0] + r[1])


if __name__ == "__main__":
    main()

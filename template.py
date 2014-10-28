#!/usr/bin/python3

import sys

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_.txt"
    with open(filename) as stream:

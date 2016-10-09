#!/usr/bin/python3

import sys

def count_rabbits(months, litter, unmature, mature):
    '''Returns the number of rabbits after "months" months, if each pair has a litter of
    "litter" pairs, and every rabbit achieves maturity after 1 month'''
    if months == 1:
        return unmature + mature
    return count_rabbits(months - 1,             # reduce one month
                  litter,                        # litter per pair remains constant
                  mature * litter,               # newborns
                  mature + unmature)             # already mature rabbits + new mature rabbits


if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else 'rosalind_fib.txt'
    with open(filename) as stream:
        inputs = stream.read().split(' ')
        print(count_rabbits(int(inputs[0]), int(inputs[1]), 1, 0))

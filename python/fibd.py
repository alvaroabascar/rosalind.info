#!/usr/bin/python3

import sys

def count_rabbits(months, life_expect, rabbits = None):
    '''Returns the number of rabbits after "months" months, if each pair has a litter of
    1 pair, every rabbit dies after life_expect and every rabbit achieves maturity after
    1 month'''
    if rabbits == None:
        rabbits = [0 for i in range(life_expect)]
        rabbits[0] = 1                              # num of rabbits of age 0 months
    if months == 1:
        return sum(rabbits)
    actives = sum(rabbits[1:])                      # number of active rabbits
    for i in range(1, life_expect):
        rabbits[-i] = rabbits[-i - 1]
    rabbits[0] = actives 
    return count_rabbits(months - 1, life_expect, rabbits)

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else 'rosalind_fibd.txt'
    with open(filename) as stream:
        inputs = stream.read().split(' ')
        print(count_rabbits(int(inputs[0]), int(inputs[1])))

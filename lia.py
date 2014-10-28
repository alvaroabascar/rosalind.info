#!/usr/bin/python3

import sys
import math

def bin_coeff(m, n):
    '''Return binomial coefficient m / n'''
    return math.factorial(m) / (math.factorial(n) * math.factorial(m-n))


def probs(k, N):
    probs_none = 0
    orgs = 2**k
    for i in range(N):
        prob = bin_coeff(orgs, i) * 0.25**i * 0.75**(orgs - i)
        probs_none += prob
    return 1 - probs_none




if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_lia.txt"
    with open(filename) as stream:
        print(probs(*[int(i) for i in stream.read().strip().split()]))

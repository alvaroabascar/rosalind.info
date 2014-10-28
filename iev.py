#!/usr/bin/python3

import sys

def exp_dom_offspring(couples):
    '''couples = list of couples [AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa,
       aa-aa]
       returns the expected number of dominant offspring, given that
       each couple has two offspring'''
    AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa = couples
    expected = AA_AA * 2 +\
               AA_Aa * 2 +\
               AA_aa * 2 +\
               Aa_Aa * 0.75 * 2 +\
               Aa_aa * 0.5 * 2
    return expected
              

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_iev.txt"
    with open(filename) as stream:
        couples = [int(i) for i in stream.read().strip().split(' ')]
        print(exp_dom_offspring(couples))

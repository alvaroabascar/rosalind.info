#!/usr/bin/python3

import sys

def long_inc_subs(perm):
    '''Given a permutation list, returns the largest increasing
    subsequence'''
    if len(perm) == 1:
        return perm
    longest_subseq = []
    l = len(perm)
    for i in range(l):
        subseq = []
        subseq.append(perm[i])
        for j in range(i+1, l):
            if perm[j] > subseq[-1] and len(subseq) + 1 >=\
                        len(subseq)+len(long_inc_subs(perm[j+1:])):
               subseq.append(perm[j])
        if len(subseq) > len(longest_subseq):
            longest_subseq = subseq
    return longest_subseq


if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_lgis.txt"
    with open(filename) as stream:
        lines = [line.strip() for line in stream.readlines()]
        n = int(lines[0])
        permutation = [int(i) for i in lines[1].split(' ')]
        
        inc = long_inc_subs(permutation)
        permutation.reverse()
        dec = long_inc_subs(permutation)
        dec.reverse()
        print(' '.join([str(i) for i in inc]))
        print(' '.join([str(i) for i in dec]))

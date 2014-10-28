#!/usr/bin/python3

import sys

def count_nucleotides(seq):
    '''Return the number of A C G T in seq (a string)'''
    return (seq.count('A'), seq.count('C'), seq.count('G'), seq.count('T'))

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_dna.txt"
    with open(filename) as stream:
        print(' '.join([str(i) for i in count_nucleotides(stream.read())]))
	

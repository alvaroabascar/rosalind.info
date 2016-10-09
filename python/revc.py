#!/usr/bin/python3

import sys

def reverse_complement(DNAseq):
    '''Return the complementary and reversed sequence of DNAseq'''
    RNAseq = []
    for nucleotide in DNAseq:

        if nucleotide == 'A':
            RNAseq.append('T')

        elif nucleotide == 'T':
            RNAseq.append('A')

        elif nucleotide == 'C':
            RNAseq.append('G')

        elif nucleotide == 'G':
            RNAseq.append('C')

    RNAseq.reverse()
    return ''.join(RNAseq)

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_revc.txt"
    with open(filename) as stream:
        print(reverse_complement(stream.read()))

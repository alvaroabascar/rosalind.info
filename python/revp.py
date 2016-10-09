#!/usr/bin/python3

import sys
import re
import GenLib

def reverse_palindromes(DNAseq, min = 4, max = 12):
    '''Given a DNA strand, find all its palindromes'''
    l = len(DNAseq)
    revcomp = GenLib.reverse_complement(DNAseq)
    rev_pals = []
    for rp_len in range(min, max + 1):
        for offset in range(0, l - rp_len + 1):
            if DNAseq[offset:offset + rp_len] ==\
               revcomp[l - (offset + rp_len): l - offset]:
               rev_pals.append((offset + 1, rp_len))
    return rev_pals



if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_revp.txt"
    with open(filename) as stream:
        seq = re.findall(r'>\w+?\n([ATCG\s]+)', stream.read())[0]
        seq = seq.replace('\n', '')
        result = reverse_palindromes(seq, min = 4, max = 12)
        result.sort(key = (lambda x: x[0]))
        print('\n'.join([' '.join([str(i) for i in pair]) for pair in result]))

#!/usr/bin/python3

import sys
import re
import GenLib

def remove_introns(seq, introns):
    for intron in introns:
        seq = seq.replace(intron, '')
    return seq

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_splc.txt"
    with open(filename) as stream:
        seqs = re.findall(r'>[\w\s]+?([ATCG\s]+)', stream.read())
        seqs = [seq.replace('\n', '') for seq in seqs]
        print(GenLib.DNA_to_prot(remove_introns(seqs[0], seqs[1:])))

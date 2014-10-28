#!/usr/bin/python3

import sys
import GenLib

def total_weight(Protseq):
    '''Given a protein sequence, return the total monoisotopic weight'''
    ws = [GenLib.monoisotopic_mass[aa] for aa in Protseq]
    return sum(ws)

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_prtm.txt"
    with open(filename) as stream:
        print(total_weight(stream.read().strip()))

#!/usr/bin/python3

import sys

def num_rnas(Protseq):
    genetic_code =\
        [('UUU', 'F'), 
         ('UUC', 'F'), 
         ('UUA', 'L'), 
         ('UUG', 'L'), 
         ('UCU', 'S'), 
         ('UCC', 'S'), 
         ('UCA', 'S'), 
         ('UCG', 'S'), 
         ('UAU', 'Y'), 
         ('UAC', 'Y'), 
         ('UAA', 'Stop'),
         ('UAG', 'Stop'),
         ('UGU', 'C'),
         ('UGC', 'C'), 
         ('UGA', 'Stop'),
         ('UGG', 'W'), 
         ('CUU', 'L'),
         ('CUC', 'L'),
         ('CUA', 'L'),
         ('CUG', 'L'),
         ('CCU', 'P'),
         ('CCC', 'P'),
         ('CCA', 'P'),
         ('CCG', 'P'),
         ('CAU', 'H'),
         ('CAC', 'H'),
         ('CAA', 'Q'),
         ('CAG', 'Q'),
         ('CGU', 'R'),
         ('CGC', 'R'),
         ('CGA', 'R'),
         ('CGG', 'R'),
         ('AUU', 'I'),
         ('AUC', 'I'),
         ('AUA', 'I'),
         ('AUG', 'M'),
         ('ACU', 'T'),
         ('ACC', 'T'),
         ('ACA', 'T'),
         ('ACG', 'T'),
         ('AAU', 'N'),
         ('AAC', 'N'),
         ('AAA', 'K'),
         ('AAG', 'K'),
         ('AGU', 'S'),
         ('AGC', 'S'),
         ('AGA', 'R'),
         ('AGG', 'R'),
         ('GUU', 'V'),
         ('GUC', 'V'),
         ('GUA', 'V'),
         ('GUG', 'V'),
         ('GCU', 'A'),
         ('GCC', 'A'),
         ('GCA', 'A'),
         ('GCG', 'A'),
         ('GAU', 'D'),
         ('GAC', 'D'),
         ('GAA', 'E'),
         ('GAG', 'E'),
         ('GGU', 'G'),
         ('GGC', 'G'),
         ('GGA', 'G'),
         ('GGG', 'G')]
    deg = {}
    aas = [x[1] for x in genetic_code]
    for aa in aas:
        if aa in deg:
            deg[aa] += 1
        else:
            deg[aa] = 1
    result = 1 
    for aa in Protseq:
        result *= deg[aa]
        if result > 1e6:
            result %= 1000000
    result *= deg['Stop']
    return result % 1000000

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_mrna.txt"
    with open(filename) as stream:
        print(num_rnas(stream.read().strip()))

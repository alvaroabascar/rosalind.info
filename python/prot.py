#!/usr/bin/python3

import sys

def rna_to_prot(RNAseq):
    genetic_code = dict(
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
         ('GGG', 'G')])
    prot = []
    for i in range(0, len(RNAseq) - 3, 3):
        codon = RNAseq[i:i+3]
        if codon != 'Stop':
            prot.append(genetic_code[codon])
    return ''.join(prot)



if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_prot.txt"
    with open(filename) as stream:
        print(rna_to_prot(stream.read().strip()))

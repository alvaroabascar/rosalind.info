#!/usr/bin/python3

import sys
import re
import GenLib

def orfs(DNAseq):
    '''Given a DNA sequence, returns the transcriptions of every ORF'''
    orfs = list(set(GenLib.find_orfs(DNAseq))) # to remove repetitions
    orfs_seqs = [GenLib.DNA_to_prot(orf) for orf in orfs]
    return orfs_seqs

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_orf.txt"
    with open(filename) as stream:
        seq = re.findall(r'>[\w\s]+?\n([ACGT\s]+)', stream.read())
        seq = seq[0].replace('\n', '')
        print('\n'.join(orfs(seq)))
        

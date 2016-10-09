#!/usr/bin/python3

import sys

def transcribe(DNAseq):
    '''Transcribe a DNA sequence into a RNA sequence (just replacing T with U)'''
    return DNAseq.replace('T', 'U')



if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_rna.txt"
    with open(filename) as stream:
        print(transcribe(stream.read()))

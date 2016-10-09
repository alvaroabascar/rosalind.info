#!/usr/bin/python3

import sys
import re

def gc(seq):
    return (seq.count('C') + seq.count('G')) / float(len(seq)) * 100

def highest_gc(seqs):
    '''Given a dict name->sequence, returns the name and GC content of the sequence with the
    highest GC content'''
    max_gc = max(seqs.items(), key = (lambda x: gc(x[-1])))
    return (max_gc[0], str(gc(max_gc[1])))

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_gc.txt"
    with open(filename) as stream:
        seqs = re.findall(r'>(\w+)\s([ATCG\s]+)', stream.read())
        seqs = [(a, b.replace('\n', '')) for a, b in seqs] # remove newlines in seqs
        print('\n'.join(highest_gc(dict(seqs))))

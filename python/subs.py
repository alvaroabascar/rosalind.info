#!/usr/bin/python3

import sys

def subs(seq, subseq):
    locations = []
    i = seq.find(subseq, 0)
    while i != -1:
        locations.append(i + 1)
        i += 1
        i = seq.find(subseq, i)
    return locations



if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_subs.txt"
    with open(filename) as stream:
        seqs = [line.strip() for line in stream.readlines()]
        print(' '.join([str(l) for l in subs(seqs[0], seqs[1])]))

#!/usr/bin/python3

import sys

def Hamming_distance(seq, seq2):
    distance = 0
    for n, n2 in zip(seq, seq2):
        if n != n2:
            distance += 1
    return distance


if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_hamm.txt"
    with open(filename) as stream:
        seqs = [line.strip() for line in stream.readlines()]
        print(Hamming_distance(seqs[0], seqs[1]))

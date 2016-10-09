#!/usr/bin/python3

import sys
import re

def profile_matrix(seqs):
    '''Given a list of sequences, returns the profile matrix as a
    dictionary {'A': [5 1 0 0 ..], 'T': [0 0 3 5], 'C': etc.}'''
    prof_matrix = {'A': [], 'C': [], 'G': [], 'T': []}
    for Ns in zip(*seqs):
        for N in ['A', 'C', 'G', 'T']:
            prof_matrix[N].append(Ns.count(N))
    return prof_matrix

def consensus_string(profile_matrix):
    '''Given a profile matrix, returns a consensus string'''
    consensus = ''
    items = tuple(profile_matrix.items())
    length = len(items[0][1])
    for i in range(length):
        consensus += max(items, key = (lambda x: x[1][i]))[0]
    return consensus

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_cons.txt"
    with open(filename) as stream:
        seqs = re.findall(r'>\w+\n([ATCG\s]+)', stream.read())
        seqs = [seq.replace('\n', '') for seq in seqs]
        #print(len(seqs))
        #print('\n'.join(seqs))
        #exit(0)
        prof_matrix = profile_matrix(seqs)
        print(consensus_string(prof_matrix))
        for N in ['A', 'C', 'G', 'T']:
            print(N + ':', ' '.join([str(i) for i in prof_matrix[N]]))

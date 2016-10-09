#!/usr/bin/python3

import sys
import re

def grph(seqs, k = 3):
    adjacency_list = []
    for name, seq in seqs.items():
        for name2, seq2 in seqs.items():
            if name == name2 or seq == seq2:
                continue
            if seq[-k:] == seq2[:k]:
                adjacency_list.append((name, name2))
    return adjacency_list 
    
    

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_grph.txt"
    with open(filename) as stream:
        inputs = re.findall(r'>(\w+)\n([ATCG\s]+)', stream.read())
        inputs = [(name, seq.replace('\n', '')) for name, seq in inputs]
        sequences = dict(inputs)
        print('\n'.join([' '.join(dir_graph) for dir_graph in grph(sequences)]))

#!/usr/bin/python3

import sys
import urllib.request
import re

def retrieve_prot_seq(prot_id):
    f = urllib.request.urlopen('http://www.uniprot.org/uniprot/' +\
                               prot_id + '.fasta')
    seq = re.findall(r'>[\w\W]+?\n([\w\s]+)', f.read().decode('utf-8'))
    seq = seq[0].replace('\n', '')
    return seq

def find_motif(prot_seq, motif):
    result = [str(m.start() + 1) for m in re.finditer(motif, prot_seq)]
    return result

def N_glyc_motif_vect(dataset):
    motif = re.compile('(?=(N[^P][ST][^P]))')
    result = [(prot_id, find_motif(retrieve_prot_seq(prot_id), motif))
                for prot_id in dataset]
    return [r for r in result if r[1]]

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_mprt.txt"
    with open(filename) as stream:
        dataset = [line.strip() for line in stream.readlines()]
        results = N_glyc_motif_vect(dataset)
        print('\n'.join(['\n'.join(
            (ID, ' '.join(locs))) for ID, locs in results]))

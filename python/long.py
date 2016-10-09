#!/usr/bin/python3

import sys
import re

def merge(seq1, seq2):
    '''Merge two sequences if they overlap by more than half their length,
    return None otherwise'''
    if seq1 in seq2:
        return seq2
    if seq2 in seq1:
        return seq1
    l1 = len(seq1)
    l2 = len(seq2)
    shrt_len = min(l1, l2)
    lng_len = max(l1, l2)
    shrt = seq1 if l1 <= l2 else seq2
    lng = seq1 if l1 > l2 else seq2
    # we start with the two sequences left-aligned: xxxxxxxx
    #                                               yyyyyyyyyyyyyy
    # start moving the shortest to the left, one position at a time:
    #                                           <- xxxxxxxx
    #                                               yyyyyyyyyyyyyy
    longest_alignment = ''
    for i in range(int(shrt_len/2)+1):
        if shrt[i:] == lng[0:shrt_len - i]:
            alignment = shrt + lng[shrt_len - i:]
            if len(alignment) > len(longest_alignment):
                longest_alignment = alignment
            break
    # now start with them right-aligned, and move the shortest to the
    # right
    for i in range(int(shrt_len/2)):
        if shrt[0:shrt_len - i] == lng[-(shrt_len - i):]:
            alignment = lng + shrt[shrt_len-i:]
            if len(alignment) > len(longest_alignment):
                longest_alignment = alignment
            break
    return longest_alignment

    
def reconstruct(seqs_arg):
    '''Given a list of substrings, return the smallest superstring containing
    all of them (the substrings must overlap by more than half their length'''
    seqs = seqs_arg[:]
    while len(seqs) > 1:
        for i in range(len(seqs)):
            break_outer = False
            for j in range(len(seqs)):
                # don't compare a sequence with itself
                if i == j:
                    continue
                merged_seq = merge(seqs[i], seqs[j])
                if merged_seq:
                    seqs.remove(seqs[i])
                    seqs.remove(seqs[j-1])
                    seqs.insert(0, merged_seq)
                    break_outer = True
                    break
            if break_outer:
                break
    return seqs[0]

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_long.txt"
    with open(filename) as stream:
        seqs = re.findall('>\w+?\n([ATCG\s]+)', stream.read())
        seqs = [seq.replace('\n', '') for seq in seqs]
        print(reconstruct(seqs))

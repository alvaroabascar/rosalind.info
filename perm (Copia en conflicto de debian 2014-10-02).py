#!/usr/bin/python3

import sys

def permutations(lista):
    if len(lista) == 1:
        return [lista]
    perms = []
    for item in lista:
        newlista = [it for it in lista if it != item]
        newperms = permutations(newlista)
        for newperm in newperms:
            perms.append([item] + newperm)
    return perms

def permutations_n(n):
    return permutations([str(i) for i in list(range(1, n+1))])

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_perm.txt"
    with open(filename) as stream:
        perms = permutations_n(int(stream.read().strip()))
        print(len(perms))
        print('\n'.join([' '.join(it for it in perm) for perm in perms]))

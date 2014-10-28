#!/usr/bin/python3

import sys

def signed_perms(order, lista):
    if order == 1:
        return [[l] for l in lista]
    perms = []
    newlista = lista + [-i for i in lista]
    for item in newlista:
        others = [it for it in newlista if it != item and -it != item]
        newperms = signed_perms(order - 1, others)
        for perm in newperms:
            perms.append([item] + perm)
    return perms

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_sign.txt"
    with open(filename) as stream:
        inpt = int(stream.read().replace('\n', ''))
        lista = list(range(1, inpt + 1))
        #lista += [-i for i in lista]
        result = [tuple(i) for i in signed_perms(inpt, lista)]
        result = list(set(result))
        print(len(result))
        print('\n'.join([' '.join([str(i) for i in perm]) for perm in result]))

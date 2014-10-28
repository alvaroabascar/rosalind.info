#!/usr/bin/python3

import sys

def combinations(lista, n):
    combs = []
    if n == 1:
        return [[l] if type(l) != list else l for l in lista]
    for item in lista:
        newcombs = combinations(lista, n - 1)
        for newcomb in newcombs:
            combs.append([item] + newcomb)
    return combs

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "rosalind_lexf.txt"
    with open(filename) as stream:
        inputs = [line.strip() for line in stream.readlines()]
        symbols = inputs[0].split(' ')
        n = int(inputs[1])
        sym_to_num = {}
        num_to_sym = {}
        i = 0
        for symbol in symbols:
            sym_to_num[symbol] = str(i)
            num_to_sym[str(i)] = symbol
            i = i + 1
        nums = [sym_to_num[sym] for sym in symbols]
        combs = combinations(nums, n)
        combs.sort()
        strings = []
        for comb in combs:
            string = ''
            for num in comb:
                string += num_to_sym[num]
            strings.append(string)
        print('\n'.join(strings))

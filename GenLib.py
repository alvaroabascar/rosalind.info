import re

genetic_code = dict(
    [('UUU', 'F'), 
     ('UUC', 'F'), 
     ('UUA', 'L'), 
     ('UUG', 'L'), 
     ('UCU', 'S'), 
     ('UCC', 'S'), 
     ('UCA', 'S'), 
     ('UCG', 'S'), 
     ('UAU', 'Y'), 
     ('UAC', 'Y'), 
     ('UAA', 'Stop'),
     ('UAG', 'Stop'),
     ('UGU', 'C'),
     ('UGC', 'C'), 
     ('UGA', 'Stop'),
     ('UGG', 'W'), 
     ('CUU', 'L'),
     ('CUC', 'L'),
     ('CUA', 'L'),
     ('CUG', 'L'),
     ('CCU', 'P'),
     ('CCC', 'P'),
     ('CCA', 'P'),
     ('CCG', 'P'),
     ('CAU', 'H'),
     ('CAC', 'H'),
     ('CAA', 'Q'),
     ('CAG', 'Q'),
     ('CGU', 'R'),
     ('CGC', 'R'),
     ('CGA', 'R'),
     ('CGG', 'R'),
     ('AUU', 'I'),
     ('AUC', 'I'),
     ('AUA', 'I'),
     ('AUG', 'M'),
     ('ACU', 'T'),
     ('ACC', 'T'),
     ('ACA', 'T'),
     ('ACG', 'T'),
     ('AAU', 'N'),
     ('AAC', 'N'),
     ('AAA', 'K'),
     ('AAG', 'K'),
     ('AGU', 'S'),
     ('AGC', 'S'),
     ('AGA', 'R'),
     ('AGG', 'R'),
     ('GUU', 'V'),
     ('GUC', 'V'),
     ('GUA', 'V'),
     ('GUG', 'V'),
     ('GCU', 'A'),
     ('GCC', 'A'),
     ('GCA', 'A'),
     ('GCG', 'A'),
     ('GAU', 'D'),
     ('GAC', 'D'),
     ('GAA', 'E'),
     ('GAG', 'E'),
     ('GGU', 'G'),
     ('GGC', 'G'),
     ('GGA', 'G'),
     ('GGG', 'G')])

monoisotopic_mass = dict(
   [("A", 71.03711),
    ("C", 103.00919),
    ("D", 115.02694),
    ("E", 129.04259),
    ("F", 147.06841),
    ("G", 57.02146),
    ("H", 137.05891),
    ("I", 113.08406),
    ("K", 128.09496),
    ("L", 113.08406),
    ("M", 131.04049),
    ("N", 114.04293),
    ("P", 97.05276),
    ("Q", 128.05858),
    ("R", 156.10111),
    ("S", 87.03203),
    ("T", 101.04768),
    ("V", 99.06841),
    ("W", 186.07931),
    ("Y", 163.06333),
    ("H2O", 18.01056)])

def DNA_to_RNA(DNAseq):
    '''Given a DNA sequence, transcribes it into RNA'''
    return DNAseq.replace('T', 'U')

def RNA_to_DNA(RNAseq):
    '''Given a RNA sequence, turn it into DNA'''
    return RNAseq.replace('U', 'T')

def DNA_to_prot(DNAseq):
    return RNA_to_prot(DNA_to_RNA(DNAseq))

def RNA_to_prot(RNAseq):
    '''Translates the given sequence into a protein, finishing at the
        first stop'''
    prot = []
    for i in range(0, len(RNAseq) - 2, 3):
        if genetic_code[RNAseq[i:i+3]] == 'Stop':
            break
        prot.append(genetic_code[RNAseq[i:i+3]])
    return ''.join(prot)

def complement(DNAseq):
    return DNAseq.replace('A', 't').replace('T', 'a').replace('C', 'g').\
        replace('G', 'c').upper()

def reverse_complement(DNAseq):
    comp = list(complement(DNAseq))
    comp.reverse()
    return ''.join(comp)

def find_orfs_one_strand(DNAseq):
    '''Given a sequence of DNA, returns a list of tuples (start, end)
    which delimites each ORF'''
    orfs = []
    begins = re.finditer(r'ATG', DNAseq)
    ends = [a.start() for a in re.finditer(r'TGA|TAG|TAA', DNAseq)]
    for begin in begins:
        start = begin.start()
        orf = None
        for end in ends:
            if end > start and (end - start) % 3 == 0:
                orf = (start, end)
                orfs.append(orf)
                break
    return [DNAseq[o[0]:o[1]] for o in orfs]

def find_orfs(DNAseq):
    result = find_orfs_one_strand(DNAseq)
    result.extend(find_orfs_one_strand(reverse_complement(DNAseq)))
    return result

def permutations(lista):
    '''Given a list "lista" of elements, returns all permutations
	(not repeating elements)'''
    perms = []
    if len(lista) == 1:
        return [lista]
    for item in lista:
        newlista = [it for it in lista if it != item]
        newperms = permutations(newlista)
        for newperm in newperms:
            perms.append([item] + newperm)
    return perms

def combinations(lista, n):
    '''Given a list "lista" and an integer "n", returns a list of all
    the possible combinations of "n" elements from "lista" (including
    repetition)'''
    combs = []
    if n == 1:
        return [[l] if type(l) != list else l for l in lista]
    for item in lista:
        newcombs = combinations(lista, n - 1)
        for newcomb in newcombs:
            combs.append([item] + newcomb)
    return combs

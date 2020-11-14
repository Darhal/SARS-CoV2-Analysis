import pytest
import numpy
import Bio
from Bio.Data import CodonTable
from Bio import SeqIO
#from Bio.Alphabet import generic_dna
from Bio.SeqUtils import GC, GC123
import timeit
import matplotlib
import math


#def sum(n):
#    res = 0
#    for k in range(n):
#        res += math.sin(k+1)
#    return res

#def sequence_arn(file):
#    S = []
#    for seq in SeqIO.parse(open('file'),'fasta'):
#        S.append(seq)
#    return S
#Seq.read(open(fasta)),'fasta',alphabet=generic_dna).seq


 S =[]

 for seq in SeqIO.parse(open('sous-ensemble_1_nucleotide_ver.fasta'),'fasta'):
     S.append(seq)
 print(S)


def taille_ensemble(L): # taille d'une liste de séquence
    l = []

    for k in L:
        l.append(len(k))
    return l


#def tri(L): # peut être écrit si .sort n'est pas donné


def moyenne(list): # on prend en entée une liste de valeur
    if not list:
        return None
    
    res = 0

    for k in list:
        res += k
    return res/len(list)


def mediane(list): # on prend en entrée une liste de valeur
    if not list:
        return None

    L = list.sort()
    n = len(L)

    if n%2 == 0:
        return (L[n/2]+L[n/2-1])/2
    else:
        return L[(n-1)/2]


def quartile(n,list): # quartile(2,list) est la médiane
    if not list:
        return None
    if n not in [1,2,3]:
        return None
    
    L = list.sort()
    t = len(list)
    
    if n == 1:
        if t%4 == 0:
            return (L[n/4]+L[n/4-1])/2
        else:
            return L[int(n/4)]
    elif n == 2:
        return mediane(list)
    elif n == 3:
        if t%4 == 0:
            return (L[3*n/4]+L[3*n/4-1])/2
        else:
            return L[int(3*n/4)]


def taux_GC123_ensemble(L): # taux GC123 du'une liste de séquence
    l = []

    for seq in L:
        l.append(GC123(seq))
    return l


def variance(list):
    if not list:
        return None

    res = 0

    m = moyenne(list)
    for k in list:
        res += (m-k)**2
    return res/len(list)


def ecart_type(list):
    return math.sqrt(variance(list))


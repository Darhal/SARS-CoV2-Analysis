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
from src.stats import *

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


#  S =[]

#  for seq in SeqIO.parse(open('sous-ensemble_1_nucleotide_ver.fasta'),'fasta'):
#      S.append(seq)
#  print(S)


# taille_ensemble([seqA, seqB, seqC]) = [len(seqA),len(seqB),len(seqC)]

def taille_ensemble(L): # liste de la taille de chaque séquence d'une liste de séquence
    ''' on aura un échantillon de séquence, la fonction permet de donner la taille de chaque séquence dans une liste

    Args :
        liste de séquences

    Returns :
        liste de la taille de chaque séquence de l'échantillon
    '''
    l = []

    for k in L:
        l.append(len(k))
    return l


#def tri(L): # peut être écrit si .sort n'est pas donné


def moyenne(list): # on prend en entée une liste de valeur
    ''' la fonction fait la moyenne des valeurs d'une liste

    Args :
        liste de valeurs

    Returns :
        la moyenne des valeurs
    '''
    if not list:
        return None
    
    res = 0

    for k in list:
        res += k
    return res/len(list)


def mediane(list): # on prend en entrée une liste de valeur
    ''' la fonction donne la médiane de l'échantillon

    Args :
        liste de valeurs

    Returns :
        la médiane de la liste
    '''
    if not list:
        return None

    L = list.sort()
    n = len(L)

    if n%2 == 0:
        return (L[n/2]+L[n/2-1])/2
    else:
        return L[(n-1)/2]


def quartile(n,list): # quartile(2,list) est la médiane
    ''' la fonction donne le quartile (1er, 2e, ou 3e) de l'échantillon

    Args :
        liste de valeurs

    Returns :
        le quartile (1er, 2e, ou 3e) de la liste
    '''
    if not list:
        return None
    if n not in [1,2,3]:
        return None
    
    L = list.sort()
    t = len(list)
    
    if n == 1: # le 1er quartile
        if t%4 == 0:
            return (L[n/4]+L[n/4-1])/2
        else:
            return L[int(n/4)]
    elif n == 2: # la médiane
        return mediane(list)
    elif n == 3: # le 3e quartile
        if t%4 == 0:
            return (L[3*n/4]+L[3*n/4-1])/2
        else:
            return L[int(3*n/4)]


def taux_GC123_ensemble(L): # taux GC123 d'une liste de séquence, ça donne le taux de GC dans liste de séquences
    l = []

    for seq in L:
        l.append(GC123(seq))
    return l


def variance(list):
    ''' la fonction calcule la variance de l'échantillon

    Args :
        liste de valeurs

    Returns :
        la variance de la liste
    '''
    if not list:
        return None

    res = 0
    m = moyenne(list)

    for k in list:
        res += (m-k)**2
    return res/len(list)


def ecart_type(list):
    ''' la fonction calcule l'écart-type de l'échantillon

    Args :
        liste de valeurs

    Returns :
        l'écart-type' de la liste
    '''
    return math.sqrt(variance(list))


def intervalle_interquartile(list):
    return quartile(3,list) - quartile(1,list)


def nombre_nucleotide_echantillon(tab):
    A = []
    U = []
    G = []
    C = []

    for k in tab:
        N = nombre_nucleotide(k)
        A.append(N['A'])
        U.append(N['U'])
        G.append(N['G'])
        C.append(N['C'])
    return [A, U, G, C]


def moyenne_nucleotide(tab):
    A = moyenne(nombre_nucleotide_echantillon(tab)[0])
    U = moyenne(nombre_nucleotide_echantillon(tab)[1])
    G = moyenne(nombre_nucleotide_echantillon(tab)[2])
    C = moyenne(nombre_nucleotide_echantillon(tab)[3])
    return {'A':A, 'U':U, 'G':G, 'C':C}


def mediane_nucleotide(tab):
    A = mediane(nombre_nucleotide_echantillon(tab)[0])
    U = mediane(nombre_nucleotide_echantillon(tab)[1])
    G = mediane(nombre_nucleotide_echantillon(tab)[2])
    C = mediane(nombre_nucleotide_echantillon(tab)[3])
    return {'A': A, 'U': U, 'G': G, 'C': C}


def quartile_nucleotide(n, tab):
    A = quartile(n, nombre_nucleotide_echantillon(tab)[0])
    U = quartile(n, nombre_nucleotide_echantillon(tab)[1])
    G = quartile(n, nombre_nucleotide_echantillon(tab)[2])
    C = quartile(n, nombre_nucleotide_echantillon(tab)[3])
    return {'A': A, 'U': U, 'G': G, 'C': C}


def intervalle_interquartile_nucleotide(tab):
    A = intervalle_interquartile(nombre_nucleotide_echantillon(tab)[0])
    U = intervalle_interquartile(nombre_nucleotide_echantillon(tab)[1])
    G = intervalle_interquartile(nombre_nucleotide_echantillon(tab)[2])
    C = intervalle_interquartile(nombre_nucleotide_echantillon(tab)[3])
    return {'A': A, 'U': U, 'G': G, 'C': C}


def variance_nucleotide(tab):
    A = variance(nombre_nucleotide_echantillon(tab)[0])
    U = variance(nombre_nucleotide_echantillon(tab)[1])
    G = variance(nombre_nucleotide_echantillon(tab)[2])
    C = variance(nombre_nucleotide_echantillon(tab)[3])
    return {'A': A, 'U': U, 'G': G, 'C': C}


def ecart_type_nucleotide(tab):
    A = ecart_type(nombre_nucleotide_echantillon(tab)[0])
    U = ecart_type(nombre_nucleotide_echantillon(tab)[1])
    G = ecart_type(nombre_nucleotide_echantillon(tab)[2])
    C = ecart_type(nombre_nucleotide_echantillon(tab)[3])
    return {'A': A, 'U': U, 'G': G, 'C': C}


def moyenne_taille_genome(tab):
    return moyenne(taille_ensemble(tab))


def mediane_taille_genome(tab):
    return mediane(taille_ensemble(tab))


def quartile_taille_genome(n, tab):
    return quartile(n, taille_ensemble(tab))


def intervalle_interquartile_taille_genome(tab):
    return intervalle_interquartile(taille_ensemble(tab))


def ecart_type_taille_genome(tab):
    return ecart_type(taille_ensemble(tab))
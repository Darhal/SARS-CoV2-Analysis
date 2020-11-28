import math
from .utility import *
from .codon import *
from .stats import *

def moyenne_nucleotide(tab):
    ''' La fonction calcule la moyenne d'apparition de chaque nucleotide dans l'échantillon

    Args :
        tab : échantillon (liste) de séquences

    Returns :
        dictionnaire des apparitions moyenne des nucléotides dans l'échantillon
    '''
    A = moyenne(nombre_nucleotide_echantillon(tab)[0])
    U = moyenne(nombre_nucleotide_echantillon(tab)[1])
    G = moyenne(nombre_nucleotide_echantillon(tab)[2])
    C = moyenne(nombre_nucleotide_echantillon(tab)[3])
    return {'A':A, 'U':U, 'G':G, 'C':C}


def mediane_nucleotide(tab):
    ''' La fonction calcule la médiane d'apparition de chaque nucleotide dans l'échantillon

    Args :
        tab : échantillon (liste) de séquences

    Returns :
        dictionnaire des apparitions médiane des nucléotides dans l'échantillon
    '''
    A = mediane(nombre_nucleotide_echantillon(tab)[0])
    U = mediane(nombre_nucleotide_echantillon(tab)[1])
    G = mediane(nombre_nucleotide_echantillon(tab)[2])
    C = mediane(nombre_nucleotide_echantillon(tab)[3])
    return {'A': A, 'U': U, 'G': G, 'C': C}


def quartile_nucleotide(n, tab):
    ''' La fonction calcule le quartile (1er ou 3e) d'apparition de chaque nucléotide dans l'échantillon

    Args :
        tab : échantillon (liste) de séquences

    Returns :
        dictionnaire des apparitions quartile (1er ou 3e) des nucléotides dans l'échantillon
    '''
    A = quartile(n, nombre_nucleotide_echantillon(tab)[0])
    U = quartile(n, nombre_nucleotide_echantillon(tab)[1])
    G = quartile(n, nombre_nucleotide_echantillon(tab)[2])
    C = quartile(n, nombre_nucleotide_echantillon(tab)[3])
    return {'A': A, 'U': U, 'G': G, 'C': C}


def intervalle_interquartile_nucleotide(tab):
    ''' La fonction calcule l'interquartile (Q3 - Q1) d'apparition de chaque nucléotide dans l'échantillon

    Args :
        tab : échantillon (liste) de séquences

    Returns :
        dictionnaire valeur interquartile (Q3 - Q1) des nucléotides dans l'échantillon
    '''
    A = intervalle_interquartile(nombre_nucleotide_echantillon(tab)[0])
    U = intervalle_interquartile(nombre_nucleotide_echantillon(tab)[1])
    G = intervalle_interquartile(nombre_nucleotide_echantillon(tab)[2])
    C = intervalle_interquartile(nombre_nucleotide_echantillon(tab)[3])
    return {'A': A, 'U': U, 'G': G, 'C': C}


def variance_nucleotide(tab):
    ''' La fonction calcule la variance d'apparition de chaque nucléotide dans l'échantillon

    Args :
        tab : échantillon (liste) de séquences

    Returns :
        dictionnaire valeur de la variance des apparitions des nucléotides dans l'échantillon
    '''
    A = variance(nombre_nucleotide_echantillon(tab)[0])
    U = variance(nombre_nucleotide_echantillon(tab)[1])
    G = variance(nombre_nucleotide_echantillon(tab)[2])
    C = variance(nombre_nucleotide_echantillon(tab)[3])
    return {'A': A, 'U': U, 'G': G, 'C': C}


def ecart_type_nucleotide(tab):
    ''' La fonction calcule l'écart-type d'apparition de chaque nucléotide dans l'échantillon

    Args :
        tab : échantillon (liste) de séquences

    Returns :
        dictionnaire valeur de l'écart-type des apparitions des nucléotides dans l'échantillon
    '''
    A = ecart_type(nombre_nucleotide_echantillon(tab)[0])
    U = ecart_type(nombre_nucleotide_echantillon(tab)[1])
    G = ecart_type(nombre_nucleotide_echantillon(tab)[2])
    C = ecart_type(nombre_nucleotide_echantillon(tab)[3])
    return {'A': A, 'U': U, 'G': G, 'C': C}

def moyenne_acide(tab):
    '''Function that returns the average of occurence of each amino-acid in the sample

       Args:
           tab: sample of amino-acid sequences

       Returns:
           Dictionary that contains the average of occurence of elements as value and the element as key
    '''

    d = {}
    nbr = nombre_element_echantillon(tab)
    list_element = list(nbr.keys())

    for element in list_element:
        d[element] = moyenne(nbr[element])

    return d


def mediane_acide(tab):
    '''Function that returns the median of occurence of each amino-acid in the sample

       Args:
           tab: sample of amino-acid sequences

       Returns:
           Dictionary that contains the median of occurence of elements as value and the element as key
    '''

    d = {}
    nbr = nombre_element_echantillon(tab)
    list_element = list(nbr.keys())

    for element in list_element:
        d[element] = mediane(nbr[element])

    return d


def quartile_acide(n, tab):
    '''Function that returns the first or third quartile of occurence of each amino-acid in the sample

       Args:
           n: integer (1 or 3 )
           tab: sample of amino-acid sequences

       Returns:
           Dictionary that contains the quartile of occurence of elements as value and the element as key
    '''

    d = {}
    nbr = nombre_element_echantillon(tab)
    list_element = list(nbr.keys())

    for element in list_element:
        d[element] = quartile(n, nbr[element])

    return d


def intervalle_interquartile_acide(tab):
    '''Function that returns the interquartile (Q3 - Q1) of occurence of each amino-acid in the sample

       Args:
           tab: sample of amino-acid sequences

       Returns:
           Dictionary that contains the interquartile of occurence of elements as value and the element as key
    '''

    d = {}
    nbr = nombre_element_echantillon(tab)
    list_element = list(nbr.keys())

    for element in list_element:
        d[element] = intervalle_interquartile(nbr[element])

    return d


def variance_acide(tab):
    '''Function that returns the variance of occurence of each amino-acid in the sample

       Args:
           tab: sample of amino-acid sequences

       Returns:
           Dictionary that contains the variance of occurence of elements as value and the element as key
    '''

    d = {}
    nbr = nombre_element_echantillon(tab)
    list_element = list(nbr.keys())

    for element in list_element:
        d[element] = variance(nbr[element])

    return d


def ecart_type_acide(tab):
    '''Function that returns the standard deviation of occurence of each amino-acid in the sample

        Args:
          tab: sample of amino-acid sequences

        Returns:
          Dictionary that contains the standard deviation of occurence of elements as value and the element as key
    '''

    d = {}
    nbr = nombre_element_echantillon(tab)
    list_element = list(nbr.keys())

    for element in list_element:
        d[element] = ecart_type(nbr[element])

    return d
import math
from .utility import *

def proportions(sequence):
    '''Retourne un dictionaire contenant les proportions des différents nucléotides de la séquence d'ARNm entré.

    Args:
        sequence : the ARNm or codons sequence (type : string)

    Returns:
        dico_proportions : Dictionnaire associant les proportions aux éléments de la séquence
    '''

    dico_nombre_elements = nombre_elements(sequence)
    nombre_total_elements = total_elements(sequence)
    dico_proportions = {}
    
    for element in dico_nombre_elements:
        dico_proportions[element] = dico_nombre_elements[element]/nombre_total_elements

    return dico_proportions


def moyenne(list): # on prend en entée une liste de valeur
    ''' La fonction fait la moyenne des valeurs d'une liste

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
    ''' La fonction donne la médiane de l'échantillon

    Args :
        liste de valeurs

    Returns :
        la médiane de la liste
    '''
    if not list:
        return None

    L = sorted(list)
    n = len(L)

    if n%2 == 0:
        return (L[n//2]+L[n//2-1])/2
    else:
        return L[(n-1)//2]


def quartile(n,list): # quartile(2,list) est la médiane
    ''' La fonction donne le quartile (1er, 2e, ou 3e) de l'échantillon

    Args :
        liste de valeurs

    Returns :
        le quartile (1er, 2e, ou 3e) de la liste
    '''
    if not list:
        return None
    if n not in [1,2,3]:
        return None
    
    L = sorted(list)
    t = len(list)
    
    if n == 2: # la médiane
        return mediane(list)
    elif t%4 == 0:
        if n == 1:
            return (L[t//4]+L[t//4 - 1]) / 2
        elif n == 3:
            return (L[3*t//4]+L[3*t//4 - 1]) / 2
    elif (t%4 == 1) or (t%4 == 2):
        if n == 1:
            return L[int(t/4)]
        elif n == 3:
            return L[int(3*t/4)]
    elif t%4 == 3:
        if n == 1:
            return (L[int(t/4)]+L[int(t/4) + 1]) / 2
        elif n == 3:
            return (L[int(3*t/4)]+L[int(3*t/4) - 1]) / 2


def intervalle_interquartile(list):
    return quartile(3,list) - quartile(1,list)


def variance(list):
    ''' La fonction calcule la variance de l'échantillon

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
    ''' La fonction calcule l'écart-type de l'échantillon

    Args :
        liste de valeurs

    Returns :
        l'écart-type' de la liste
    '''
    return math.sqrt(variance(list))


def moyenne_proportion(liste):
    ''' function that calculate the average of proportions of a nucleotide based on different RNA

    Args :
        list of dictionaries that represent the RNA sequences

    Returns :
        Dictionary that contains the average of proportions of nucleotides as values and nucleotides as keys
    '''
    s = 0
    d = {'A': 0, 'U': 0, 'G': 0, 'C': 0}

    for nucl in ["A", "C", "G", "U"]:
        for p in range(len(liste)):
            seq = liste[p]
            s+= seq[nucl]

        d[nucl] = s/len(liste)

    return(d)



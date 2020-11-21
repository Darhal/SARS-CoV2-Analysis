import math
from .utility import *

def proportions(ARNm):
    '''Retourne un dictionaire contenant les proportions des différents nucléotides de la séquence d'ARNm entré.

    Args:
        ARNm : the ARNm sequence (type : string)

    Returns:
        dico_proportions : Dictionnaire associant les proportions aux différentes bases
    '''
    
    
    dico_nombre_nucleotides = nombre_nucleotide(ARNm)
    total_nucleotides = total_nucleotide(ARNm)

    prop_a = 100*dico_nombre_nucleotides["A"]/total_nucleotides
    prop_t = 100*dico_nombre_nucleotides["U"]/total_nucleotides
    prop_g = 100*dico_nombre_nucleotides["G"]/total_nucleotides
    prop_c = 100*dico_nombre_nucleotides["C"]/total_nucleotides

    dico_proportions = {"A" : prop_a, "U" : prop_t, "G" : prop_g, "C" : prop_c}

#    print("Proportion de A :",prop_a,"% (",dico_nombre_nucleotides["A"],"bases / ",total_nucleotides,"bases)")
#    print("Proportion de T :",prop_t,"% (",dico_nombre_nucleotides["T"],"bases / ",total_nucleotides,"bases)")
#    print("Proportion de C :",prop_c,"% (",dico_nombre_nucleotides["C"],"bases / ",total_nucleotides,"bases)")
#    print("Proportion de G :",prop_g,"% (",dico_nombre_nucleotides["G"],"bases / ",total_nucleotides,"bases)\n")

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


def moyenne_nucleotide(tab):
    ''' La fonction calcule la moyenne d'apparition de chaque nucleotide dans l'échantillon

    Args :
        échantillon (liste) de séquences

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
        échantillon (liste) de séquences

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
        échantillon (liste) de séquences

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
        échantillon (liste) de séquences

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
        échantillon (liste) de séquences

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
        échantillon (liste) de séquences

    Returns :
        dictionnaire valeur de l'écart-type des apparitions des nucléotides dans l'échantillon
    '''
    A = ecart_type(nombre_nucleotide_echantillon(tab)[0])
    U = ecart_type(nombre_nucleotide_echantillon(tab)[1])
    G = ecart_type(nombre_nucleotide_echantillon(tab)[2])
    C = ecart_type(nombre_nucleotide_echantillon(tab)[3])
    return {'A': A, 'U': U, 'G': G, 'C': C}


def moyenne_taille_genome(tab):
    ''' La fonction calcule la taille moyenne du genome dans l'échantillon

    Args :
        échantillon (liste) de séquences

    Returns :
        valeur de la taille moyenne du genome dans l'échantillon
    '''
    return moyenne(taille_ensemble(tab))


def mediane_taille_genome(tab):
    ''' La fonction calcule la taille médiane du genome dans l'échantillon

    Args :
        échantillon (liste) de séquences

    Returns :
        valeur de la taille médiane du genome dans l'échantillon
    '''
    return mediane(taille_ensemble(tab))


def quartile_taille_genome(n, tab):
    ''' La fonction calcule la taille du quartile (1er ou 3e) du genome dans l'échantillon

    Args :
        échantillon (liste) de séquences

    Returns :
        valeur de la taille du quartile (1er ou 3e) du genome dans l'échantillon
    '''
    return quartile(n, taille_ensemble(tab))


def intervalle_interquartile_taille_genome(tab):
    ''' La fonction calcule l'intervalle interquartile de la taille du genome dans l'échantillon

    Args :
        échantillon (liste) de séquences

    Returns :
        valeur de l'intervalle interquartile de la taille du genome dans l'échantillon
    '''
    return intervalle_interquartile(taille_ensemble(tab))


def variance_taille_genome(tab):
    ''' La fonction calcule la variance des tailles des genomes dans l'échantillon

    Args :
        échantillon (liste) de séquences

    Returns :
        valeur de la variance des tailles des genomes dans l'échantillon
    '''
    return variance(taille_ensemble(tab))


def ecart_type_taille_genome(tab):
    ''' La fonction calcule l'écrat-type des tailles des genomes dans l'échantillon

    Args :
        échantillon (liste) de séquences

    Returns :
        valeur de l'écrat-type des tailles des genomes dans l'échantillon
    '''
    return ecart_type(taille_ensemble(tab))

from Bio import SeqIO

def fasta_to_genome(filename):
    '''Function that parse a fasta file
    
    Args:
        filename: the fasta file that contain the genomic data

    Returns:
        The first sequence if the file contains only one, a table of sequences otherwise
    '''
    genome = []

    for seq_record in SeqIO.parse(filename, "fasta"):
        genome.append(seq_record.seq)

    if len(genome) == 1:
        return genome[0]
    return genome


def transcription_complementaire(ADNc):
    '''Function qui remplace la séquence de ADNc (ADN complémentaire) en ARNm
    
    Args:
        ADN : La séquence d'ADN complémentaire du génome à retranscrire en ARNm

    Returns:
        ARNm : La séquence d'ARNm issue de la séquence d'ADNc entrée.
    '''
    d_transcription = []
    
    for base in ADNc:
        if base == "T" :
            d_transcription.append("U")
        else:
            d_transcription.append(base)

    ARNm = ''.join(d_transcription)
        
    return ARNm


def total_nucleotide(ARNm):
    '''Nombre total des nucléotides dans une sequence

    Args:
        ARNm: the RNA sequence

    Returns:
        Length of the RNA sequence
    '''
    return len(ARNm)


def taille_ensemble(L): # liste de la taille de chaque séquence d'une liste de séquence
    ''' On aura un échantillon de séquence, la fonction permet de donner la taille de chaque séquence dans une liste

    Args :
        liste de séquences

    Returns :
        liste de la taille de chaque séquence de l'échantillon
    '''
    l = []

    for k in L:
        l.append(len(k))
    return l


def nombre_nucleotide(ARNm):
    '''Retourne un dictionnaire indiquant le nombre de chaque type de nucléotide

    Args:
        ARNm: the RNA sequence
    
    Returns:
        Dictionary that contains the number of nucleotides as value and nucleotide as key
    '''
    d = {'A':0, 'U':0, 'G':0, 'C':0}

    for i in range(len(ARNm)):
        if ARNm[i] == 'A':
            d['A'] += 1
        elif ARNm[i] == 'U':
            d['U'] += 1
        elif ARNm[i] == 'G':
            d['G'] += 1
        elif ARNm[i] == 'C':
            d['C'] += 1

    return d


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
from Bio import SeqIO

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

def fasta_to_genome(filename):
    '''Function that parse a fasta file
    
    Args:
        filename: the fasta file that contain the genomic data

    Returns:
        The first sequence if the file contains only one, a table of sequences otherwise
    '''
    genome = []

    for seq_record in SeqIO.parse(filename, "fasta"):
        genome.append(transcription_complementaire(seq_record.seq))

    if len(genome) == 1:
        return genome[0]
    return genome

def total_elements(sequence):
    '''Nombre total d'éléments dans une sequence (ARN, ADN ou Acides aminés)

    Args:
        sequence: the RNA/DNA/amino-acid sequence

    Returns:
        Length of the RNA sequence
    '''
    return len(sequence)


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

def nombre_elements(sequence):
    '''Retourne un dictionnaire indiquant le nombre de chaque element de la sequence

    Args:
        sequence: the RNA/DNA/amino-acid sequence
    
    Returns:
        Dictionary that contains the number of elements as value and the element as key
    '''

    d = {}

    for i in sequence:
        if i not in d:
            d[i] = 1
        
        else:
            d[i] += 1

    return d

def nombre_nucleotide_echantillon(tab):
    A = []
    U = []
    G = []
    C = []

    for k in tab:
        N = taille_ensemble(k)
        A.append(N['A'])
        U.append(N['U'])
        G.append(N['G'])
        C.append(N['C'])
    return [A, U, G, C]
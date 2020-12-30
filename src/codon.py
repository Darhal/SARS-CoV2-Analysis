from Bio import SeqIO
from src.utility import *
from src.globals import *

def start_to_stop(ARNm):
    """Function that returns sequences of an ARNm from start to stop codons

    Args:
        ARNm: ARN sequence string or list

    Returns:
        List of valid sequences
    """
    ARNm = ''.join(ARNm)
    length = len(ARNm)
    l = []
    i = 0

    while (i < (length-4)) :
        if ARNm[i:i+3] == 'AUG':
            j = i + 3

            while (ARNm[j:j+3] not in ['UGA', 'UAG', 'UAA', 'UAR']) and (j < length-3):
                j += 3

            if ARNm[j:j+3] in ['UGA', 'UAG', 'UAA', 'UAR']:
                l.append(ARNm[i:j])
                i = j + 3

            if j >= length-3:
                break
        else:
            i += 1
    return l


def codons(ARNm):
    '''Function that return the amino acids coded by the ARNm sequence

       Args:
           ARNm: ARN sequence list or string

       Returns:
           List of the amino acids
    '''
    seq = start_to_stop(ARNm)
    l = []

    for i in range(len(seq)):
        amino_acids = []
        length = len(seq[i])

        for j in range(0, length - 2, 3):
            codons = "".join([seq[i][j], seq[i][j + 1], seq[i][j + 2]])  # Constructing a codon
            if try_AUGC(codons):
                amino_acid = CODONS_TO_AMINO_ACIDS[codons]
                amino_acids.append(amino_acid)
            else:
                continue

        amino_seq = "".join(amino_acids)
        l.append(amino_seq)

    return l


def codons_v2(ARNm):
    '''Function that return the amino acids coded by the ARNm sequence
    
    Args:
        ARNm: ARN sequence
    
    Returns:
        List of the amino acids
    '''
    amino_acids = []
    length = len(ARNm)
    length = length - length % 3

    for i in range(0, length - 2, 3):
        codons = "".join([ARNm[i], ARNm[i + 1], ARNm[i + 2]])   # Constructing a codon
        amino_acid = CODONS_TO_AMINO_ACIDS[codons]
        amino_acids.append(amino_acid)
    
    return ''.join(amino_acids)


def codons_echantillon(liste):
    '''Function that return the amino acids sequences coded by the ARNm sequence list

    Args:
        ARNm: ARN sequence list

    Returns:
        List of the amino acid sequences
    '''
    sortie = []

    for sequence in liste:
        traduction = codons_v3(sequence)
        sortie.append(traduction)

    return sortie


def codons_v3(ARNm):
    '''Function that returns the amino acids coded by the ARNm sequence

        Args:
            ARNm: a list of ARN sequence

        Returns:
            List of the amino acids
    '''
    ARNm_ch = ''.join(ARNm)
    seq = start_to_stop(ARNm_ch)
    l = []

    for i in range(len(seq)):
        amino_acids = []
        length = len(seq[i])

        for j in range(0, length - 2, 3):
            codons = "".join([seq[i][j], seq[i][j + 1], seq[i][j + 2]])  # Constructing a codon
            if try_AUGC(codons):
                amino_acid = CODONS_TO_AMINO_ACIDS[codons]
                amino_acids.append(amino_acid)
            else:
                continue

        amino_seq = "".join(amino_acids)
        l.append(amino_seq)

    res = "".join(l)
    return res


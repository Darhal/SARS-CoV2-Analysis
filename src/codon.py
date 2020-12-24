from Bio import SeqIO
from .utility import *
from .globals import *


def codons(ARNm):
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
        traduction = codons(sequence)
        sortie.append(traduction)

    return sortie


def start_to_stop(ARNm):
    """

    """
    length = len(ARNm)
    l = []
    i = 0

    while (i < (length-4)) :

        if ARNm[i:i+3] == 'AUG':
            j = i+3

            while (ARNm[j:j+3] not in ['UAG', 'UAA', 'UAR']) and (j < length-3):
                j += 1

            if ARNm[j:j+3] in ['UAG', 'UAA', 'UAR']:
                l.append(ARNm[i:j])
                i = j+3

            if j >= length-3 :
                break

        else:
            i+=1

    return l
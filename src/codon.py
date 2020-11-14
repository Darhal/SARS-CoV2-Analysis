from Bio import SeqIO
from utility import *
from globals import *


def codons(ARNm):
    '''Function that return the amino acids coded by the ARNm sequence
    
    Args:
        ARNm: ARN sequence
    
    Returns:
        List of the amino acids
    '''
    amino_acids = []

    for i in range(0, len(ARNm) - 3, 3):
        codons = "".join([ARNm[i], ARNm[i + 1], ARNm[i + 2]])   # Constructing a codon
        amino_acid = CODONS_TO_AMINO_ACIDS[codons]
        amino_acids.append(amino_acid)
    
    return amino_acids
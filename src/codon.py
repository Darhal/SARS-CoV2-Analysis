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
    amino_acids_seq = []
    amino_acids = []

    for i in range(0, len(ARNm) - 3, 3):
        codons = "".join([ARNm[i], ARNm[i + 1], ARNm[i + 2]])   # Constructing a codon
        codons = codons.replace('T', 'U')                       # replace T with U
        amino_acid = CODONS_TO_PROTEINS[codons]

        if amino_acid == "STOP":
            if len(amino_acids) != 0:
                amino_acids_seq.append(amino_acids)
                amino_acids = []
        else:
            amino_acids.append(amino_acid)
    
    return amino_acids_seq
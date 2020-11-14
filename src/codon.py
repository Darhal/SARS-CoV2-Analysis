from Bio import SeqIO
from utility import *
from globals import *


def codons(ARNm):
    '''Fonction qui retourne les acides aminés codé par l'ARN
    
    Args:
        ARNm: Seq d'ARN
    
    Returns:
        liste des acides aminés
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
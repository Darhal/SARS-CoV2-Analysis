from Bio import SeqIO

def fasta_to_genome(filename):
    genome = []

    for seq_record in SeqIO.parse("../genome/"+filename, "fasta"):
        genome.append(seq_record.seq)

    return genome


def total_nucleotide(ARNm):
    '''
        Fonction qui retourne le nombre total des nucléotides dans une sequence

        Args:
            ARNm: Seq d'ARN

        Returns:
            un entier qui représente la taille de seq
        '''
    return len(ARNm)

def nombre_nucleotide(ARNm):
    '''
    Fonction qui retourne le nombre de chaque type de nucléotide

    Args:
        ARNm: Seq d'ARN

    Returns:
        un dictionnaire qui prend les nucléotides comme clés et le nombre de chaque nucléotides comme valeurs
    '''
    d = {'A':0, 'T':0, 'G':0, 'C':0}

    for i in range(len(ARNm)):
        if ARNm[i] == 'A':
            d['A'] += 1
        elif ARNm[i] == 'T':
            d['T'] += 1
        elif ARNm[i] == 'G':
            d['G'] += 1
        elif ARNm[i] == 'C':
            d['C'] += 1

    return d
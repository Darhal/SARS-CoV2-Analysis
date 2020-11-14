from Bio import SeqIO

def fasta_to_genome(filename):
    '''Function that parse a fasta file
    
    Args:
        filename: the fasta file that contain the genomic data

    Returns:
        The first sequence if the file contains only one, a table of sequences otherwise
    '''
    genome = []

    for seq_record in SeqIO.parse("../genome/"+filename, "fasta"):
        genome.append(seq_record.seq)

    if len(genome) == 1:
        return genome[0]
    return genome


<<<<<<< HEAD
def total_nucleotide(ARNm):
    '''
        Fonction qui retourne le nombre total des nucléotides dans une sequence

        Args:
            ARNm: Seq d'ARN

        Returns:
            un entier qui représente la taille de seq
        '''
||||||| 8f14109
def total_nucleotide(ARNm):         #nombre total des nucléotides dans une sequence
=======
def total_nucleotide(ARNm):
    '''Nombre total des nucléotides dans une sequence

    Args:
        ARNm: the RNA sequence

    Returns:
        Length of the RNA sequence
    '''
>>>>>>> 18592bf7fccc9fc0e711b37d84cf48bfaf2c1468
    return len(ARNm)

<<<<<<< HEAD
def nombre_nucleotide(ARNm):
    '''
    Fonction qui retourne le nombre de chaque type de nucléotide

    Args:
        ARNm: Seq d'ARN

    Returns:
        un dictionnaire qui prend les nucléotides comme clés et le nombre de chaque nucléotides comme valeurs
    '''
||||||| 8f14109
def nombre_nucleotide(ARNm):        #retourne un dictionnaire indiquant le nombre de chaque type de nucléotide
=======

def nombre_nucleotide(ARNm):
    '''Retourne un dictionnaire indiquant le nombre de chaque type de nucléotide

    Args:
        ARNm: the RNA sequence
    
    Returns:
        Dictionary that contains the number of nucleotides as value and nucleotide as key
    '''
>>>>>>> 18592bf7fccc9fc0e711b37d84cf48bfaf2c1468
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
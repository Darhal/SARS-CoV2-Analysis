from Bio import SeqIO

def FastaToGenome(filename):
    genome = []

    for seq_record in SeqIO.parse("../genome/"+filename, "fasta"):
        genome.append(seq_record.seq)
        
    return genome

def total_nucleotide(ARNm):         #nombre total des nucléotides dans une sequence
    return len(ARNm)

def nombre_nucleotide(ARNm):        #retourne un dictionnaire indiquant le nombre de chaque type de nucléotide
    d={'A':0, 'T':0, 'G':0, 'C':0}
    for i in range(len(ARNm)):
        if ARNm[i]=='A':
            d['A']+=1
        elif ARNm[i]=='T':
            d['T']+=1
        elif ARNm[i]=='G':
            d['G']+=1
        elif ARNm[i] =='C':
            d['C']+=1
    return d

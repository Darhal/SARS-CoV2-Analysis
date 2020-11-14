from Bio import SeqIO

def FastaToGenome(filename):
    genome = []

    for seq_record in SeqIO.parse("../genome/"+filename, "fasta"):
        genome.append(seq_record.seq)

    return genome
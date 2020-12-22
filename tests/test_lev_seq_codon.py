from utility import *
from lev import *
from codon import *

sequences10 = fasta_to_genome("../genome/dix_sequences.fasta")
print(lev_itr(codons(sequences10[0]), codons(sequences10[2])))

seqUSA = fasta_to_genome("../genome/deux_sequences_usa_18122020.fasta")
print(lev_itr(codons(seqUSA[0]), codons(seqUSA[1])))

seqUSAchina = fasta_to_genome("../genome/deux_sequences_china_13012020_usa_18122020.fasta")
print(lev_itr(codons(seqUSAchina[0]), codons(seqUSAchina[1])))
from src.utility import *
from src.codon import *

arn = fasta_to_genome("genome/dix_sequences.fasta")[0]
print("------------ CODONS  ------------")
print(codons(arn))
print("------------ CODONS V2 ------------")
print(codons_v2(arn))
print("------------ CODONS V3 ------------")
print(codons_v3(arn))
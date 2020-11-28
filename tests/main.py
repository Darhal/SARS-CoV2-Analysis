import numpy as np

from src.stats import *

###### Test des fonctions _nucleotide ######

print(moyenne_nucleotide(fasta_to_genome("./genome/dix_sequences.fasta")))
print(mediane_nucleotide(fasta_to_genome("./genome/dix_sequences.fasta")))
print(variance_nucleotide(fasta_to_genome("./genome/dix_sequences.fasta")))
print(quartile_nucleotide(1,fasta_to_genome("./genome/dix_sequences.fasta")))
print(quartile_nucleotide(3,fasta_to_genome("./genome/dix_sequences.fasta")))
print(intervalle_interquartile(fasta_to_genome("./genome/dix_sequences.fasta")))
print(ecart_type(fasta_to_genome("./genome/dix_sequences.fasta")))

####################################################

###### Test de la fonction mediane_nucleotide ######

print(variance_nucleotide(fasta_to_genome("./genome/dix_sequences.fasta")))

print(moyenne_acide(fasta_to_genome("./genome/dix_sequences.fasta")))


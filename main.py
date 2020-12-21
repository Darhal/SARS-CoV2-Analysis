import numpy as np

from src.stats import *
from Bio import Seq
from src.lev import *

# # arns = fasta_to_genome("./genome/dix_sequences.fasta")
# # stats = perform_all_stats(arns, NUCLEOTIDES)

# # print(f"Moyenne: {stats['moy']}")
# # print(f"Mediane: {stats['med']}")
# # print(f"ecart type: {stats['ecartt']}")
# # print(f"Variance: {stats['var']}")
# # print(f"Quart 1: {stats['quart1']}")
# # print(f"Quart 3: {stats['quart3']}")
# # print(f"Inter Quart 3: {stats['int_quart']}")

# # ####################### ACIDES AMINES #######################
# # acids = codons_echantillon(arns)
# # moy = call_stat(moyenne, acids, AMINO_ACIDS)
# # med = call_stat(mediane, acids, AMINO_ACIDS)
# # ecartt = call_stat(ecart_type, acids, AMINO_ACIDS)
# # var = call_stat(variance, acids, AMINO_ACIDS)
# # quart1 = call_stat(quartile, acids, AMINO_ACIDS, 1)
# # quart3 = call_stat(quartile, acids, AMINO_ACIDS, 3)
# # int_quart = call_stat(intervalle_interquartile, acids, AMINO_ACIDS)

# # print(f"Moyenne: {moy}")
# # print(f"Mediane: {med}")
# # print(f"ecart type: {ecartt}")
# # print(f"Variance: {var}")
# # print(f"Quart 1: {quart1}")
# # print(f"Quart 3: {quart3}")
# # print(f"Inter Quart 3: {int_quart}")

# arns = fasta_to_genome("./genome/10000_sequences.fasta")
# stats = perform_all_stats(arns, NUCLEOTIDES)
# print(stats)


# print(f"Moyenne: {stats['moy']}")
# print(f"Mediane: {stats['med']}")
# print(f"ecart type: {stats['ecartt']}")
# print(f"Variance: {stats['var']}")
# print(f"Quart 1: {stats['quart1']}")
# print(f"Quart 3: {stats['quart3']}")
# print(f"Inter Quart 3: {stats['int_quart']}")

# ####################### ACIDES AMINES #######################
# acids = codons_echantillon(arns)
# moy = call_stat(moyenne, acids, AMINO_ACIDS)
# med = call_stat(mediane, acids, AMINO_ACIDS)
# ecartt = call_stat(ecart_type, acids, AMINO_ACIDS)
# var = call_stat(variance, acids, AMINO_ACIDS)
# quart1 = call_stat(quartile, acids, AMINO_ACIDS, 1)
# quart3 = call_stat(quartile, acids, AMINO_ACIDS, 3)
# int_quart = call_stat(intervalle_interquartile, acids, AMINO_ACIDS)

# print(f"Moyenne: {moy}")
# print(f"Mediane: {med}")
# print(f"ecart type: {ecartt}")
# print(f"Variance: {var}")
# print(f"Quart 1: {quart1}")
# print(f"Quart 3: {quart3}")
# print(f"Inter Quart 3: {int_quart}")


# arns = fasta_to_genome("./genome/10000_sequences.fasta")
# stats = perform_all_stats(arns, NUCLEOTIDES)
# print(stats)
#
#
# print(f"Moyenne: {stats['moy']}")
# print(f"Mediane: {stats['med']}")
# print(f"ecart type: {stats['ecartt']}")
# print(f"Variance: {stats['var']}")
# print(f"Quart 1: {stats['quart1']}")
# print(f"Quart 3: {stats['quart3']}")
# print(f"Inter Quart 3: {stats['int_quart']}")
#
# ####################### ACIDES AMINES #######################
# acids = codons_echantillon(arns)
# moy = call_stat(moyenne, acids, AMINO_ACIDS)
# med = call_stat(mediane, acids, AMINO_ACIDS)
# ecartt = call_stat(ecart_type, acids, AMINO_ACIDS)
# var = call_stat(variance, acids, AMINO_ACIDS)
# quart1 = call_stat(quartile, acids, AMINO_ACIDS, 1)
# quart3 = call_stat(quartile, acids, AMINO_ACIDS, 3)
# int_quart = call_stat(intervalle_interquartile, acids, AMINO_ACIDS)
#
# print(f"Moyenne: {moy}")
# print(f"Mediane: {med}")
# print(f"ecart type: {ecartt}")
# print(f"Variance: {var}")
# print(f"Quart 1: {quart1}")
# print(f"Quart 3: {quart3}")
# print(f"Inter Quart 3: {int_quart}")
#
# print(perform_all_stats(fasta_to_genome("./genome/dix_minisequences.fasta"), NUCLEOTIDES))
# print(call_stat(moyenne, fasta_to_genome("./genome/dix_sequences.fasta"), NUCLEOTIDES))


genomes = fasta_to_genome("./genome/dix_sequences.fasta")
codons1, codons2 = codons(genomes[0]), codons(genomes[1])
print(lev_itr(codons1, codons2))

print(lev_itr("Sunday", "Saturday"))


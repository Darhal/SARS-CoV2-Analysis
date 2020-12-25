from src.stats import *
from src.levenshtein import *

arns = fasta_to_genome("genome/dix_sequences.fasta")
stats = perform_all_stats(arns, NUCLEOTIDES)

print(f"Moyenne: {stats['moy']}")
print(f"Mediane: {stats['med']}")
print(f"ecart type: {stats['ecartt']}")
print(f"Variance: {stats['var']}")
print(f"Quart 1: {stats['quart1']}")
print(f"Quart 3: {stats['quart3']}")
print(f"Inter Quart 3: {stats['int_quart']}")

####################### ACIDES AMINES #######################
acids = codons_echantillon(arns)
moy = call_stat(moyenne, acids, AMINO_ACIDS)
med = call_stat(mediane, acids, AMINO_ACIDS)
ecartt = call_stat(ecart_type, acids, AMINO_ACIDS)
var = call_stat(variance, acids, AMINO_ACIDS)
quart1 = call_stat(quartile, acids, AMINO_ACIDS, 1)
quart3 = call_stat(quartile, acids, AMINO_ACIDS, 3)
int_quart = call_stat(intervalle_interquartile, acids, AMINO_ACIDS)

print(f"Moyenne: {moy}")
print(f"Mediane: {med}")
print(f"ecart type: {ecartt}")
print(f"Variance: {var}")
print(f"Quart 1: {quart1}")
print(f"Quart 3: {quart3}")
print(f"Inter Quart 3: {int_quart}")

# arns = fasta_to_genome("../genome/10000_sequences.fasta")
# stats = perform_all_stats(arns, NUCLEOTIDES)
# print(stats)
#
# print(f"Moyenne: {stats['moy']}")
# print(f"Mediane: {stats['med']}")
# print(f"ecart type: {stats['ecartt']}")
# print(f"Variance: {stats['var']}")
# print(f"Quart 1: {stats['quart1']}")
# print(f"Quart 3: {stats['quart3']}")
# print(f"Inter Quart 3: {stats['int_quart']}")

###################### ACIDES AMINES #######################
acids = codons_echantillon(arns)
moy = call_stat(moyenne, acids, AMINO_ACIDS)
med = call_stat(mediane, acids, AMINO_ACIDS)
ecartt = call_stat(ecart_type, acids, AMINO_ACIDS)
var = call_stat(variance, acids, AMINO_ACIDS)
quart1 = call_stat(quartile, acids, AMINO_ACIDS, 1)
quart3 = call_stat(quartile, acids, AMINO_ACIDS, 3)
int_quart = call_stat(intervalle_interquartile, acids, AMINO_ACIDS)

print(f"Moyenne: {moy}")
print(f"Mediane: {med}")
print(f"ecart type: {ecartt}")
print(f"Variance: {var}")
print(f"Quart 1: {quart1}")
print(f"Quart 3: {quart3}")
print(f"Inter Quart 3: {int_quart}")


# arns = fasta_to_genome("../genome/10000_sequences.fasta")
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


###################### ACIDES AMINES #######################
acids = codons_echantillon(arns)
moy = call_stat(moyenne, acids, AMINO_ACIDS)
med = call_stat(mediane, acids, AMINO_ACIDS)
ecartt = call_stat(ecart_type, acids, AMINO_ACIDS)
var = call_stat(variance, acids, AMINO_ACIDS)
quart1 = call_stat(quartile, acids, AMINO_ACIDS, 1)
quart3 = call_stat(quartile, acids, AMINO_ACIDS, 3)
int_quart = call_stat(intervalle_interquartile, acids, AMINO_ACIDS)

print(f"Moyenne: {moy}")
print(f"Mediane: {med}")
print(f"ecart type: {ecartt}")
print(f"Variance: {var}")
print(f"Quart 1: {quart1}")
print(f"Quart 3: {quart3}")
print(f"Inter Quart 3: {int_quart}")


print(perform_all_stats(fasta_to_genome("./genome/dix_minisequences.fasta"), NUCLEOTIDES))
print(call_stat(moyenne, fasta_to_genome("./genome/dix_sequences.fasta"), NUCLEOTIDES))


###################### STATS TAILLE DU ARNm SARS-COV2 ######################
print(perform_all_stats_taille(fasta_to_genome("./genome/dix_sequences.fasta")))
print(perform_all_stats_taille(fasta_to_genome("./genome/200_sequences.fasta")))
print(perform_all_stats_taille(fasta_to_genome("./genome/1000_sequences.fasta")))
print(perform_all_stats_taille(fasta_to_genome("./genome/1000_sequences_janvier_avril_2020.fasta")))
# print(perform_all_stats_taille(fasta_to_genome("./genome/10000_sequences.fasta")))
# print(perform_all_stats_taille(fasta_to_genome("./genome/10000_sequences_janvier_aout_2020.fasta")))


###################### STATS NUCLEOTIDES DU ARNm SARS-COV2 ######################
print(perform_all_stats(fasta_to_genome("./genome/dix_sequences.fasta"), NUCLEOTIDES))
print(perform_all_stats(fasta_to_genome("./genome/200_sequences.fasta"), NUCLEOTIDES))
print(perform_all_stats(fasta_to_genome("./genome/1000_sequences.fasta"), NUCLEOTIDES))
print(perform_all_stats(fasta_to_genome("./genome/1000_sequences_janvier_avril_2020.fasta"), NUCLEOTIDES))
# print(perform_all_stats(fasta_to_genome("./genome/10000_sequences.fasta"), NUCLEOTIDES))
# print(perform_all_stats(fasta_to_genome("./genome/10000_sequences_janvier_aout_2020.fasta"), NUCLEOTIDES))


###################### STATS CODONS DU ARNm SARS-COV2 ######################
print(perform_all_stats(fasta_to_genome("./genome/dix_sequences.fasta"), AMINO_ACIDS))
print(perform_all_stats(fasta_to_genome("./genome/200_sequences.fasta"), AMINO_ACIDS))
print(perform_all_stats(fasta_to_genome("./genome/1000_sequences.fasta"), AMINO_ACIDS))
print(perform_all_stats(fasta_to_genome("./genome/1000_sequences_janvier_avril_2020.fasta"), AMINO_ACIDS))
# print(perform_all_stats(fasta_to_genome("./genome/10000_sequences.fasta"), AMINO_ACIDS))
# print(perform_all_stats(fasta_to_genome("./genome/10000_sequences_janvier_aout_2020.fasta"), AMINO_ACIDS))
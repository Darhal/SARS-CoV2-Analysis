from src.stats import *
from src.levenshtein import *


arns = fasta_to_genome("genome/200_sequences.fasta")


####################### TAILLE DE L'ARNm #######################
stats_taille = perform_all_stats_taille(fasta_to_genome("./genome/200_sequences.fasta"))

print(f"Moyenne: {stats_taille['moy']}")
print(f"Médiane: {stats_taille['med']}")
print(f"écart-type: {stats_taille['ecartt']}")
print(f"Variance: {stats_taille['var']}")
print(f"Quart 1: {stats_taille['quart1']}")
print(f"Quart 3: {stats_taille['quart3']}")
print(f"Interquartile: {stats_taille['int_quart']}")


####################### NUCLEOTIDES #######################
stats_nucleo = perform_all_stats(arns, NUCLEOTIDES)
prop_nucleo = perform_all_stats_prop(arns, NUCLEOTIDES)

print(f"Moyenne: {stats_nucleo['moy']}")
print(f"Médiane: {stats_nucleo['med']}")
print(f"écart-type: {stats_nucleo['ecartt']}")
print(f"Variance: {stats_nucleo['var']}")
print(f"Quart 1: {stats_nucleo['quart1']}")
print(f"Quart 3: {stats_nucleo['quart3']}")
print(f"Interquartile: {stats_nucleo['int_quart']}")

print(f"Moyenne proportions: {prop_nucleo['moy']}")
print(f"Médiane proportions: {prop_nucleo['med']}")

# Pour 10000 séquences
# arns = fasta_to_genome("../genome/10000_sequences.fasta")
# stats = perform_all_stats(arns, NUCLEOTIDES)
# print(stats)
#
# print(f"Moyenne: {stats['moy']}")
# print(f"Médiane: {stats['med']}")
# print(f"écart-type: {stats['ecartt']}")
# print(f"Variance: {stats['var']}")
# print(f"Quart 1: {stats['quart1']}")
# print(f"Quart 3: {stats['quart3']}")
# print(f"Interquartile: {stats['int_quart']}")

####################### ACIDES AMINES #######################
# sans utiliser la fonction perform_all_stats
acids = codons_echantillon(arns)
moy = call_stat(moyenne, acids, AMINO_ACIDS)
med = call_stat(mediane, acids, AMINO_ACIDS)
ecartt = call_stat(ecart_type, acids, AMINO_ACIDS)
var = call_stat(variance, acids, AMINO_ACIDS)
quart1 = call_stat(quartile, acids, AMINO_ACIDS, 1)
quart3 = call_stat(quartile, acids, AMINO_ACIDS, 3)
int_quart = call_stat(intervalle_interquartile, acids, AMINO_ACIDS)

print(f"Moyenne: {moy}")
print(f"Médiane: {med}")
print(f"écart-type: {ecartt}")
print(f"Variance: {var}")
print(f"Quart 1: {quart1}")
print(f"Quart 3: {quart3}")
print(f"Interquartile: {int_quart}")

# stats des proportions codons
prop_acids = perform_all_stats_prop(acids, AMINO_ACIDS)

print(f"Moyenne proportions: {prop_acids['moy']}")
print(f"Médiane proportions: {prop_acids['med']}")


###################### STATS TAILLE DU ARNm SARS-COV2 ######################
perform_all_stats_taille(fasta_to_genome("./genome/dix_sequences.fasta"))
# perform_all_stats_taille(fasta_to_genome("./genome/200_sequences.fasta"))
# perform_all_stats_taille(fasta_to_genome("./genome/1000_sequences.fasta"))
# perform_all_stats_taille(fasta_to_genome("./genome/1000_sequences_janvier_avril_2020.fasta"))
# perform_all_stats_taille(fasta_to_genome("./genome/10000_sequences.fasta"))
# perform_all_stats_taille(fasta_to_genome("./genome/10000_sequences_janvier_aout_2020.fasta"))


###################### STATS NUCLEOTIDES DU ARNm SARS-COV2 ######################
perform_all_stats(fasta_to_genome("./genome/dix_sequences.fasta"), NUCLEOTIDES)
# perform_all_stats(fasta_to_genome("./genome/200_sequences.fasta"), NUCLEOTIDES)
# perform_all_stats(fasta_to_genome("./genome/1000_sequences.fasta"), NUCLEOTIDES)
# perform_all_stats(fasta_to_genome("./genome/1000_sequences_janvier_avril_2020.fasta"), NUCLEOTIDES)
# perform_all_stats(fasta_to_genome("./genome/10000_sequences.fasta"), NUCLEOTIDES)
# perform_all_stats(fasta_to_genome("./genome/10000_sequences_janvier_aout_2020.fasta"), NUCLEOTIDES)


###################### STATS CODONS DU ARNm SARS-COV2 ######################
perform_all_stats(codons_echantillon(fasta_to_genome("./genome/dix_sequences.fasta")), AMINO_ACIDS)
# perform_all_stats(codons_echantillon(fasta_to_genome("./genome/200_sequences.fasta")), AMINO_ACIDS)
# perform_all_stats(codons_echantillon(fasta_to_genome("./genome/1000_sequences.fasta")), AMINO_ACIDS)
# perform_all_stats(codons_echantillon(fasta_to_genome("./genome/1000_sequences_janvier_avril_2020.fasta")), AMINO_ACIDS)
# perform_all_stats(codons_echantillon(fasta_to_genome("./genome/10000_sequences.fasta")), AMINO_ACIDS)
# perform_all_stats(codons_echantillon(fasta_to_genome("./genome/10000_sequences_janvier_aout_2020.fasta")), AMINO_ACIDS)


###################### STATS TAILLE DE CODONS SARS-COV2 ######################
perform_all_stats_taille(codons_echantillon(fasta_to_genome("./genome/dix_sequences.fasta")))
# perform_all_stats_taille(fasta_to_genome("./genome/200_sequences.fasta"))
# perform_all_stats_taille(fasta_to_genome("./genome/1000_sequences.fasta"))
# perform_all_stats_taille(fasta_to_genome("./genome/1000_sequences_janvier_avril_2020.fasta"))
# perform_all_stats_taille(fasta_to_genome("./genome/10000_sequences.fasta"))
# perform_all_stats_taille(fasta_to_genome("./genome/10000_sequences_janvier_aout_2020.fasta"))


###################### STATS PROPORTIONS NUCLEOTIDES DU ARNm SARS-COV2 ######################
perform_all_stats_prop(fasta_to_genome("./genome/dix_sequences.fasta"), NUCLEOTIDES)
# perform_all_stats_prop(fasta_to_genome("./genome/200_sequences.fasta"), NUCLEOTIDES)
# perform_all_stats_prop(fasta_to_genome("./genome/1000_sequences.fasta"), NUCLEOTIDES)
# perform_all_stats_prop(fasta_to_genome("./genome/1000_sequences_janvier_avril_2020.fasta"), NUCLEOTIDES)
# perform_all_stats_prop(fasta_to_genome("./genome/10000_sequences.fasta"), NUCLEOTIDES)
# perform_all_stats_prop(fasta_to_genome("./genome/10000_sequences_janvier_aout_2020.fasta"), NUCLEOTIDES)


###################### STATS PROPORTIONS CODONS DU ARNm SARS-COV2 ######################
perform_all_stats_prop(codons_echantillon(fasta_to_genome("./genome/dix_sequences.fasta")), AMINO_ACIDS)
# perform_all_stats_prop(codons_echantillon(fasta_to_genome("./genome/200_sequences.fasta")), AMINO_ACIDS)
# perform_all_stats_prop(codons_echantillon(fasta_to_genome("./genome/1000_sequences.fasta")), AMINO_ACIDS)
# perform_all_stats_prop(codons_echantillon(fasta_to_genome("./genome/1000_sequences_janvier_avril_2020.fasta")), AMINO_ACIDS)
# perform_all_stats_prop(codons_echantillon(fasta_to_genome("./genome/10000_sequences.fasta")), AMINO_ACIDS)
# perform_all_stats_prop(codons_echantillon(fasta_to_genome("./genome/10000_sequences_janvier_aout_2020.fasta")), AMINO_ACIDS)
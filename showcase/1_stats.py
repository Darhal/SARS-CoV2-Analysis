from src.stats import *

arns = fasta_to_genome("genome/200_sequences.fasta")

####################### TAILLE DE L'ARNm #######################
stats_taille = perform_all_stats_taille(arns)

print("------------- TAILLE DE L'ARNm -------------")
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

print("------------- STATS NUCLEOTIDES -------------")
print(f"Moyenne: {stats_nucleo['moy']}")
print(f"Médiane: {stats_nucleo['med']}")
print(f"écart-type: {stats_nucleo['ecartt']}")
print(f"Variance: {stats_nucleo['var']}")
print(f"Quart 1: {stats_nucleo['quart1']}")
print(f"Quart 3: {stats_nucleo['quart3']}")
print(f"Interquartile: {stats_nucleo['int_quart']}")

print(f"Moyenne proportions: {prop_nucleo['moy']}")
print(f"Médiane proportions: {prop_nucleo['med']}")

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

print("------------- STATS ACIDES AMINES / CODONS -------------")
print(f"Moyenne: {moy}\n")
print(f"Médiane: {med}\n")
print(f"écart-type: {ecartt}\n")
print(f"Variance: {var}\n")
print(f"Quart 1: {quart1}\n")
print(f"Quart 3: {quart3}\n")
print(f"Interquartile: {int_quart}\n")

# stats des proportions codons
prop_acids = perform_all_stats_prop(acids, AMINO_ACIDS)
print(f"Moyenne proportions: {prop_acids['moy']}\n")
print(f"Médiane proportions: {prop_acids['med']}\n")
from src.utility import *
from src.levenshtein import *
from src.codon import *

# sequences10 = fasta_to_genome("../genome/dix_sequences.fasta")
# print(lev_itr(codons(sequences10[0]), codons(sequences10[2])))
# On compare la séquence originelle du génome provenant
# donne le résultat de 8375, vérifié par un calculateur en ligne.


##################### DIFFERENTE PERIODE DIFFERENT LIEU ########################
seqUSAChina = fasta_to_genome("../genome/deux_sequences_china_13012020_usa_18122020.fasta")
print(lev_itr(codons_v2(seqUSAChina[0]), codons_v2(seqUSAChina[1])))
# On compare deux séquences l'une de Chine la séquence 'originelle' de Wuhan de janvier 2020
# et l'autre de USA de décembre 2020,
# le résultat est 555, ceci est vérifié par un calculateur en ligne.

seqUSABrazil = fasta_to_genome("../genome/deux_sequences_usa_california_21122020_brazil_23032020.fasta")
print(lev_itr(codons_v2(seqUSABrazil[0]), codons_v2(seqUSABrazil[1])))
# Deux séquences de USA décembre 2020 et Brésil mars 2020
# le résultat est 18 (vérifié), ceci est petit.



############################# MEME PERIODE ##############################

seqbelger = fasta_to_genome("../genome/deux_sequences_belgium_germany_15122020.fasta")
print(lev_itr(codons_v2(seqbelger[0]), codons_v2(seqbelger[1])))
# On compare deux séquences proches en période (décembre 2020) de Belgium et Germany (pas très éloigné en lieu)
# le résultat est 19 (vérifié), ceci est étonnament petit.

seqUSATunisia = fasta_to_genome("../genome/deux_sequences_usa_16122020_tunisia_15122020.fasta")
print(lev_itr(codons_v2(seqUSATunisia[0]), codons_v2(seqUSATunisia[1])))
# Deux séquences de même période (décembre 2020) mais de lieu différent (USA et Tunisie).
# le résultat de 8458 (vérifié), est très grande.



######################### MEME PERIODE MEME LIEU ##########################

seqUSA = fasta_to_genome("../genome/deux_sequences_usa_18122020.fasta")
print(lev_itr(codons_v2(seqUSA[0]), codons_v2(seqUSA[1])))
# On compare deux séquences de même période (décembre 2020), du même lieu (USA).
# La fonction donne le résultat de 544, ceci est vérifié par un calculateur en ligne.

seqChina = fasta_to_genome("../genome/deux_sequences_china_15052020.fasta")
print(lev_itr(codons_v2(seqChina[0]), codons_v2(seqChina[1])))
# On compare deux séquences de même période (mars 2020), du même lieu (Chine),
# le résultat est 8393 (vérifié), ceci est pour l'instant la plus grande distance (contre intuitivement).
# d'autres tests doivent être réalisé.

seqChina_taiwan = fasta_to_genome("../genome/deux_sequences_taiwan_11122020.fasta")
print(lev_itr(codons_v2(seqChina_taiwan[0]), codons_v2(seqChina_taiwan[1])))
# Deux séquence de même période (décembre 2020) et de même lieu (Chine taïwan),
# le résultat est 19 (vérifié), distance très petite.

seqChina_taiwan_memetaille = fasta_to_genome("./genome/deux_sequences_taiwan_memetaille_11122020.fasta")
print(lev_itr(codons_v2(seqChina_taiwan_memetaille[0]), codons_v2(seqChina_taiwan_memetaille[1])))
# Deux séquence de même taille, de même période (décembre 2020) et de même lieu (Chine taïwan),
# le résultat est 18 (vérifié), distance très petite.

seqUSA_california = fasta_to_genome("../genome/deux_sequences_usa_california_21122020.fasta")
print(lev_itr(codons_v2(seqUSA_california[0]), codons_v2(seqUSA_california[1])))
# On compare deux séquences de même période (décembre 2020), du même lieu (USA Californie).
# La fonction donne le résultat de 8373 (vérifié), ceci est très grand.



############################### MEME LIEU ###################################

seqChina_diffperiode = fasta_to_genome("../genome/deux_sequences_china_13012020_15052020.fasta")
print(lev_itr(codons_v2(seqChina_diffperiode[0]), codons_v2(seqChina_diffperiode[1])))
# Deux séquences du même lieu (en Chine) de période différente (janvier 2020 et mars 2020).
# le résultat est 30 (vérifié), distance très petite.

seqUSA_california_diffperiode = fasta_to_genome("../genome/deux_sequences_usa_california_28012020_21122020.fasta")
print(lev_itr(codons_v2(seqUSA_california_diffperiode[0]), codons_v2(seqUSA_california_diffperiode[1])))
# Deux séquence de même lieu (USA Californie), mais de période différente.
# le résultat est de 21 (vérifié), distance très petite.


#####################################################################################################################
############################## REAPPLICATION AVEC LA NOUVELLE VERSION DE CODONS #####################################
#####################################################################################################################


##################### DIFFERENTE PERIODE DIFFERENT LIEU ########################

seqUSAChina = fasta_to_genome("../genome/deux_sequences_china_13012020_usa_18122020.fasta")

seq_acides_USAChina1 = codons(seqUSAChina[0])
seq_acides_USAChina2 = codons(seqUSAChina[1])
print(lev_itr(seq_acides_USAChina1, seq_acides_USAChina2))
l = []

for i in range(min(len(seq_acides_USAChina1), len(seq_acides_USAChina2))):
        l.append(lev_itr(seq_acides_USAChina1[i], seq_acides_USAChina2[i]))
print (l)

"""
On compare deux séquences l'une de Chine la séquence 'originelle' de Wuhan de janvier 2020
et l'autre de USA de décembre 2020,
le résultat est:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 11, 11, 3, 5, 5, 6, 4, 3, 2, 3, 6, 7, 2, 16, 15, 4, 2, 1, 0,
 5, 13, 12, 7, 20, 20, 3, 11, 12, 3, 3, 3, 4, 5, 8, 7, 13, 11, 10, 4, 4, 4, 4, 4, 1, 2, 3, 9, 10, 2, 9, 8, 4, 5, 11, 10, 
 9, 9, 1, 4, 4, 3, 5, 12, 14, 15, 15, 3, 3, 2, 10, 11, 1, 12, 10, 15, 16, 9, 16, 16, 6, 5, 5, 5, 2, 4, 2, 8, 9, 6, 1, 2, 
 9, 10, 2, 2, 2, 6, 8, 8, 4, 1, 4, 7, 6, 4, 4, 4, 3, 3, 2, 9, 10, 1, 1, 5, 6, 4, 4, 0, 0, 12, 8, 7, 7, 5, 0, 8, 8, 6, 6,
 5, 3, 3, 2, 7, 10, 11, 3, 2, 4, 0, 0, 5, 21, 21, 4, 9, 10, 6, 3, 5, 6, 2, 3, 3, 4, 5, 6, 6, 1, 1, 1, 2, 20, 20, 2, 0, 4,
 4, 7, 7, 14, 14, 8, 9, 1, 1, 4, 4, 7, 8, 7, 7, 7, 6, 5, 1, 1, 2, 3, 7, 13, 14, 7, 7, 4, 4, 3, 17, 17, 4, 7, 7, 2, 2, 2,
 2, 1, 3, 3, 9, 7, 6, 6, 3, 3, 2, 1, 1, 2, 3, 3, 1, 12, 12, 2, 2, 3, 5, 6, 1, 9, 8, 5, 5, 2, 2, 2, 4, 4, 0, 10, 9, 8, 4,
 4, 4, 4, 10, 9, 3, 24, 24, 1, 1, 2, 6, 11, 11, 5, 17, 15, 8, 3, 8, 9, 9, 3, 3, 11, 10, 6, 3, 7, 5, 6, 7, 7, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 6, 6, 7, 7, 7, 2, 5, 6, 6, 7, 3, 3, 4, 5, 21, 19, 14, 14, 13, 11, 3, 32, 32, 4, 1, 13, 11, 12, 12,
 9, 9, 2, 0, 3, 3]
"""

seqUSABrazil = fasta_to_genome("../genome/deux_sequences_usa_california_21122020_brazil_23032020.fasta")

seq_acides_USABrazil1 = codons(seqUSABrazil[0])
seq_acides_USABrazil2 = codons(seqUSABrazil[1])
print(lev_itr(seq_acides_USABrazil1,seq_acides_USABrazil2))
l = []

for i in range(min(len(seq_acides_USABrazil1), len(seq_acides_USABrazil2))):
        l.append(lev_itr(seq_acides_USABrazil1[i], seq_acides_USABrazil2[i]))
print (l)

"""
Deux séquences de USA décembre 2020 et Brésil mars 2020
le résultat est:
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0]
"""

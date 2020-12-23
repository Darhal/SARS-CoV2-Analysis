from src.utility import *
from src.lev import *
from src.codon import *

# sequences10 = fasta_to_genome("genome/dix_sequences.fasta")
# print(lev_itr(codons(sequences10[0]), codons(sequences10[2])))
# On compare la séquence originelle du génome provenant
# donne le résultat de 8375, vérifié par un calculateur en ligne.


##################### DIFFERENTE PERIODE DIFFERENT LIEU ########################

seqUSAChina = fasta_to_genome("genome/deux_sequences_china_13012020_usa_18122020.fasta")
print(lev_itr(codons(seqUSAChina[0]), codons(seqUSAChina[1])))
# On compare deux séquences l'une de Chine la séquence 'originelle' de Wuhan de janvier 2020
# et l'autre de USA de décembre 2020,
# le résultat est 555, ceci est vérifié par un calculateur en ligne.

seqUSABrazil = fasta_to_genome("genome/deux_sequences_usa_california_21122020_brazil_23032020.fasta")
print(lev_itr(codons(seqUSABrazil[0]), codons(seqUSABrazil[1])))
# Deux séquences de USA décembre 2020 et Brésil mars 2020
# le résultat est 18 (vérifié), ceci est petit.



############################# MEME PERIODE ##############################

seqbelger = fasta_to_genome("genome/deux_sequences_belgium_germany_15122020.fasta")
print(lev_itr(codons(seqbelger[0]), codons(seqbelger[1])))
# On compare deux séquences proches en période (décembre 2020) de Belgium et Germany (pas très éloigné en lieu)
# le résultat est 19 (vérifié), ceci est étonnament petit.

seqUSATunisia = fasta_to_genome("genome/deux_sequences_usa_16122020_tunisia_15122020.fasta")
print(lev_itr(codons(seqUSATunisia[0]), codons(seqUSATunisia[1])))
# Deux séquences de même période (décembre 2020) mais de lieu différent (USA et Tunisie).
# le résultat de 8458 (vérifié), est très grande.



######################### MEME PERIODE MEME LIEU ##########################

seqUSA = fasta_to_genome("genome/deux_sequences_usa_18122020.fasta")
print(lev_itr(codons(seqUSA[0]), codons(seqUSA[1])))
# On compare deux séquences de même période (décembre 2020), du même lieu (USA).
# La fonction donne le résultat de 544, ceci est vérifié par un calculateur en ligne.

seqChina = fasta_to_genome("genome/deux_sequences_china_15052020.fasta")
print(lev_itr(codons(seqChina[0]), codons(seqChina[1])))
# On compare deux séquences de même période (mars 2020), du même lieu (Chine),
# le résultat est 8393 (vérifié), ceci est pour l'instant la plus grande distance (contre intuitivement).
# d'autres tests doivent être réalisé.

seqChina_taiwan = fasta_to_genome("genome/deux_sequences_taiwan_11122020.fasta")
print(lev_itr(codons(seqChina_taiwan[0]), codons(seqChina_taiwan[1])))
# Deux séquence de même période (décembre 2020) et de même lieu (Chine taïwan),
# le résultat est 19 (vérifié), distance très petite.

seqChina_taiwan_memetaille = fasta_to_genome("genome/deux_sequences_taiwan_memetaille_11122020.fasta")
print(lev_itr(codons(seqChina_taiwan_memetaille[0]), codons(seqChina_taiwan_memetaille[1])))
# Deux séquence de même taille, de même période (décembre 2020) et de même lieu (Chine taïwan),
# le résultat est 18 (vérifié), distance très petite.

seqUSA_california = fasta_to_genome("genome/deux_sequences_usa_california_21122020.fasta")
print(lev_itr(codons(seqUSA_california[0]), codons(seqUSA_california[1])))
# On compare deux séquences de même période (décembre 2020), du même lieu (USA Californie).
# La fonction donne le résultat de 8373 (vérifié), ceci est très grand.



############################### MEME LIEU ###################################

seqChina_diffperiode = fasta_to_genome("genome/deux_sequences_china_13012020_15052020.fasta")
print(lev_itr(codons(seqChina_diffperiode[0]), codons(seqChina_diffperiode[1])))
# Deux séquences du même lieu (en Chine) de période différente (janvier 2020 et mars 2020).
# le résultat est 30 (vérifié), distance très petite.

seqUSA_california_diffperiode = fasta_to_genome("genome/deux_sequences_usa_california_28012020_21122020.fasta")
print(lev_itr(codons(seqUSA_california_diffperiode[0]), codons(seqUSA_california_diffperiode[1])))
# Deux séquence de même lieu (USA Californie), mais de période différente.
# le résultat est de 21 (vérifié), distance très petite.
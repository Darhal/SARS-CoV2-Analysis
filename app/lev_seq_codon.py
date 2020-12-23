from src.utility import *
from src.lev import *
from src.codon import *

# sequences10 = fasta_to_genome("genome/dix_sequences.fasta")
# print(lev_itr(codons(sequences10[0]), codons(sequences10[2])))
# On compare la séquence originelle du génome provenant
# donne le résultat de 8375, vérifié par un calculateur en ligne.

seqUSA = fasta_to_genome("genome/deux_sequences_usa_18122020.fasta")
print(lev_itr(codons(seqUSA[0]), codons(seqUSA[1])))
# On compare deux séquences proches en période du même lieu, les USA
# La fonction donne le résultat de 544, ceci est vérifié par un calculateur en ligne.

seqUSAChina = fasta_to_genome("genome/deux_sequences_china_13012020_usa_18122020.fasta")
print(lev_itr(codons(seqUSAChina[0]), codons(seqUSAChina[1])))
# On compare deux séquences l'une de Chine la séquence 'originelle' de Wuhan de janvier 2020
# et l'autre de USA de décembre 2020, le résultat est 555, ceci est vérifié par un calculateur en ligne.

seqbelger = fasta_to_genome("genome/deux_sequences_china_13012020_usa_18122020.fasta")
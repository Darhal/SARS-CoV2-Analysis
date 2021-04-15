from src.utility import *
from src.levenshtein import *
from src.codon import *
from multiprocessing import Pool


def affiche_res(L1, L2):
    l1, l2 = meme_taille(L1[:], L2[:])
    l = []

    for i in range(len(l1)):
        l.append(lev(l1[i], l2[i]))

    print(l)


def lev_cod_mt(genome, cap):
    seqUSAChina = fasta_to_genome(genome)
    print(cap+": ", end='')
    print(lev(codons_v2(seqUSAChina[0]), codons_v2(seqUSAChina[1])))


if __name__ == "__main__":
    print("------------------------- LEV SUR CODONS -------------------------")
    ##################### DIFFERENTE PERIODE DIFFERENT LIEU ########################
    seqUSAChina = fasta_to_genome("./genome/deux_sequences_china_13012020_usa_18122020.fasta")
    seq_acides_USAChina1 = codons(seqUSAChina[0])
    seq_acides_USAChina2 = codons(seqUSAChina[1])
    affiche_res(seq_acides_USAChina1, seq_acides_USAChina2)

    ##################### MEME LIEU MEME PERIODE ########################
    seqChina = fasta_to_genome("./genome/deux_sequences_china_15052020.fasta")
    seq_acides_China1 = codons(seqChina[0])
    seq_acides_China2 = codons(seqChina[1])
    affiche_res(seq_acides_China1, seq_acides_China2)

    #------------------------- CODONS V2 -------------------------#
    print("-------------------------- LEV SUR CODONS V2 --------------------------")

    pool = Pool(2)
    pool.starmap(lev_cod_mt, [
        ("./genome/deux_sequences_china_13012020_usa_18122020.fasta", "DIFFERENTE PERIODE DIFFERENT LIEU"), 
        ("./genome/deux_sequences_usa_18122020.fasta", "MEME PERIODE MEME LIEU")
    ]);

    ##################### DIFFERENTE PERIODE DIFFERENT LIEU ########################
    # seqUSAChina = fasta_to_genome("./genome/deux_sequences_china_13012020_usa_18122020.fasta")
    # print(lev(codons_v2(seqUSAChina[0]), codons_v2(seqUSAChina[1])))

    # ######################### MEME PERIODE MEME LIEU ##########################
    # seqUSA = fasta_to_genome("./genome/deux_sequences_usa_18122020.fasta")
    # print(lev(codons_v2(seqUSA[0]), codons_v2(seqUSA[1])))


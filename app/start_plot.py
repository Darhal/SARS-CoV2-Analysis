from matplotlib import pyplot as plt
import numpy as np
from src.stats import *
from src.utility import*

def plot_histo_nb_nucleotide(fasta, nucleotide, précision):
    
    '''Plot un hstogramme du nombre de séquences (ordonnée) en fonction du nombre de nucléotide entré en paramètre qu'elles possèdent (un seul nucléotide), avec un nombre de barres égal à précision '''
    
    #plot_histo_nb_nucleotide('1000_sequences.fasta', 'G', 10000)
    genome = fasta_to_genome(fasta)
    dico = nombre_element_echantillon(genome, [nucleotide])
    
    print("Comptage des nucléotides terminé, calcul des barres pour l'histogramme en cours...")

    minimum = min(dico[nucleotide])
    maximum = max(dico[nucleotide])+1

    nb_tranches = précision

    if nb_tranches > maximum - minimum :
        print('La précision excède la précision maximum ( max = ',maximum - minimum,") pour cet échantillon!\n")
        boolean = input("Ajuster la précision au maximum? (Vivement recommandé y/n \n")

    if nb_tranches < maximum - minimum :
        print("La précision n'est pas maximale pour cet échantillon! ( max = ",maximum - minimum,") \n")
        boolean = input("Ajuster la précision au maximum? (Peut impacter fortement les performances au delà de 10000) y/n \n")
        
    if boolean == 'y':
        nb_tranches = maximum-minimum
        print("précision ajustée, reprise du calcul...")

    taille_tranches = (maximum - minimum)/ nb_tranches

    tranches = [int(minimum + i*taille_tranches) for i in range(nb_tranches)]
    tranches[-1] += 1

    barres = [0 for i in range(nb_tranches)]

    for i in dico[nucleotide]:
        for j in range(nb_tranches):
            if int(minimum + j*taille_tranches) <= i < int(minimum + (j+1)*taille_tranches):
                barres[j] += 1
                break

    plt.bar(tranches,barres)
    plt.show()



def plot_histo_nb_acide(fasta, acide_aminé, précision):
    
    '''Plot un hstogramme du nombre d'Acide aminé saisi (un seul) en entrée pour chaque séquence dans un fichier fasta, avec une précision donnée.'''
    #plot_histo_nb_acide('1000_sequences.fasta', 'M', 100)
    genome = fasta_to_genome(fasta)
    trad = codons_echantillon(genome)
    dico = nombre_element_echantillon(trad, [acide_aminé])

    print("Comptage des acides aminés terminé, calcul des barres pour l'histogramme en cours...")
    
    minimum = min(dico[acide_aminé])
    maximum = max(dico[acide_aminé])+1

    nb_tranches = précision

    if nb_tranches > maximum - minimum :
        print('La précision excède la précision maximum ( max = ',maximum - minimum,") pour cet échantillon!\n")
        boolean = input("Ajuster la précision au maximum? (Vivement recommandé y/n \n")

    if nb_tranches < maximum - minimum :
        print("La précision n'est pas maximale pour cet échantillon! ( max = ",maximum - minimum,") \n")
        boolean = input("Ajuster la précision au maximum? (Peut impacter fortement les performances au delà de 10000) y/n \n")
        
    if boolean == 'y':
        nb_tranches = maximum-minimum
        print("précision ajustée, reprise du calcul...")

    taille_tranches = (maximum - minimum)/ nb_tranches

    tranches = [int(minimum + i*taille_tranches) for i in range(nb_tranches)]
    tranches[-1] += 1

    barres = [0 for i in range(nb_tranches)]

    for i in dico[acide_aminé]:
        for j in range(nb_tranches):
            if int(minimum + j*taille_tranches) <= i < int(minimum + (j+1)*taille_tranches):
                barres[j] += 1
                break

    plt.bar(tranches,barres)
    plt.show()



def plot_histo_taille(fasta, précision):
    
    '''Plot un hstogramme de la taille chaque séquence dans un fichier fasta, avec une précision donnée.'''
    #plot_histo_taille('1000_sequences.fasta', 10000)
    genome = fasta_to_genome(fasta)
    liste = taille_ensemble(genome)

    print("Détermination de la taille des séquences terminé, calcul des barres pour l'histogramme en cours...")

    minimum = min(liste)
    maximum = max(liste)+1
    nb_tranches = précision

    if nb_tranches > maximum - minimum :
        print('La précision excède la précision maximum ( max = ',maximum - minimum,") pour cet échantillon!\n")
        boolean = input("Ajuster la précision au maximum? (Vivement recommandé y/n \n")

    if nb_tranches < maximum - minimum :
        print("La précision n'est pas maximale pour cet échantillon! ( max = ",maximum - minimum,") \n")
        boolean = input("Ajuster la précision au maximum? (Peut impacter fortement les performances au delà de 10000) y/n \n")
        
    if boolean == 'y':
        nb_tranches = maximum-minimum
        print("précision ajustée, reprise du calcul...")

    taille_tranches = (maximum - minimum)/ nb_tranches

    tranches = [int(minimum + i*taille_tranches) for i in range(nb_tranches)]
    tranches[-1] += 1

    barres = [0 for i in range(nb_tranches)]

    for i in liste:
        for j in range(nb_tranches):
            if int(minimum + j*taille_tranches) <= i < int(minimum + (j+1)*taille_tranches):
                barres[j] += 1
                break

    plt.bar(tranches,barres)
    plt.show()



def plot_proportions_nucleotide(fasta, sampler):
    #plot_proportions_nucleotide('1000_sequences.fasta', NUCLEOTIDES)
    genome = fasta_to_genome(fasta)
    dico = call_stat_prop(moyenne, genome, sampler)

    print(dico)

    plt.pie([dico[i] for i in dico if dico[i] != 0], labels = [i for i in dico if dico[i] != 0], autopct='%1.1f%%', startangle=90)

    plt.show()



def plot_proportions_acide(fasta, sampler):
    #plot_proportions_acide('1000_sequences.fasta', AMINO_ACIDS)
    genome = fasta_to_genome(fasta)
    trad = codons_echantillon(genome)
    dico = call_stat_prop(moyenne, trad, sampler)

    plt.pie([dico[i] for i in dico if dico[i] != 0], labels = [i for i in dico if dico[i] != 0], autopct='%1.1f%%', startangle=90, radius =1.3)

    plt.show()

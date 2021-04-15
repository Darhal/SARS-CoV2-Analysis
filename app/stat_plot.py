from matplotlib import pyplot as plt
import numpy as np
from src.stats import *
from src.utility import*

def plot_moyenne_acide(fasta):
    '''Fonction qui trace un histogramme de la moyenne des acides aminés présents dans les séquences du fichier fasta.

    Args:
        fasta : le fichier fasta à étudier

    Returns:
        Un histogramme de la moyenne des acides aminés présents dans les séquences du fichier fasta.
    '''
    
    genome = fasta_to_genome(fasta)
    trad = codons_echantillon(genome)
    dico = call_stat(moyenne, trad, AMINO_ACIDS)

    barwidth = 0.45

    br = np.arange(len(dico)) 

    
    plt.bar([i for i in dico],[dico[i] for i in dico], width = barwidth, label = str(fasta))


    plt.xlabel('Branch', fontweight ='bold') 
    plt.ylabel('Students passed', fontweight ='bold')

    plt.xticks([r + 0.0025 for r in range(len(dico))], 
               [i for i in dico])

    plt.show()

    



def plot_histo_nb_nucleotide(fasta, nucleotide, précision):
    '''Fonction qui trace un histogramme du nombre de séquences d'un fichier fasta en fonction du nombre de nucléotide
    entré en paramètre qu'elle possède.

    Args:
        fasta : le fichier fasta à étudier
        précision : nombre de barres à calculer pour l'histogramme. Plus il y en a, plus l'histogramme est précis
        mais le calcul peut être plus long. Si nécessaire, il sera proposé lors de l'exécution de la fonction d'ajuster
        automatiquement la précision à son maximum.

    Returns:
        Un histogramme présentant les nombre de séquences d'un fichier fasta en fonction du nombre de nucléotide
    entré en paramètre qu'elle possède.
    '''
    #plot_histo_nb_nucleotide('1000_sequences.fasta', 'G', 10000)
    
    
    genome = fasta_to_genome(fasta)
    dico = nombre_element_echantillon(genome, [nucleotide])
    
    print("Comptage des nucléotides terminé, calcul des barres pour l'histogramme en cours...")

    minimum = min(dico[nucleotide])
    maximum = max(dico[nucleotide])+1

    nb_tranches = précision
    boolean = 'y'

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
    plt.xlabel("Nombre de nucléotide '" + nucleotide + "' dans la séquence")
    plt.ylabel('Nombre de séquences')
    plt.title("Nombre de séquences possédant un nombe de nucléotide '" + nucleotide + "' donné pour le fichier '" + fasta +"'")
    plt.show()





def plot_histo_nb_acide(fasta, acide_aminé, précision):
    '''Fonction qui trace un histogramme du nombre de séquences d'un fichier fasta en fonction du nombre d'acide aminé
    entré en paramètre qu'elle possède.

    Args:
        fasta : le fichier fasta à étudier
        précision : nombre de barres à calculer pour l'histogramme. Plus il y en a, plus l'histogramme est précis
        mais le calcul peut être plus long. Si nécessaire, il sera proposé lors de l'exécution de la fonction d'ajuster
        automatiquement la précision à son maximum.

    Returns:
        Un histogramme présentant les nombre de séquences d'un fichier fasta en fonction du nombre d'acide aminé
    entré en paramètre qu'elle possède.
    '''
    
    #exemple : plot_histo_nb_acide('1000_sequences.fasta', 'M', 100)
    genome = fasta_to_genome(fasta)
    trad = codons_echantillon(genome)
    dico = nombre_element_echantillon(trad, [acide_aminé])

    print("Comptage des acides aminés terminé, calcul des barres pour l'histogramme en cours...")
    
    minimum = min(dico[acide_aminé])
    maximum = max(dico[acide_aminé])+1

    nb_tranches = précision
    boolean = 'n'

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
    plt.xlabel("Nombre d'acide aminé '" + acide_aminé + "' dans la séquence")
    plt.ylabel('Nombre de séquences')
    plt.title("Nombre de séquences possédant un nombe d'acide aminé '" + acide_aminé + "' donné pour le fichier '" + fasta +"'")
    plt.show()





def plot_histo_taille_nucl(fasta, précision):

    '''Fonction qui trace un histogramme du nombre de séquences d'un fichier fasta en fonction de la taille de celles-ci
    en nucléotides.

    Args:
        fasta : le fichier fasta à étudier
        précision : nombre de barres à calculer pour l'histogramme. Plus il y en a, plus l'histogramme est précis
        mais le calcul peut être plus long. Si nécessaire, il sera proposé lors de l'exécution de la fonction d'ajuster
        automatiquement la précision à son maximum.

    Returns:
        Un histogramme présentant les nombre de séquences d'un fichier fasta en fonction de la taille de celles-ci
        en nucléotides.
    '''
    
    '''Plot un hstogramme de la taille chaque séquence dans un fichier fasta, avec une précision donnée.'''
    #exemple : plot_histo_taille_nucl('1000_sequences.fasta', 10000)
    genome = fasta_to_genome(fasta)
    liste = taille_ensemble(genome)

    print("Détermination de la taille des séquences terminé, calcul des barres pour l'histogramme en cours...")

    minimum = min(liste)
    maximum = max(liste)+1
    nb_tranches = précision
    boolean = 'n'

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
    plt.xlabel('Taille de la séquence (en nucléotides)')
    plt.ylabel('Nombre de séquences')
    plt.title("Nombre de séquences en fonction de leur taille en nucléotides pour le fichier '" + fasta +"'")
    plt.show()




def plot_histo_taille_acid(fasta, précision):
    '''Fonction qui trace un histogramme du nombre de séquences d'un fichier fasta en fonction de la taille de celles-ci
    en acides aminés.

    Args:
        fasta : le fichier fasta à étudier
        précision : nombre de barres à calculer pour l'histogramme. Plus il y en a, plus l'histogramme est précis
        mais le calcul peut être plus long. Si nécessaire, il sera proposé lors de l'exécution de la fonction d'ajuster
        automatiquement la précision à son maximum.

    Returns:
        Un histogramme présentant les nombre de séquences d'un fichier fasta en fonction de la taille de celles-ci
        en acides aminés.
    '''

    
    #exemple : plot_histo_taille_acid('1000_sequences.fasta', 10000)
    genome = fasta_to_genome(fasta)
    trad = codons_echantillon(genome)
    liste = taille_ensemble(trad)

    print("Détermination de la taille des séquences terminé, calcul des barres pour l'histogramme en cours...")

    minimum = min(liste)
    maximum = max(liste)+1
    nb_tranches = précision
    boolean = 'n'

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
    plt.xlabel('Taille de la séquence (en acides aminés)')
    plt.ylabel('Nombre de séquences')
    plt.title("Nombre de séquences en fonction de leur taille en acides aminés pour le fichier '" + fasta +"'")
    plt.show()





def plot_proportions_nucleotide(fasta, sampler):
    '''Fonction qui trace un diagramme circulaire des proportion moyennes des nucléotides présents dans les séquences
    d'un fichier fasta.

    Args:
        fasta : le fichier fasta à étudier
        sampler : string ou liste comportant les nucléotides à prendre en compte dans le calcul. (Entrer
        sampler = NUCLEOTIDES pour avoir tous les acides aminés.)

    Returns:
        Un diagramme circulaire des proportions moyennes des nucléotides. Si un acide aminé n'apparait pas dans le
        diagramme c'est qu'il n'existe pas dans les séquences étudiées
    '''
    #exemple : plot_proportions_nucleotide('1000_sequences.fasta', NUCLEOTIDES)
    genome = fasta_to_genome(fasta)
    dico = call_stat_prop(moyenne, genome, sampler)

    print(dico)

    plt.pie([dico[i] for i in dico if dico[i] != 0], labels = [i for i in dico if dico[i] != 0], autopct='%1.1f%%', startangle=90)

    plt.title("Diagramme circulaire de la proportion des nucléotides pour le fichier '" + fasta +"'")
    plt.show()





def plot_proportions_acide(fasta, sampler):
    '''Fonction qui trace un diagramme circulaire des proportion moyennes des acides aminés présents dans les séquences
    d'un fichier fasta.

    Args:
        fasta : le fichier fasta à étudier
        sampler : string ou liste comportant les Acides aminés à prendre en compte dans le calcul. (Entrer
        sampler = AMINO_ACIDS pour avoir tous les acides aminés.)

    Returns:
        Un diagramme circulaire des proportions moyennes des acides aminés. Si un acide aminé n'apparait pas dans le
        diagramme c'est qu'il n'existe pas dans les séquences étudiées
    '''
    #exemple : plot_proportions_acide('1000_sequences.fasta', AMINO_ACIDS)
    genome = fasta_to_genome(fasta)
    trad = codons_echantillon(genome)
    dico = call_stat_prop(moyenne, trad, sampler)

    plt.pie([dico[i] for i in dico if dico[i] != 0], labels = [i for i in dico if dico[i] != 0], autopct='%1.1f%%', startangle=90)
    plt.title("Diagramme circulaire de la proportion des acides aminés pour le fichier '" + fasta +"'")
    plt.show()


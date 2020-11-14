from utility import *


def proportions(filename):

    tableau = compteur_bases(fichier)
    
    init = open(fichier, "r")
    sequence = init.read()
    liste_sequence = [base for base in sequence if base != "\n"]
    longueur = len(liste_sequence)

    prop_a = 100*tableau[0][1]/longueur
    prop_c = 100*tableau[1][1]/longueur
    prop_t = 100*tableau[2][1]/longueur
    prop_g = 100*tableau[3][1]/longueur

    print("Proportion de A :",prop_a,"% (",tableau[0][1],"bases / ",longueur,"bases)")
    print("Proportion de C :",prop_c,"% (",tableau[1][1],"bases / ",longueur,"bases)")
    print("Proportion de T :",prop_t,"% (",tableau[2][1],"bases / ",longueur,"bases)")
    print("Proportion de G :",prop_g,"% (",tableau[3][1],"bases / ",longueur,"bases)")


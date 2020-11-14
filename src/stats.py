from utility import *


def proportions(ARNm):
    '''Retourne un dictionaire contenant les proportions des différents nucléotides de la séquence d'ARNm entré.

    Args:
        ARNm : the ARNm sequence (type : string)

    Returns:
        dico_proportions : Dictionnaire associant les proportions aux différentes bases
    '''
    
    
    dico_nombre_nucleotides = nombre_nucleotide(ARNm)
    total_nucleotides = total_nucleotide(ARNm)

    prop_a = 100*dico_nombre_nucleotides["A"]/total_nucleotides
    prop_t = 100*dico_nombre_nucleotides["T"]/total_nucleotides
    prop_g = 100*dico_nombre_nucleotides["G"]/total_nucleotides
    prop_c = 100*dico_nombre_nucleotides["C"]/total_nucleotides

    dico_proportions = {"A" : prop_a, "T" : prop_t, "G" : prop_g, "C" : prop_c}

#    print("Proportion de A :",prop_a,"% (",dico_nombre_nucleotides["A"],"bases / ",total_nucleotides,"bases)")
#    print("Proportion de T :",prop_t,"% (",dico_nombre_nucleotides["T"],"bases / ",total_nucleotides,"bases)")
#    print("Proportion de C :",prop_c,"% (",dico_nombre_nucleotides["C"],"bases / ",total_nucleotides,"bases)")
#    print("Proportion de G :",prop_g,"% (",dico_nombre_nucleotides["G"],"bases / ",total_nucleotides,"bases)\n")

    return dico_proportions

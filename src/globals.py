"""
* All constants must be here & global variables
"""

"""
    * # These are extracted from here: https://courses.lumenlearning.com/wm-biology1/chapter/reading-codons/

    probably using this is better: (https://fr.wikipedia.org/wiki/Code_g%C3%A9n%C3%A9tique)
    Acide aminé : FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
    Initiation  : ···M···············M···············M····························
    1re base    : UUUUUUUUUUUUUUUUCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
    2e base     : UUUUCCCCAAAAGGGGUUUUCCCCAAAAGGGGUUUUCCCCAAAAGGGGUUUUCCCCAAAAGGGG
    3e base     : UCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAG
"""
CODONS_TO_AMINO_ACIDS = {
    # First Column
    "UUU": "F",
    "UUC": "F",
    "UUA": "L",
    "UUG": "L",

    "CUU": "L",
    "CUC": "L",
    "CUA": "L",
    "CUG": "L",

    "AUU": "I",
    "AUC": "I",
    "AUA": "I",
    "AUG": "M",

    "GUU": "V",
    "GUC": "V",
    "GUA": "V",
    "GUG": "V",

    # Second Column
    "UCU": "S",
    "UCC": "S",
    "UCA": "S",
    "UCG": "S",

    "CCU": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",

    "ACU": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",

    "GCU": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",

    # Third Column
    "UAU": "Y",
    "UAC": "Y",
    "UAA": "*",
    "UAG": "*",

    "CAU": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",

    "AAU": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",

    "GAU": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",

    # Fourth Column
    "UGU": "C",
    "UGC": "C",
    "UGA": "*",
    "UGG": "W",

    "CGU": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",

    "AGU": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",

    "GGU": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
}

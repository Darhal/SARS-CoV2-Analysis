"""
    * All constants must be here
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
CODONS_TO_PROTEINS = {
    # First Column
    "UUU": "Phe",
    "UUC": "Phe",
    "UUA": "Leu",
    "UUG": "Leu",

    "CUU": "Leu",
    "CUC": "Leu",
    "CUA": "Leu",
    "CUG": "Leu",

    "AUU": "Ile",
    "AUC": "Ile",
    "AUA": "Ile",
    "AUG": "Met",

    "GUU": "Val",
    "GUC": "Val",
    "GUA": "Val",
    "GUG": "Val",

    # Second Column
    "UCU": "Ser",
    "UCC": "Ser",
    "UCA": "Ser",
    "UCG": "Ser",

    "CCU": "Pro",
    "CCC": "Pro",
    "CCA": "Pro",
    "CCG": "Pro",

    "ACU": "Thr",
    "ACC": "Thr",
    "ACA": "Thr",
    "ACG": "Thr",

    "GCU": "Ala",
    "GCC": "Ala",
    "GCA": "Ala",
    "GCG": "Ala",

    # Third Column
    "UAU": "Tyr",
    "UAC": "Tyr",
    "UAA": "STOP",
    "UAG": "STOP",

    "CAU": "His",
    "CAC": "His",
    "CAA": "Gln",
    "CAG": "Gln",

    "AAU": "Asn",
    "AAC": "Asn",
    "AAA": "Lys",
    "AAG": "Lys",

    "GAU": "Asp",
    "GAC": "Asp",
    "GAA": "Glu",
    "GAG": "Glu",

    # Fourth Column
    "UGU": "Cys",
    "UGC": "Cys",
    "UGA": "STOP",
    "UGG": "Trp",

    "CGU": "Arg",
    "CGC": "Arg",
    "CGA": "Arg",
    "CGG": "Arg",

    "AGU": "Ser",
    "AGC": "Ser",
    "AGA": "Arg",
    "AGG": "Arg",

    "GGU": "Gly",
    "GGC": "Gly",
    "GGA": "Gly",
    "GGG": "Gly",
}
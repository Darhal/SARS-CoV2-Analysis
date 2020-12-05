import pytest

from src.utility import *
from src.globals import *


def test_total_elements():
    assert total_elements('ACU') == 3
    assert total_elements('ACUCU') == 5
    assert total_elements([]) == 0
    assert total_elements('ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAAC') == len('ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAAC')


def test_taille_ensemble():
    assert taille_ensemble([[1, 2, 3, 4, 5], [4, 5, 6, 5, 6, 8, 0, 'a'], ['a', 'b1', 123, 147, 000], [], [''], [1]]) == [5, 8, 5, 0, 1, 1]
    assert taille_ensemble([]) == []
    assert taille_ensemble([[]]) == [0]


def test_nombre_elements():
    assert nombre_elements('ACU', NUCLEOTIDES) == {'A': 1, 'U': 1, 'G': 0, 'C': 1}
    assert nombre_elements('AAA', NUCLEOTIDES) == {'A': 3, 'U': 0, 'G': 0, 'C': 0}
    assert nombre_elements('ACU', NUCLEOTIDES) == {'A': 1, 'U': 1, 'G': 0, 'C': 1}
    assert nombre_elements('ACUGACU', NUCLEOTIDES) == {'A': 2, 'U': 2, 'G': 1, 'C': 2}

    assert nombre_elements('FLIQ', AMINO_ACIDS) == {'A': 0, 'R': 0, 'N': 0, 'D': 0, 'C': 0, 'Q': 1,
                                                  'E': 0, 'G': 0, 'H': 0, 'I': 1, 'L': 1, 'K': 0, 'M': 0,
                                                  'F': 1, 'P': 0, 'O': 0, 'S': 0, 'U': 0, 'T': 0, 'W': 0,
                                                  'Y': 0, 'V': 0, 'B': 0, 'Z': 0, 'X': 0, 'J': 0, '*': 0}

    assert nombre_elements('AAA', AMINO_ACIDS) == {'A': 3, 'R': 0, 'N': 0, 'D': 0, 'C': 0, 'Q': 0,
                                                  'E': 0, 'G': 0, 'H': 0, 'I': 0, 'L': 0, 'K': 0, 'M': 0,
                                                  'F': 0, 'P': 0, 'O': 0, 'S': 0, 'U': 0, 'T': 0, 'W': 0,
                                                  'Y': 0, 'V': 0, 'B': 0, 'Z': 0, 'X': 0, 'J': 0, '*': 0}

    assert nombre_elements('ACV', AMINO_ACIDS) == {'A': 1, 'R': 0, 'N': 0, 'D': 0, 'C': 1, 'Q': 0,
                                                  'E': 0, 'G': 0, 'H': 0, 'I': 0, 'L': 0, 'K': 0, 'M': 0,
                                                  'F': 0, 'P': 0, 'O': 0, 'S': 0, 'U': 0, 'T': 0, 'W': 0,
                                                  'Y': 0, 'V': 1, 'B': 0, 'Z': 0, 'X': 0, 'J': 0, '*': 0}

    assert nombre_elements('ACCSACV', AMINO_ACIDS) == {'A': 2, 'R': 0, 'N': 0, 'D': 0, 'C': 3, 'Q': 0,
                                                      'E': 0, 'G': 0, 'H': 0, 'I': 0, 'L': 0, 'K': 0, 'M': 0,
                                                      'F': 0, 'P': 0, 'O': 0, 'S': 1, 'U': 0, 'T': 0, 'W': 0,
                                                      'Y': 0, 'V': 1, 'B': 0, 'Z': 0, 'X': 0, 'J': 0, '*': 0}



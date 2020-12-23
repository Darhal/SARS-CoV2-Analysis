import pytest

from src.utility import *
from src.globals import *


def test_transcription_complementaire():
    assert transcription_complementaire('') == ''
    assert transcription_complementaire('TCGAT') == 'UCGAU'
    assert transcription_complementaire('T') == 'U'
    assert transcription_complementaire('U') == 'U'
    assert transcription_complementaire('TAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGT') == 'UAAAGGUUUAUACCUUCCCAGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGU'
    assert transcription_complementaire('TTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTA') == 'UUUAUACCUUCCCAGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUCUCUA'
    assert transcription_complementaire('TATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAA') == 'UAUACCUUCCCAGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUCUCUAAA'


def test_fasta_to_genome():
    assert fasta_to_genome("./genome/dix_minisequences.fasta") == ['UAAAGGUUUAUACCUUCCCAGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGU',
                                                                  'UUUAUACCUUCCCAGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUCUCUA',
                                                                  'UAUACCUUCCCAGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUCUCUAAA',
                                                                  'AAGGUUUAUACCUUCCCAGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUC',
                                                                  'GGUUUAUACCUUCCCAGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUCUC',
                                                                  'UACCUUCCCAGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUCUCUAAACG',
                                                                  'GUUUAUACCUUCCCAGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUCUCU',
                                                                  'CAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUCUCUAAACGAACUUUAAAAUCUGU',
                                                                  'AGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUCUCUAAACGAACUUUAAA',
                                                                  'AAGGUUUAUACCUUCCCAGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUC']


def test_total_elements():
    assert total_elements('ACU') == 3
    assert total_elements('ACUCU') == 5
    assert total_elements([]) == 0
    assert total_elements('AUUAAAGGTTTATACCTTCCCAGGTAACAAACCAAC') == len('AUUAAAGGTTTATACCTTCCCAGGTAACAAACCAAC')


def test_taille_ensemble():
    assert taille_ensemble([[1, 2, 3, 4, 5], [4, 5, 6, 5, 6, 8, 0, 'a'], ['a', 'b1', 123, 147, 000], [], [''], [1]]) == [5, 8, 5, 0, 1, 1]
    assert taille_ensemble([]) == []
    assert taille_ensemble([[]]) == [0]
    assert taille_ensemble(['']) == [0]
    assert taille_ensemble(['', []]) == [0, 0]
    assert taille_ensemble(['123', '', '02587', 'azerty', 'QWERTY', ' ', '.']) == [3, 0, 5, 6, 6, 1, 1]
    assert taille_ensemble(['UAAAGGUUUAUACCUUCCCAGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGU',
                            'UUUAUACCUUCCCAGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUCUCUA',
                            'UAUACCUUCCCAGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUCUCUAAA',
                            'AAGGUUUAUACCUUCCCAGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUC',
                            'GGUUUAUACCUUCCCAGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUCUC',
                            'UACCUUCCCAGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUCUCUAAACG',
                            'GUUUAUACCUUCCCAGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUCUCU',
                            'CAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUCUCUAAACGAACUUUAAAAUCUGU',
                            'AGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUCUCUAAACGAACUUUAAA',
                            'AAGGUUUAUACCUUCCCAGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUC']) == [60, 60, 60, 60, 60, 60,
                                                                                                 60, 60, 60, 60]


def test_nombre_elements():
    assert nombre_elements('ACU', NUCLEOTIDES) == {'A': 1, 'U': 1, 'G': 0, 'C': 1}
    assert nombre_elements('AAA', NUCLEOTIDES) == {'A': 3, 'U': 0, 'G': 0, 'C': 0}
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


def test_nombre_element_echantillon():
    assert nombre_element_echantillon(['ACU','AAA','ACUGACU'], NUCLEOTIDES) == {'A': [1, 3, 2], 'U': [1, 0, 2],
                                                                                'G': [0, 0, 1], 'C': [1, 0, 2]}
    assert nombre_element_echantillon([], NUCLEOTIDES) == {}

    assert nombre_element_echantillon(['FLIQ', 'ACCSACV', 'ACV', 'AAA'], AMINO_ACIDS) == {'A': [0, 2, 1, 3], 'R': [0, 0, 0, 0],
                                                    'N': [0, 0, 0, 0], 'D': [0, 0, 0, 0], 'C': [0, 3, 1, 0], 'Q': [1, 0, 0, 0],
                                                    'E': [0, 0, 0, 0], 'G': [0, 0, 0, 0], 'H': [0, 0, 0, 0], 'I': [1, 0, 0, 0],
                                                    'L': [1, 0, 0, 0], 'K': [0, 0, 0, 0], 'M': [0, 0, 0, 0], 'F': [1, 0, 0, 0],
                                                    'P': [0, 0, 0, 0], 'O': [0, 0, 0, 0], 'S': [0, 1, 0, 0], 'U': [0, 0, 0, 0],
                                                    'T': [0, 0, 0, 0], 'W': [0, 0, 0, 0], 'Y': [0, 0, 0, 0], 'V': [0, 1, 1, 0],
                                                    'B': [0, 0, 0, 0], 'Z': [0, 0, 0, 0], 'X': [0, 0, 0, 0], 'J': [0, 0, 0, 0],
                                                    '*': [0, 0, 0, 0]}

    assert nombre_element_echantillon([], AMINO_ACIDS) == {}
    assert nombre_element_echantillon(fasta_to_genome("./genome/dix_minisequences.fasta"), NUCLEOTIDES) == {'A': [18, 16, 18, 17, 15, 17, 15, 19, 21, 17],
                                                                                                        'U': [19, 21, 19, 19, 20, 18, 21, 20, 18, 19],
                                                                                                        'G': [8, 6, 6, 8, 8, 7, 7, 6, 7, 8],
                                                                                                        'C': [15, 17, 17, 16, 17, 18, 17, 15, 14, 16]}
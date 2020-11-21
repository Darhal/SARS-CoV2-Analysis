import pytest

from src.utility import *

def test_total_nucleotide():
    assert total_nucleotide(['A', 'C', 'U']) == 3
    assert total_nucleotide(['A', 'C', 'U','C', 'U']) == 5
    assert total_nucleotide([]) == 0


def test_nombre_nucleotide():
    assert nombre_nucleotide(['A', 'C', 'U']) == {'A': 1, 'U': 1, 'G': 0, 'C': 1}
    assert nombre_nucleotide(['A', 'A', 'A']) == {'A': 3, 'U': 0, 'G': 0, 'C': 0}
    assert nombre_nucleotide(['A', 'C', 'U']) == {'A': 1, 'U': 1, 'G': 0, 'C': 1}
    assert nombre_nucleotide(['A', 'C', 'U', 'G', 'A', 'C', 'U']) == {'A': 2, 'U': 2, 'G': 1, 'C': 2}




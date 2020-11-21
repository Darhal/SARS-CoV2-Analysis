import pytest

from src.utility import *


def test_taille_ensemble():
    assert taille_ensemble([[1, 2, 3, 4, 5], [4, 5, 6, 5, 6, 8, 0, 'a'], ['a', 'b1', 123, 147, 000], [], [''], [1]]) == [5, 8, 5, 0, 1, 1]
    assert taille_ensemble([]) == []
    assert taille_ensemble([[]]) == [0]


def test_total_elements():
    assert total_elements(['A', 'C', 'U']) == 3
    assert total_elements(['A', 'C', 'U','C', 'U']) == 5
    assert total_elements([]) == 0


def test_nombre_elements():
    assert nombre_elements(['A', 'C', 'U']) == {'A': 1, 'U': 1, 'G': 0, 'C': 1}
    assert nombre_elements(['A', 'A', 'A']) == {'A': 3, 'U': 0, 'G': 0, 'C': 0}
    assert nombre_elements(['A', 'C', 'U']) == {'A': 1, 'U': 1, 'G': 0, 'C': 1}
    assert nombre_elements(['A', 'C', 'U', 'G', 'A', 'C', 'U']) == {'A': 2, 'U': 2, 'G': 1, 'C': 2}





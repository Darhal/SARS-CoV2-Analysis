import pytest
import numpy as np

from src.stats import *


def test_taille_ensemble():
    # assert taille_ensenble([[1, 2, 3, 4, 5], [4, 5, 6, 5, 6, 8, 0, 'a'], ['a', 'b1', 123, 147, 000], [], [''], [1]]) == [5, 8, 5, 0, 1, 1]
    # assert taille_ensenble([]) == []
    # assert taille_ensemble([[]]) == [0]
    pass


def test_moyenne(): # on n'a pas test les chaînes de caractère, ou des lites qui n'ont pas comme éléments des nombres
    assert moyenne([1, 2, 3]) == 2
    assert moyenne([]) == None
    assert moyenne([159]) == 159
    assert moyenne([2.5, 2.5, 2.6, 2.7, 2.2, 0]) == np.mean([2.5, 2.5, 2.6, 2.7, 2.2, 0])


def test_mediane():
    assert mediane([1, 2]) == 1.5
    assert mediane([10, 20, 30]) == 20
    assert mediane([0, 0, 0, 1]) == 0
    assert mediane([]) == None
    assert mediane([5, 5, 1]) == 5
    assert mediane([3.5, 2.5]) == 3
    assert mediane([9, 4, 7, 5, 8, 6, 3, 2, 1, 10]) == 5.5


def test_quartile():
    assert quartile(1, []) == None
    assert quartile(5, [1, 2, 3]) == None
    assert quartile(2, [4, 5, 6]) == mediane([4, 5, 6])
    assert quartile(1, [4, 5, 6]) == 4.5
    assert quartile(3, [4, 5, 6]) == 5.5
    assert quartile(2, [9, 8, 7, 6, 5, 4, 3, 2, 1]) == mediane([9, 8, 7, 6, 5, 4, 3, 2, 1])
    assert quartile(1, [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
    assert quartile(3, [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 7
    assert quartile(2, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == mediane([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert quartile(1, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2
    assert quartile(3, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 7
    assert quartile(2, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10]) == mediane([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10])
    assert quartile(1, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10]) == 2.5
    assert quartile(3, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10]) == 7.5
    assert quartile(2, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 11]) == mediane([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 11])
    assert quartile(1, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 11]) == 2.5
    assert quartile(3, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 11]) == 8.5
    assert quartile(2, [1, 1, 3, 3, 5, 5, 5]) == mediane([1, 1, 3, 3, 5, 5, 5])
    assert quartile(1, [1, 1, 3, 3, 5, 5, 5]) == 2
    assert quartile(3, [1, 1, 3, 3, 5, 5, 5]) == 5


def test_variance():
    assert variance([1, 2, 3, 4, 5]) == np.var([1, 2, 3, 4, 5])
    assert variance([]) == None
    assert variance([1]) == 0
    assert variance([5, 5, 5, 5, 5]) == 0
    assert variance([4, 8, 5, 6, 2, 4, 3, 6, 5, 7, 8, 5, 2, 6, 3, 6, 5, 4, 1000, 22, -500, 46, 12, 0, 0, 0]) == np.var([4, 8, 5, 6, 2, 4, 3, 6, 5, 7, 8, 5, 2, 6, 3, 6, 5, 4, 1000, 22, -500, 46, 12, 0, 0, 0])


def test_ecart_type():
    assert ecart_type([4, 8, 5, 6, 2, 4, 3, 6, 5, 7, 8, 5, 2, 6, 3, 6, 5, 4, 1000, 22, -500, 46, 12, 0, 0, 0]) == math.sqrt(np.var([4, 8, 5, 6, 2, 4, 3, 6, 5, 7, 8, 5, 2, 6, 3, 6, 5, 4, 1000, 22, -500, 46, 12, 0, 0, 0]))
    assert ecart_type([1, 2, 3, 4, 5]) == math.sqrt(np.var([1, 2, 3, 4, 5]))


def test_mediane_nucleotide():
    print(mediane_nucleotide(fasta_to_genome("./genome/dix_sequences.fasta")))



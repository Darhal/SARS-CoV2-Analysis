import pytest
import numpy as np
# import statistics as st

from src.stats import *

def test_moyenne(): # on n'a pas test les chaînes de caractère, ou des lites qui n'ont pas comme éléments des nombres
    assert moyenne([1, 2, 3]) == 2
    assert moyenne([]) == None
    assert moyenne([159]) == 159
    assert moyenne([2.5, 2.5, 2.6, 2.7, 2.2, 0]) == np.mean([2.5, 2.5, 2.6, 2.7, 2.2, 0])


def test_mediane(): # les tests ont aussi été fait à la main manuellement sans le module statistics
    assert mediane([1, 2]) == np.median([1, 2])
    assert mediane([10, 20, 30]) == np.median([10, 20, 30])
    assert mediane([0, 0, 0, 1]) == np.median([0, 0, 0, 1])
    assert mediane([]) == None
    assert mediane([5, 5, 1]) == np.median([5, 5, 1])
    assert mediane([3.5, 2.5]) == np.median([3.5, 2.5])
    assert mediane([9, 4, 7, 5, 8, 6, 3, 2, 1, 10]) == np.median([9, 4, 7, 5, 8, 6, 3, 2, 1, 10])


def test_quartile():
    assert quartile([], 1) == None
    assert quartile([1, 2, 3], 5) == None
    assert quartile([4, 5, 6], 2) == mediane([4, 5, 6])
    assert quartile([4, 5, 6], 1) == np.quantile([4, 5, 6], 0.25, interpolation="lower")
    assert quartile([4, 5, 6], 3) == np.quantile([4, 5, 6], 0.75, interpolation="higher")
    assert quartile([30, 90, 95, 100], 1) == np.quantile([30, 90, 95, 100], 0.25, interpolation="lower")
    assert quartile([30, 90, 95, 100], 3) == np.quantile([30, 90, 95, 100], 0.75, interpolation="higher")
    assert quartile([9, 8, 7, 6, 5, 4, 3, 2, 1], 2) == mediane([9, 8, 7, 6, 5, 4, 3, 2, 1])
    assert quartile([9, 8, 7, 6, 5, 4, 3, 2, 1], 1) == np.quantile([9, 8, 7, 6, 5, 4, 3, 2, 1], 0.25, interpolation="lower")
    assert quartile([9, 8, 7, 6, 5, 4, 3, 2, 1], 3) == np.quantile([9, 8, 7, 6, 5, 4, 3, 2, 1], 0.75, interpolation="higher")
    assert quartile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 2) == mediane([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert quartile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 1) == np.quantile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 0.25, interpolation="lower")
    assert quartile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 3) == np.quantile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 0.75, interpolation="higher")
    assert quartile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10], 2) == mediane([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10])
    assert quartile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10], 1) == np.quantile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10], 0.25, interpolation="lower")
    assert quartile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10], 3) == np.quantile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10], 0.75, interpolation="higher")
    assert quartile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 11], 2) == mediane([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 11])
    assert quartile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 11], 1) == np.quantile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 11], 0.25, interpolation="lower")
    assert quartile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 11], 3) == np.quantile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 11], 0.75, interpolation="higher")
    assert quartile([1, 1, 3, 3, 5, 5, 5], 2) == mediane([1, 1, 3, 3, 5, 5, 5])
    assert quartile([1, 1, 3, 3, 5, 5, 5], 1) == np.quantile([1, 1, 3, 3, 5, 5, 5], 0.25, interpolation="lower")
    assert quartile([1, 1, 3, 3, 5, 5, 5], 3) == np.quantile([1, 1, 3, 3, 5, 5, 5], 0.75, interpolation="higher")


def test_intervalle_interquartile():
    assert intervalle_interquartile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == np.quantile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 0.75, interpolation="higher")-np.quantile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 0.25, interpolation="lower")
    assert intervalle_interquartile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10]) == np.quantile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10], 0.75, interpolation="higher")-np.quantile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10], 0.25, interpolation="lower")
    assert intervalle_interquartile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 11]) == np.quantile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 11], 0.75, interpolation="higher")-np.quantile([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 11], 0.25, interpolation="lower")
    assert intervalle_interquartile([1, 1, 3, 3, 5, 5, 5]) == np.quantile([1, 1, 3, 3, 5, 5, 5], 0.75, interpolation="higher")-np.quantile([1, 1, 3, 3, 5, 5, 5], 0.25, interpolation="lower")
    assert intervalle_interquartile([9, 8, 7, 6, 5, 4, 3, 2, 1]) == np.quantile([9, 8, 7, 6, 5, 4, 3, 2, 1], 0.75, interpolation="higher")-np.quantile([9, 8, 7, 6, 5, 4, 3, 2, 1], 0.25, interpolation="lower")


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
    # print(mediane_nucleotide(fasta_to_genome("./genome/dix_sequences.fasta")))
    pass



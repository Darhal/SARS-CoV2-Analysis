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


def test_call_stat_on_echantillon():
    assert call_stat_on_echantillon(moyenne, {'A': [1, 3, 2], 'U': [1, 0, 2], 'G': [0, 0, 1], 'C': [1, 0, 2]}) == {
        'A': np.mean([1, 3, 2]),'U': np.mean([1, 0, 2]),'G': np.mean([0, 0, 1]), 'C': np.mean([1, 0, 2])}

    assert call_stat_on_echantillon(moyenne, {'A': [0, 0, 0], 'U': [0, 0, 0], 'G': [0, 0, 0], 'C': [0, 0, 0]}) == {
        'A': 0, 'U': 0, 'G': 0, 'C': 0}

    assert call_stat_on_echantillon(mediane, {'A': [1, 3, 2], 'U': [1, 0, 2], 'G': [0, 0, 1], 'C': [1, 0, 2]}) == {
        'A': np.median([1, 3, 2]),'U': np.median([1, 0, 2]), 'G': np.median([0, 0, 1]), 'C': np.median([1, 0, 2])}

    assert call_stat_on_echantillon(mediane, {'A': [0, 0, 0], 'U': [0, 0, 0], 'G': [0, 0, 0],'C': [0, 0, 0]}) == {
        'A': 0, 'U': 0, 'G': 0, 'C': 0}

    assert call_stat_on_echantillon(variance, {'A': [0, 0, 0], 'U': [0, 0, 0], 'G': [0, 0, 0], 'C': [0, 0, 0]}) == {
        'A': 0, 'U': 0, 'G': 0, 'C': 0}

    assert call_stat_on_echantillon(variance, {'A': [2, 2, 2], 'U': [0, 0, 0], 'G': [1, 1, 1], 'C': [8, 8, 8]}) == {
        'A': 0, 'U': 0, 'G': 0, 'C': 0}

    assert call_stat_on_echantillon(variance, {'A': [5, 2, 8], 'U': [0, 4, 0], 'G': [1, 17, 1], 'C': [817, 14, 8]}) == {
        'A': np.var([5, 2, 8]), 'U': np.var([0, 4, 0]), 'G': np.var([1, 17, 1]), 'C': np.var([817, 14, 8])}

    assert call_stat_on_echantillon(ecart_type, {'A': [5, 2, 8], 'U': [0, 4, 0], 'G': [1, 17, 1], 'C': [817, 14, 8]}) == {
        'A': np.sqrt(np.var([5, 2, 8])), 'U': np.sqrt(np.var([0, 4, 0])), 'G': np.sqrt(np.var([1, 17, 1])), 'C': np.sqrt(np.var([817, 14, 8]))}

    assert call_stat_on_echantillon(ecart_type, {'A': [2, 2, 2], 'U': [0, 0, 0], 'G': [1, 1, 1], 'C': [8, 8, 8]}) == {
        'A': 0, 'U': 0, 'G': 0, 'C': 0}

    assert call_stat_on_echantillon(quartile, {'A': [4, 5, 6], 'U': [8, 4, 15], 'G': [1, 1, 1], 'C': [18, 8, 156]}, 1) == {
                'A': np.quantile([4, 5, 6], 0.25, interpolation="lower"),
                'U': np.quantile([8, 4, 15], 0.25, interpolation="lower"),
                'G': np.quantile([1, 1, 1], 0.25, interpolation="lower"),
                'C': np.quantile([18, 8, 156], 0.25, interpolation="lower")
                }

    assert call_stat_on_echantillon(quartile, {'A': [4, 5, 6], 'U': [8, 4, 15], 'G': [1, 1, 1], 'C': [18, 8, 156]}, 3) == {
                'A': np.quantile([4, 5, 6], 0.75, interpolation="higher"),
                'U': np.quantile([8, 4, 15], 0.75, interpolation="higher"),
                'G': np.quantile([1, 1, 1], 0.75, interpolation="higher"),
                'C': np.quantile([18, 8, 156], 0.75, interpolation="higher")
                }

    assert call_stat_on_echantillon(intervalle_interquartile, {'A': [4, 5, 6], 'U': [8, 4, 15], 'G': [1, 1, 1], 'C': [18, 8, 156]}) == {
                'A': intervalle_interquartile([4, 5, 6]),
                'U': intervalle_interquartile([8, 4, 15]),
                'G': intervalle_interquartile([1, 1, 1]),
                'C': intervalle_interquartile([18, 8, 156])
                }


def test_proportions():
    assert proportions('AUGC', ['A', 'U', 'G', 'C']) == {'A': 0.25, 'U': 0.25, 'G': 0.25, 'C': 0.25}
    assert proportions('', ['A', 'U', 'G', 'C']) == {'A': 0, 'U': 0, 'G': 0, 'C': 0}
    assert proportions('AAAA', ['A', 'U', 'G', 'C']) == {'A': 1, 'U': 0, 'G': 0, 'C': 0}
    assert proportions('AAAAAAA', ['U', 'G', 'C']) == {'U': 0, 'G': 0, 'C': 0}
    assert proportions('UGCC', ['A', 'U', 'G', 'C']) == {'A' : 0, 'U': 0.25, 'G': 0.25, 'C': 0.5}


def test_call_stat_taille_genome():
    assert call_stat(mediane, fasta_to_genome("./genome/dix_sequences.fasta"),NUCLEOTIDES) == {'A': 8951.0, 'U': 9601.0, 'G': 5857.5, 'C': 5485.5}


def test_perform_all_stats_taille():
    assert perform_all_stats_taille(fasta_to_genome("./genome/dix_sequences.fasta")) == {'moy': 29892.9,
                                                                                         'med': 29895.5,
                                                                                         'ecartt': 7.608547824650905,
                                                                                         'var': 57.89000000000001,
                                                                                         'quart1': 29891,
                                                                                         'quart3': 29899,
                                                                                         'int_quart': 8}


def test_call_stat():
    assert call_stat(mediane, fasta_to_genome("./genome/dix_sequences.fasta"),NUCLEOTIDES) == {'A': 8951.0, 'U': 9601.0, 'G': 5857.5, 'C': 5485.5}
    assert call_stat(moyenne, fasta_to_genome("./genome/dix_minisequences.fasta"), NUCLEOTIDES) == {'A': 17.3, 'U': 19.4, 'G': 7.1, 'C': 16.2}
    assert call_stat(mediane, fasta_to_genome("./genome/dix_minisequences.fasta"), NUCLEOTIDES) == {'A': 17.0, 'U': 19.0, 'G': 7.0, 'C': 16.5}
    assert call_stat(variance, fasta_to_genome("./genome/dix_minisequences.fasta"), NUCLEOTIDES) == {'A': 3.01, 'U': 1.0399999999999998, 'G': 0.69, 'C': 1.36}
    assert call_stat(ecart_type, fasta_to_genome("./genome/dix_minisequences.fasta"), NUCLEOTIDES) == {'A': 1.7349351572897471, 'U': 1.0198039027185568, 'G': 0.8306623862918074, 'C': 1.1661903789690602}
    assert call_stat(quartile, fasta_to_genome("./genome/dix_minisequences.fasta"), NUCLEOTIDES, 1) == {'A': 16, 'U': 19, 'G': 6, 'C': 15}
    assert call_stat(quartile, fasta_to_genome("./genome/dix_minisequences.fasta"), NUCLEOTIDES, 3) == {'A': 18, 'U': 20, 'G': 8, 'C': 17}
    assert call_stat(intervalle_interquartile, fasta_to_genome("./genome/dix_minisequences.fasta"), NUCLEOTIDES) == {'A': 2, 'U': 1, 'G': 2, 'C': 2}


def test_call_stat_prop():
    #Inutile de tester par rapport au résultat (fait ailleurs) mais par rapport au bon fonctionnement de la fonction.
    assert call_stat_prop(moyenne, ['AU','GC','ACUG'], ['A','U','G','C']) == {'A': 0.25, 'U': 0.25, 'G': 0.25, 'C': 0.25}
    assert call_stat_prop(mediane, ['AU','GC','ACUG'], ['A','U','G','C']) == {'A': 0.25, 'U': 0.25, 'G': 0.25, 'C': 0.25}
    assert call_stat_prop(quartile, ['AU','GC','ACUG'], ['A','U','G','C'], 1) == {'A': 0.0, 'U': 0.0, 'G': 0.0, 'C': 0.0}
    assert call_stat_prop(quartile, ['AU','GC','ACUG'], ['A','U','G','C'], 3) == {'A': 0.5, 'U': 0.5, 'G': 0.5, 'C': 0.5}
    assert call_stat_prop(intervalle_interquartile, ['AU','GC','ACUG'], ['A','U','G','C']) == {'A': 0.5, 'U': 0.5, 'G': 0.5, 'C': 0.5}
    assert call_stat_prop(variance, ['AGUC','ACUG'], ['A','U','G','C']) == {'A': 0.0, 'U': 0.0, 'G': 0.0, 'C': 0.0}
    assert call_stat_prop(ecart_type, ['AGUC','ACUG'], ['A','U','G','C']) == {'A': 0.0, 'U': 0.0, 'G': 0.0, 'C': 0.0}


def test_perform_all_stats():
    assert perform_all_stats(fasta_to_genome("./genome/dix_minisequences.fasta"), NUCLEOTIDES) == {'moy': {'A': 17.3, 'U': 19.4, 'G': 7.1, 'C': 16.2},
                                                                                                   'med': {'A': 17.0, 'U': 19.0, 'G': 7.0, 'C': 16.5},
                                                                                                   'ecartt': {'A': 1.7349351572897471, 'U': 1.0198039027185568, 'G': 0.8306623862918074, 'C': 1.1661903789690602},
                                                                                                   'var': {'A': 3.01, 'U': 1.0399999999999998, 'G': 0.69, 'C': 1.36},
                                                                                                   'quart1': {'A': 16, 'U': 19, 'G': 6, 'C': 15},
                                                                                                   'quart3': {'A': 18, 'U': 20, 'G': 8, 'C': 17},
                                                                                                   'int_quart': {'A': 2, 'U': 1, 'G': 2, 'C': 2}}

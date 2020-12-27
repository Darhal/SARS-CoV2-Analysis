import pytest
from src.needleman import *
from collections import * 
from Bio import pairwise2

# Test cases for needleman (Q7)
TEST_CASES_V1 = [
    # Function input and result
    [ [ "ATGCT", "AGCT",  [1, -1, -2] ], [ "ATGCT", "A-GCT", 2 ] ],
    [ [ "ATCGGAG", "ATGGCAA",  [1, -1, -1] ], [ "ATCGG-AG", "AT-GGCAA", 2 ] ],
]

# Test cases for needleman all (both versions) (Q9/Q7)
TEST_CASES_V2 = [
    [
        [ "GCATGCU", "GATTACA", [1, -1, -1] ], # Function inputs
        # All solutions
        [
            ["GCATG-CU", "G-ATTACA", 0],
            ["GCA-TGCU", "G-ATTACA", 0],
            ["GCAT-GCU", "G-ATTACA", 0],
        ]
    ],
    # [
    #     [ "ATCGGAG", "ATGGCAA", [1, -1, -1] ],
    #     [
    #         ["ATCGG-AG", "AT-GGCAA", 2],
    #     ]
    # ],
]

TEST_CASES_V3 = [
    [
        [ "ABC", "ABC", [1, 2, 3, 1, 2, 3, 1, 2, 3, 4], "ABC" ],
        [

            ['-ABC', 'A-BC', 7], 
            ['-ABC', 'ABC-', 7], 
            ['-AB-A-BC', 'A--ABB-C', 7], 
            ['-AB-A-BC', 'A--ABB-C', 7], 
            ['A-BC', '-ABC', 7], 
            ['--ABC', 'ABC--', 7], 
            ['-A---ABC', 'A-ABB-C-', 7], 
            ['-A---ABC', 'A-ABB-C-', 7], 
            ['-A---A-BC', 'A-ABB-B-C', 7], 
            ['-A---A-BC', 'A-ABB-B-C', 7], 
            ['AB--A-BC', '--AABB-C', 7], 
            ['A-B-A-BC', '-A-ABB-C', 7], 
            ['A----ABC', '-AABB-C-', 7], 
            ['A----A-BC', '-AABB-B-C', 7]
        ]
    ],
]

def test_needlman():
    for t in TEST_CASES_V1:
        m = needleman(t[0][0], t[0][1], t[0][2])
        assert m[0] == t[1][0] and m[1] == t[1][1] and m[2] == t[1][2]

def test_needlman_generic():
    for t in TEST_CASES_V2:
        m = needleman(t[0][0], t[0][1], t[0][2])
        # assert m in t[1]

def test_needlman_all():
    for t in TEST_CASES_V2:
        m1 = needleman_all(t[0][0], t[0][1], t[0][2])
        alignments = pairwise2.align.globalms(t[0][0], t[0][1], t[0][2][0], t[0][2][1], t[0][2][2], 0)
        formated_alignments = [ [ a[0], a[1], int(a[2]) ] for a in alignments ]
        print(formated_alignments)
        assert sorted(m1) == sorted(t[1]) == sorted(formated_alignments)

def test_needlman_generic_mat_cout():
    for t in TEST_CASES_V3:
        m = needleman(t[0][0], t[0][1], cost_mat=t[0][2], key=t[0][3])
        # assert m in t[1]

def test_needlman_all_mat_cout():
    for t in TEST_CASES_V3:
        m1 = needleman_all(t[0][0], t[0][1], cost_mat=t[0][2], key=t[0][3])
        # assert sorted(m1) == sorted(t[1])
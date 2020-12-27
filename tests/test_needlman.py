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
        # Function inputs
        [ "GCATGCU", "GATTACA", [1, -1, -1] ], 
        # All solutions
        [
            ["GCATG-CU", "G-ATTACA", 0],
            ["GCA-TGCU", "G-ATTACA", 0],
            ["GCAT-GCU", "G-ATTACA", 0],
        ]
    ],
    [
        [ "ATCGGAG", "ATGGCAA", [1, -1, -1] ],
        [
            ["ATCGG-AG", "AT-GGCAA", 2],
        ]
    ],
    # [
    #     [ "GAAT", "GGAT", [1, 0, 0] ],
    #     [
    #         ['GAAT', 'GGAT', 3],
    #         ['-GAAT', 'GGA-T', 3],
    #         ['-GAAT', 'GG-AT', 3],
    #         ['GA-AT', 'G-GAT', 3],
    #         ['G-AAT', 'GGA-T', 3],
    #         ['G-AAT', 'GG-AT', 3],
    #     ]
    # ]
]

TEST_CASES_V3 = [
    [
        [ "ABC", "ABC", [1, 2, 3, 1, 2, 3, 1, 2, 3, 0], "ABC" ],
        [
            ['ABC', 'ABC', 6],
        ]
    ],
]

def test_needlman():
    for t in TEST_CASES_V1:
        #----------- Our Implementation -----------
        m = needleman(t[0][0], t[0][1], t[0][2])
        #---------------- Bio Seq -----------------
        alignments = pairwise2.align.globalms(t[0][0], t[0][1], t[0][2][0], t[0][2][1], t[0][2][2], t[0][2][2])
        formated_alignments = [ [ a[0], a[1], int(a[2]) ] for a in alignments ]
        #------------------ Test ------------------
        assert m[0] == t[1][0] and m[1] == t[1][1] and m[2] == t[1][2]
        assert m in formated_alignments

def test_needlman_generic():
    for t in TEST_CASES_V2:
        #----------- Our Implementation -----------
        m = needleman(t[0][0], t[0][1], t[0][2])
        #---------------- Bio Seq -----------------
        alignments = pairwise2.align.globalms(t[0][0], t[0][1], t[0][2][0], t[0][2][1], t[0][2][2], t[0][2][2])
        formated_alignments = [ [ a[0], a[1], int(a[2]) ] for a in alignments ]
        #------------------ Test ------------------
        assert m in t[1]
        assert m in formated_alignments

def test_needlman_all():
    for t in TEST_CASES_V2:
        #----------- Our Implementation -----------
        m1 = needleman_all(t[0][0], t[0][1], t[0][2])
        #---------------- Bio Seq -----------------
        alignments = pairwise2.align.globalms(t[0][0], t[0][1], t[0][2][0], t[0][2][1], t[0][2][2], t[0][2][2])
        formated_alignments = [ [ a[0], a[1], int(a[2]) ] for a in alignments ]
        #------------------ Test ------------------
        assert sorted(m1) == sorted(t[1]) == sorted(formated_alignments)

def test_needlman_generic_mat_cout():
    for t in TEST_CASES_V3:
        #----------- Our Implementation -----------
        m = needleman(t[0][0], t[0][1], cost_mat=t[0][2], key=t[0][3])
         #---------------- Bio Seq ----------------
        matrix = {}
        cle = t[0][3]
        mat = t[0][2]
        for i in range(0, len(cle)):
            for j in range(0, len(cle)):
                matrix[(cle[i], cle[j])] = mat[i * len(cle) + j]
        alignments = pairwise2.align.globaldx(t[0][0], t[0][1], matrix)
        formated_alignments = [ [ a[0], a[1], int(a[2]) ] for a in alignments ]
        #------------------ Test ------------------
        assert m in t[1]
        assert m in formated_alignments

def test_needlman_all_mat_cout():
    for t in TEST_CASES_V3:
        #----------- Our Implementation -----------
        m1 = needleman_all(t[0][0], t[0][1], cost_mat=t[0][2], key=t[0][3])
        #---------------- Bio Seq -----------------
        matrix = {}
        cle = t[0][3]
        mat = t[0][2]
        for i in range(0, len(cle)):
            for j in range(0, len(cle)):
                matrix[(cle[i], cle[j])] = mat[i * len(cle) + j]
        alignments = pairwise2.align.globaldx(t[0][0], t[0][1], matrix)
        formated_alignments = [ [ a[0], a[1], int(a[2]) ] for a in alignments ]
        #------------------ Test ------------------
        assert sorted(m1) == sorted(t[1]) == sorted(formated_alignments)
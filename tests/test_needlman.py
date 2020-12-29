import pytest
from src.needleman import *
from collections import * 
from Bio import pairwise2

# Test cases for needleman (Q7)
TEST_CASES_V1 = [
    # Function input and result
    [ "ATGCT", "AGCT",  [1, -1, -2] ],
    [ "ATCGGAG", "ATGGCAA",  [1, -1, -1] ],
]

# Test cases for needleman all (both versions) (Q9/Q7)
TEST_CASES_V2 = [
    # Function inputs
    [ "GCATGCU", "GATTACA", [1, -1, -1] ], 
    [ "ATCGGAG", "ATGGCAA", [1, -1, -1] ],
    [ "GAAT", "GGAT", [1, 0, 0] ],
]

TEST_CASES_V3 = [
    [ "ABC", "ABC", [1, 2, 3, 1, 2, 3, 1, 2, 3, 0], "ABC" ],
]

def test_needlman():
    for t in TEST_CASES_V1:
        #----------- Our Implementation -----------
        m = needleman(t[0], t[1], t[2])
        #---------------- Bio Seq -----------------
        m2 = nw_bio(t[0], t[1], t[2])
        #------------------ Test ------------------
        assert m in m2

def test_needlman_generic():
    for t in TEST_CASES_V2:
        #----------- Our Implementation -----------
        m = needleman(t[0], t[1], t[2])
        #---------------- Bio Seq -----------------
        m2 = nw_bio(t[0], t[1], t[2])
        #------------------ Test ------------------
        assert m in m2

def test_needlman_all():
    for t in TEST_CASES_V2:
        #----------- Our Implementation -----------
        m1 = needleman_all(t[0], t[1], t[2])
        #---------------- Bio Seq -----------------
        m2 = nw_bio(t[0], t[1], t[2])
        #------------------ Test ------------------
        assert sorted(m1) == sorted(m2)

def test_needlman_generic_mat_cout():
    for t in TEST_CASES_V3:
        #----------- Our Implementation -----------
        m = needleman(t[0], t[1], cost_mat=t[2], key=t[3])
        #---------------- Bio Seq ----------------
        matrix = {}
        cle = t[3]
        mat = t[2]
        for i in range(len(cle)):
            for j in range(0, len(cle)):
                matrix[(cle[i], cle[j])] = mat[i * len(cle) + j]
        alignments = pairwise2.align.globalds(t[0], t[1], matrix, t[2][len(cle)**2], t[2][len(cle)**2])
        formated_alignments = [ [ a[0], a[1], int(a[2]) ] for a in alignments ]
        #------------------ Test ------------------
        assert m in formated_alignments

def test_needlman_all_mat_cout():
    for t in TEST_CASES_V3:
        #----------- Our Implementation -----------
        m1 = needleman_all(t[0], t[1], cost_mat=t[2], key=t[3])
        #---------------- Bio Seq -----------------
        matrix = {}
        cle = t[3]
        mat = t[2]
        for i in range(len(cle)):
            for j in range(0, len(cle)):
                matrix[(cle[i], cle[j])] = mat[i * len(cle) + j]
        alignments = pairwise2.align.globalds(t[0], t[1], matrix, t[2][len(cle)**2], t[2][len(cle)**2])
        formated_alignments = [ [ a[0], a[1], int(a[2]) ] for a in alignments ]
        #------------------ Test ------------------
        assert sorted(m1) == sorted(formated_alignments)
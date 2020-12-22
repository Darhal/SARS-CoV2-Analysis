import pytest
from src.needleman import *
from collections import * 

TEST_CASES_V1 = [
    [ [ "ATGCT", "AGCT",  [1, -1, -2] ], [ "ATGCT", "A-GCT", 2 ] ],
    [ [ "ATCGGAG", "ATGGCAA",  [1, -1, -1] ], [ "ATCGG-AG", "AT-GGCAA", 2 ] ]
]

TEST_CASES_V2 = [
    [
        [ "GCATGCU", "GATTACA", [1, -1, -1] ],
        [
            ["GCATG-CU", "G-ATTACA", 0],
            ["GCA-TGCU", "G-ATTACA", 0],
            ["GCAT-GCU", "G-ATTACA", 0]
        ]
    ],
]

def test_needlman():
    for t in TEST_CASES_V1:
        m = needleman(t[0][0], t[0][1], t[0][2])
        assert m[0] == t[1][0] and m[1] == t[1][1] and m[2] == t[1][2]

def test_needlman_all():
    for t in TEST_CASES_V2:
        m1 = needleman_all(t[0][0], t[0][1], t[0][2])
        m2 = needleman_all_v2(t[0][0], t[0][1], t[0][2])
        assert sorted(m1) == sorted(m2) == sorted(t[1])
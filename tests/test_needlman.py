import pytest
from src.needleman import *

TEST_CASES_V1 = [
    [ [ "ATGCT", "AGCT",  [1, -1, -2] ], [ "ATGCT", "A-GCT", 2 ] ],
    [ [ "ATCGGAG", "ATGGCAA",  [1, -1, -1] ], [ "ATCGG-AG", "AT-GGCAA", 2 ] ]
]

def test_needlman():
    for t in TEST_CASES_V1:
        m = needleman(t[0][0], t[0][1], t[0][2])
        assert m[0] == t[1][0] and m[1] == t[1][1] and m[2] == t[1][2]

def test_needlman_all():
    pass
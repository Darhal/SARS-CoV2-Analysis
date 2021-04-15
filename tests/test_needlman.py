import pytest
from src.needleman import *
from collections import * 
from Bio import pairwise2
from src.globals import *

# used to generate bunch of random arguments for testing
from src.performance import * 

# Settings for randomly generated arguments tests
# If you want tests to run quickly then you should modify these 
# you can also set EPOCHS to 0 to completely turn them off:
# TOTAL_TESTS_PER_FUNCTION = FUNC_RUNS * EPOCHS
EPOCHS = 10         # How many times we test iterations we should run per function
NW_RUNS = 10        # How many arguments we will generate per epoch for needleman (fast)
NW_ALL_RUNS = 7     # How many arguments we will generate per epoch for needleman_all (slow)

# Test cases for needleman (both versions) (Q9/Q7)
TEST_CASES_NORMAL = [
    # Function input and result
    [ "ATGCT", "AGCT",  [1, -1, -2] ],
    [ "ATCGGAG", "ATGGCAA",  [1, -1, -1] ],
    [ "AUUGGAAUUCCCG", "UUGGUUCCG",  [1, -1, 0] ],
    [ "NNKKYYYRNYYKGAA", "NNAKYYRNYYKGA",  [2, -5, -10] ],
    [ "GCATGCU", "GATTACA", [1, -1, -1] ], 
    [ "ATCGGAG", "ATGGCAA", [1, -1, -1] ],
    [ "GAAT", "GGAT", [1, 0, 0] ],
    [ "AUUGGAAUUCCCG", "UUGGUUCCG", [1, -1, 0] ],
    [ "NNKKYYYRNYYKGAA", "NNAKYYRNYYKGA", [2, -5, -10] ],
    [ "31415", "31017", [1, 0, 0] ],
    [ "HOTDOG", "HOTCAT", [0, 0, 0] ],
    [ "31415", "31017",  [1, 0, 0] ] ,
    [ "HOTCOT", "HOTCAT", [0, 0, 0] ],
    [ "NGNYGG", "NNYGG", [1, 0, 0] ],
]

# Test cases for needleman (both versions / matrix) (Q9/Q7)
TEST_CASES_MAT = [
    [ "ABC", "ABC", [1, 2, 3, 1, 2, 3, 1, 2, 3, 0], "ABC" ],
    [ "NGNYGG", "NNYGG", [1, 2, 3, 2, 0, 3, 0, 0, 0, -2], "NYG" ],
    [ "AUUGGAAUUCCCG", "UUGGUUCCG", [5, 4, 3, 2, 2, 3, 4, 5, 9, 8, 7, 6, 6, 7, 8, 9, -10], NUCLEOTIDES ],
    [ "NNKKYYYRNYYKGAA", "NNAKYYRNYYKGA", [5, 4, 3, 2, 2, 3, 4, 5, 9, 8, 7, 6, 6, 7, 8, 9, 5, 4, 3, 2, 2, 3, 4, 5, 9, 8, 7, 6, 6, 7, 8, 9, 0, 0, 0, 0, -1], "AGKNRY" ],
    [ "31415", "31017", [5, 4, 3, 2, 2, 3, 4, 5, 9, 8, 7, 6, 6, 7, 8, 9, 4, 5, 6, 7, 7, 6, 5, 4, 0, 5, 7, 10, 20, 1, 2, 4, 2, 3, 8, 9,-1], "013457" ],
]

def test_needlman():
    for t in TEST_CASES_NORMAL:
        #----------- Our Implementation -----------
        m = needleman(t[0], t[1], t[2])
        #---------------- Bio Seq -----------------
        m2 = nw_bio(t[0], t[1], t[2])
        #------------------ Test ------------------
        assert m in m2

def test_needlman_all():
    for t in TEST_CASES_NORMAL:
        #----------- Our Implementation -----------
        m1 = needleman_all(t[0], t[1], t[2])
        #---------------- Bio Seq -----------------
        m2 = nw_bio(t[0], t[1], t[2])
        #------------------ Test ------------------
        assert sorted(m1) == sorted(m2)

def test_needlman_mat():
    for t in TEST_CASES_MAT:
        #----------- Our Implementation -----------
        m1 = needleman(t[0], t[1], cost_mat=t[2], key=t[3])
        #---------------- Bio Seq ----------------
        m2 = nw_bio_mat(t[0], t[1], cost_mat=t[2], key=t[3])
        #------------------ Test ------------------
        assert m1 in m2

def test_needlman_all_mat():
    for t in TEST_CASES_MAT:
        #----------- Our Implementation -----------
        m1 = needleman_all(t[0], t[1], cost_mat=t[2], key=t[3])
        #---------------- Bio Seq -----------------
        m2 = nw_bio_mat(t[0], t[1], cost_mat=t[2], key=t[3])
        #------------------ Test ------------------
        assert sorted(m1) == sorted(m2)

############################################################
###################  THE ULTIMATE TEST!  ###################
# We will be testing both functions with their different 
# versions (matrix or cost_table) with randomly generated 
# sequences then we will compare with BioPython
############################################################

def test_needleman_random_gen():
    for _ in range(0, EPOCHS) :
        #----------- Generating random arguments -----------
        cost_table = [ random.randint(-10, 10), random.randint(-10, 0), random.randint(-10, 0) ]
        args = arg_generator(N=NW_RUNS, stride=1, type=STRINGS, variant_arg_pos=[0, 1], static_args=[cost_table], start=1,
                    same_size=False, lower=(NW_RUNS//2)+1, upper=NW_RUNS)
        for arg in args:
            #------------------ Test ------------------
            assert needleman(*arg) in nw_bio_generic(*arg)

def test_needleman_all_random_gen():
    for _ in range(0, EPOCHS) :
        #----------- Generating random arguments -----------
        cost_table = [ random.randint(-10, 10), random.randint(-10, 0), random.randint(-10, 0) ]
        args = arg_generator(N=NW_ALL_RUNS, stride=1, type=STRINGS, variant_arg_pos=[0, 1], static_args=[cost_table], start=1,
                    same_size=False, lower=(NW_ALL_RUNS//2)+1, upper=NW_ALL_RUNS)
        for arg in args:
            #------------------ Test ------------------
            assert sorted(needleman_all(*arg)) == sorted(nw_bio_generic(*arg))

def test_needleman_mat_random_gen():
    for i in range(0, EPOCHS) :
        #----------- Generating random arguments -----------
        key = ''.join(list(set(random.choices(string.ascii_lowercase, k=i+2))))
        cost_mat = [ random.randint(-10, 10) for _ in range(len(key) ** 2 + 1) ]
        args = arg_generator(N=NW_RUNS, stride=1, type=STRINGS, samples=key, variant_arg_pos=[0, 1], static_args=[None, cost_mat, key], 
                    start=1, same_size=False, lower=(NW_RUNS//2)+1, upper=NW_RUNS)
        for arg in args:
            #------------------ Test ------------------
            assert needleman(*arg) in nw_bio_generic(*arg)

def test_needleman_mat_all_random_gen():
    for i in range(0, EPOCHS) :
        #----------- Generating random arguments -----------
        key = ''.join(list(set(random.choices(string.ascii_lowercase, k=i+2))))
        cost_mat = [ random.randint(-10, 10) for _ in range(len(key) ** 2 + 1) ]
        args = arg_generator(N=NW_ALL_RUNS, stride=1, type=STRINGS, samples=key, variant_arg_pos=[0, 1],static_args=[None, cost_mat, key], 
                    start=1, same_size=False, lower=(NW_ALL_RUNS//2)+1, upper=NW_ALL_RUNS)
        for arg in args:
            #------------------ Test ------------------
            assert sorted(needleman_all(*arg)) == sorted(nw_bio_generic(*arg))

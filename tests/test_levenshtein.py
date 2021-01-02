import pytest
from src.levenshtein import *

# used to generate bunch of random arguments for testing
from src.performance import * 

# Settings for randomly generated arguments tests
# If you want tests to run quickly then you should modify these 
# you can also set EPOCHS to 0 to completely turn them off:
# TOTAL_TESTS_PER_FUNCTION = FUNC_RUNS * EPOCHS
EPOCHS       = 20       # How many times we test iterations we should run per function
LEV_RUNS     = 10      # How many arguments we will generate per epoch for lev, lev_dp, lev_rec

TEST_CASES = [
    ["Book", "Back", 2],
    ["Levenshtein", "Levenshtein", 0],
    ["", "Levenshtein", 11],
    ["Levenshtein", "", 11],
    ["Altogether", "All together", 2],
    ["Effect", "Affect", 1],
    ["Lose", "Loose", 1],
    ["Stationary", "Stationery", 1],
    ["Specially", "Especially", 2],
    ["Principle", "Principal", 2],
    ["Allowed", "Aloud", 3],
    ["Bear", "Bare", 2],
    ["Fair", "Fare", 2],
    ["Pear", "Pair", 2],
    ["Piece", "Peace", 2],
    ["Practice", "Practise", 1],
    ["Their", "There", 2],
    ["Weather", "Whether", 2],
    ["Two", "To", 1],
    ["Two", "Too", 1],
    ["There", "Their", 2],
    ["Buy", "Bye", 2],
    ["Compliment", "Complement", 1],
    ["Brake", "Break", 2],
    ["Coarse", "Course", 1],
    ["Here", "Hear", 2],
    ["Peace", "Piece", 2],
    ["Whole", "Hole", 2],
    ["Stare", "Stair", 2],
    ["Know", "No", 3],
    ["Stare", "Stair", 2],
]

def test_rec():
    for t in TEST_CASES:
        assert lev_rec(t[0], t[1]) == t[2]

def test_dp():
    for t in TEST_CASES:
        assert lev_dp(t[0], t[1]) == t[2]

def test_dp_rec_itr():
    for t in TEST_CASES:
        assert lev(t[0], t[1]) == lev_dp(t[0], t[1]) == lev_rec(t[0], t[1]) == t[2]

def test_lev_total():
    for t in TEST_CASES:
        assert lev(t[0], t[1]) == lev_dp(t[0], t[1]) == lev_rec(t[0], t[1]) == t[2]

def test_gen_lev():
    for _ in range(0, EPOCHS) :
        #----------- Generating random arguments -----------
        args = arg_generator(N=LEV_RUNS, stride=1, type=STRINGS, variant_arg_pos=[0, 1], start=0, same_size=False, 
                    lower=LEV_RUNS/2, upper=LEV_RUNS)
        for arg in args:
            assert lev(*arg) == lev_dp(*arg) == lev_rec(*arg)
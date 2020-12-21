import pytest
from src.lev import *

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
    ["buy", "bye", 2],
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
        assert lev(t[0], t[1]) == t[2]

def test_dp():
    for t in TEST_CASES:
        assert lev_dp(t[0], t[1]) == t[2]

def test_dp_rec():
    for t in TEST_CASES:
        assert lev(t[0], t[1]) == lev_dp(t[0], t[1]) == lev_itr(t[0], t[1]) == t[2]
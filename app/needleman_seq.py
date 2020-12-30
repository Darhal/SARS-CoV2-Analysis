# Question 8 demande d'afficher opération d'alignement, faut y réfléchir.
from needleman import needleman

def print_nw_table(seq1, seq2, alg_mat):
    header = ["| "+c+" |" for c in ' -'+seq1]
    for i in range(0, len(seq2) + 1):
        for j in range(0, len(seq1) + 1):
            

def nw_verbose(seq1, seq2, cost_table = None, cost_mat = None, key = None):
    alg, alg_mat, path = needleman(seq1, seq2, cost_table=cost_table, cost_mat=cost_mat, key=key, verbose=True)
    print_nw_table(seq1, seq2, alg_mat)

nw_verbose("ATGCT", "AGCT",  [1, -1, -2])

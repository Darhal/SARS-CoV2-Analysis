# Answer to question Q8, animated execution of needleman and the construction of the alignement

import os
from time import sleep
from src.needleman import *

class COLORS:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def create_aligner_str(seq1, seq2):
    alig_str = ""
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            alig_str += "|"
        else:
            alig_str += " "
    return alig_str


def color(str, color):
    if isinstance(color, list):
        return ''.join([c for c in color]) + str + COLORS.ENDC
    return color + str + COLORS.ENDC

def spacer(nb_space, str):
    rns = (nb_space - len(str)) // 2
    rest = (nb_space - len(str)) % 2
    return (" "*(rns + rest))+str+(" "*(rns))

def print_footer(seen, alg, len_header):
    if seen[-1] != (0, 0):
        print("Seq1: "+color(alg[0][len(alg[0])-len(seen)], COLORS.BOLD)+alg[0][(len(alg[0])-len(seen) + 1):])
        print("      "+color(alg[3][len(alg[0])-len(seen)], COLORS.BOLD)+alg[3][(len(alg[3])-len(seen) + 1):])
        print("Seq2: "+color(alg[1][len(alg[0])-len(seen)], COLORS.BOLD)+alg[1][(len(alg[1])-len(seen) + 1):])
    else:
        print("Seq1: "+alg[0])
        print("      "+alg[3])
        print("Seq2: "+alg[1])

def print_nw_table(seq1, seq2, alg, alg_mat, coord = None, seen = None):
    nb_space = max([ len(str(alg_mat[i][j])) for i in range(len(seq2) + 1) for j in range(len(seq1) + 1)]) + 2
    header = ''.join(["|"+spacer(nb_space, c) for c in ' -'+seq1]) + '|'
    dummyseq = '-'+seq2
    print("-"*len(header))
    print(header)
    print("-"*len(header))

    for i in range(0, len(seq2) + 1):
        line = "|"+spacer(nb_space, dummyseq[i])
        for j in range(0, len(seq1) + 1):
            if (i, j) in seen:
                color_choice = COLORS.GREEN
                line += "|" + color(spacer(nb_space, str(alg_mat[i][j])),  color_choice)
            elif (i, j) == coord:
                line += "|" + color(spacer(nb_space, str(alg_mat[i][j])), [ COLORS.BLUE, COLORS.UNDERLINE, COLORS.BOLD ])
            else:
                line += "|" + spacer(nb_space, str(alg_mat[i][j]))
        
        line += '|'
        print(line)
    print("-"*len(header))
    if seen and len(seen) != 0:
        print_footer(seen, alg, len(header))


def nw_verbose(seq1, seq2, cost_table = None, cost_mat = None, key = None, timer = 1):
    alg, alg_mat, path = needleman(seq1, seq2, cost_table=cost_table, cost_mat=cost_mat, key=key, verbose=True)
    alg.append(create_aligner_str(alg[0], alg[1]))
    path.append((-1, -1))
    seen = []
    for coord in path:
        clear()
        print_nw_table(seq1, seq2, alg, alg_mat, coord, seen)
        seen.append(coord)
        sleep(timer)


# Some application:
nw_verbose("ATGCT", "AGCT",  [1, -1, -1])
nw_verbose("ABC", "ABC", cost_mat=[1, 2, 3, 1, 2, 3, 1, 2, 3, 0], key="ABC", timer=0.5)
nw_verbose("HOTDOG", "HOTCAT",  [1, -1, -2], timer=0.5)
nw_verbose("NGNYGG", "NNYGG", cost_mat=[1, 2, 3, 2, 0, 3, 0, 0, 0, -2], key="NYG")
nw_verbose("ABC", "ABC", cost_mat=[1, 2, 3, 1, 2, 3, 1, 2, 3, 0], key="ABC", timer=0.5)
# Answer to question Q8, animated execution of needleman and the construction of the alignement

import os
from time import sleep
from src.needleman import *

class COLORS:
    ''' Colors enum '''
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
    '''
        clears the terminal, this function is os dependant
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def create_aligner_str(seq1, seq2):
    '''
        Create a decorated sequance alignement

        Args:
            seq1: aligned sequence 1
            seq2: aligned sequence 2
        
        Returns:
            decorated aligned sequence
    '''
    alig_str = ""
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            alig_str += "|"
        else:
            alig_str += " "
    return alig_str


def color(str, color):
    ''' 
        colors a string str

        Args:
            str: the string to be colored
            color: can be single color or mutliple colors in an array
        Returns:
            colored string str that can be used in the terminal
    '''
    if isinstance(color, list):
        return ''.join([c for c in color]) + str + COLORS.ENDC
    return color + str + COLORS.ENDC


def spacer(nb_space, str):
    '''
        centers str in the middle of a number of spaces
        
        Args:
            nb_space: the number of space used to center str
            str: the string to be centered
        
        Returns:
            return the centerd string str
    '''
    rns = (nb_space - len(str)) // 2
    rest = (nb_space - len(str)) % 2
    return (" "*(rns + rest))+str+(" "*(rns))


def print_footer(seen, alg):
    '''
        prints the sequene alignment step by step

        Args:
            seen: the table of coordinates that we already visisted
            alg: a table contains the two algined sequences, the score, and the decoration

        Returns:
            None
    '''
    if seen[-1] != (0, 0):
        print("Seq1: "+color(alg[0][len(alg[0])-len(seen)], COLORS.BOLD)+alg[0][(len(alg[0])-len(seen) + 1):])
        print("      "+color(alg[3][len(alg[0])-len(seen)], COLORS.BOLD)+alg[3][(len(alg[3])-len(seen) + 1):])
        print("Seq2: "+color(alg[1][len(alg[0])-len(seen)], COLORS.BOLD)+alg[1][(len(alg[1])-len(seen) + 1):])
    else:
        print("Seq1: "+alg[0])
        print("      "+alg[3])
        print("Seq2: "+alg[1])


def print_nw_table(seq1, seq2, alg, alg_mat, coord = None, seen = None):
    '''
        prints at the alignemnt table and the coordinates taken

        Args:
            seq1: aligned sequence 1
            seq2: aligned sequence 2
            alg: a table contains the two algined sequences, the score, and the decoration
            coord: current coordinates
            seen: table of the seen coordinates
        
        Returns:
            None
    '''
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
        print_footer(seen, alg)


def nw_verbose(seq1, seq2, cost_table = None, cost_mat = None, key = None, timer = 1):
    '''
        Animated the needleman algorithm, on each iteration it clears the terminal, print the table and the path taken then wait for a specific amount 
        of time

        Args:
            seq1: the first sequence to align
            seq2: the second sequence to align
            cost_table: contains the match, mismatch and the gap cost in this order (mutual exlusive with cost_mat)
            cost_mat: contains the cost matrix and the gap at the end (mutual exlusive with cost_table and used with key)
            key: the order of the letters in the cost matrix (mutual exlusive with cost_table)
            timer: timer to sleep on each iteration
        
        Returns:
            None
    '''
    alg, alg_mat, path = needleman(seq1, seq2, cost_table=cost_table, cost_mat=cost_mat, key=key, verbose=True)
    alg.append(create_aligner_str(alg[0], alg[1]))
    path.append((-1, -1))
    seen = []
    for coord in path:
        clear()
        print_nw_table(seq1, seq2, alg, alg_mat, coord, seen)
        seen.append(coord)
        sleep(timer)


#######################################
# Some application:
#######################################
nw_verbose("ATGCT", "AGCT",  [1, -1, -1])
nw_verbose("ABC", "ABC", cost_mat=[1, 2, 3, 1, 2, 3, 1, 2, 3, 0], key="ABC", timer=0.5)
nw_verbose("HOTDOG", "HOTCAT",  [1, -1, -2], timer=0.5)
nw_verbose("NGNYGG", "NNYGG", cost_mat=[1, 2, 3, 2, 0, 3, 0, 0, 0, -2], key="NYG")
nw_verbose("ABC", "ABC", cost_mat=[1, 2, 3, 1, 2, 3, 1, 2, 3, 0], key="ABC", timer=0.5)
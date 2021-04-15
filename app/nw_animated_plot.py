import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import matplotlib

def needleman(seq1, seq2, cost_table = None, cost_mat = None, key = None, verbose = False):
    '''Function that calculates the global alignement of two sequences
    
    Args:
        seq1: first sequence
        seq2: second sequence
        cost_table: contains the match, mismatch and the gap cost in this order (mutual exlusive with cost_mat)
        cost_mat: contains the cost matrix and the gap at the end (mutual exlusive with cost_table and used with key)
        key: the order of the letters in the cost matrix (mutual exlusive with cost_table)
            E.g: [  1, 2, 3, 1, 2, 3, 1, 2, 3, 4  ] key = "ABC"
                    |  |  |  |  |  |  |  |  |  |
                    A  A  A  B  B  B  C  C  C gap
                    A  B  C  A  B  C  A  B  C  
    
    Returns:
        An array contains one possible alignements with its score 
        E.g: [seq1 alignement, seq2 alignement, score]
    '''
    # Some sanity checks:
    if cost_table and cost_mat and key:
        print("Error: cost_mat and key are mutually exlusive with cost_table, please use the one or the other")
        return
    
    if cost_table and len(cost_table) != 3:
        print("Error: cost_table must be of length 3 and contain the match, mismatch and the gap respectively ")
        return
    
    if not cost_table and ((not cost_mat and key) or (cost_mat and not key)):
        print("Error: cost_mat and key must be defined togther")
        return

    if cost_mat and key and len(cost_mat) != len(key) ** 2 + 1:
        print("Error: cost_mat must have the same length of the suqare of the length of key^2 + 1 (the last number is the gap)")
        return
    
    letter_dict = {}
    gap = 0

    if key and cost_mat:
        letter_dict = { key[i]: i for i in range(len(key)) }
        gap = cost_mat[len(key) ** 2]
    else:
        gap = cost_table[2]

    def get_cost(letter1, letter2):
        if key and cost_mat:
            return cost_mat[letter_dict[letter1] * len(key) + letter_dict[letter2]]
        else:
            if letter1 == letter2:
                return cost_table[0]
            else:
                return cost_table[1]

    len_seq1, len_seq2 = len(seq1), len(seq2)
    alignement_mat = [ [ 0 for _ in range(len_seq1 + 1) ] for _ in range(len_seq2 + 1) ]

    # Init step:
    for i in range(1, len_seq1+1):
        alignement_mat[0][i] = alignement_mat[0][i - 1] + gap
        plot_nw(seq1, seq2, alignement_mat, itr=i, coords=[(0, i)])

    for j in range(1, len_seq2+1):
        alignement_mat[j][0] = alignement_mat[j - 1][0] + gap
        plot_nw(seq1, seq2, alignement_mat, itr=len_seq1+j, coords=[(j, 0)])

    # Filling:
    for j in range(1, len_seq2+1):
        for i in range(1, len_seq1+1):
            left_val = alignement_mat[j][i - 1] + gap
            up_val = alignement_mat[j - 1][i] + gap
            diag_val = alignement_mat[j - 1][i - 1] + get_cost(seq1[i - 1], seq2[j - 1])
            alignement_mat[j][i] = max(max(left_val, up_val), diag_val)
            plot_nw(seq1, seq2, alignement_mat, itr=len_seq1+len_seq2+j*(len_seq2+1)+i, coords=[(j-1, i), (j, i-1), (j-1, i-1), (j, i)], type=0)

    # Trace back:
    coord = (len_seq2, len_seq1)
    output_seq1 = ""
    output_seq2 = ""
    coord_path = []
    coord_path.append(coord)
    dummy_itr  = 0

    while coord != (0, 0):
        cost = get_cost(seq1[coord[1] - 1], seq2[coord[0] - 1])
        if coord[0] == 0:
            coord = (coord[0], coord[1] - 1)
            output_seq1 = seq1[coord[1]] + output_seq1
            output_seq2 = '-' + output_seq2
        elif coord[1] == 0:
            coord = (coord[0] - 1, coord[1])
            output_seq1 = '-' + output_seq1
            output_seq2 = seq2[coord[0]] + output_seq2
        elif alignement_mat[coord[0] - 1][coord[1] - 1] + cost == alignement_mat[coord[0]][coord[1]]: 
            coord = (coord[0] - 1, coord[1] - 1)
            output_seq1 = seq1[coord[1]] + output_seq1
            output_seq2 = seq2[coord[0]] + output_seq2
        else:
            neighbours = [ (coord[0], coord[1] - 1), (coord[0] - 1, coord[1]) ]
            fit_neighbour = [c for c in neighbours if alignement_mat[c[0]][c[1]] + gap == alignement_mat[coord[0]][coord[1]]][0]
            
            if fit_neighbour == neighbours[0]:
                output_seq1 = seq1[fit_neighbour[1]] + output_seq1
                output_seq2 = '-' + output_seq2
            else:
                output_seq1 = '-' + output_seq1
                output_seq2 = seq2[fit_neighbour[0]] + output_seq2
            coord = fit_neighbour

        plot_nw(seq1, seq2, alignement_mat, itr=2*(len_seq1*len_seq2)+dummy_itr, coords=coord_path, type=1)
        coord_path.append(coord)
        dummy_itr+=1

    plot_nw(seq1, seq2, alignement_mat, itr=2*(len_seq1*len_seq2)+dummy_itr, coords=coord_path, type=1)
    coord_path.append((-1, -1))
    plot_nw(seq1, seq2, alignement_mat, itr=2*(len_seq1*len_seq2)+dummy_itr+1, coords=coord_path, type=1)
    if not verbose:
        return [ output_seq1, output_seq2, alignement_mat[len_seq2][len_seq1] ]
    else:
        return [ output_seq1, output_seq2, alignement_mat[len_seq2][len_seq1] ], alignement_mat, coord_path

def plot_nw(seq1, seq2, alg, coords=None, save=True, itr=0, type=-1):
    seq1 = "-"+seq1
    seq2 = "-"+seq2
    seq1_chars = list(seq1)
    seq2_chars = list(seq2)

    TYPES = [-6, -4, -2]

    color_map = [ [ 7 for _ in range(len(seq1_chars)) ] for _ in range(len(seq2_chars)) ]

    if coords:
        for coord in coords:
            if type == -1: # Init
                color_map[coord[0]][coord[1]] = -7
            elif type == 0: # Filling
                color_map[coord[0]][coord[1]] = 6
            elif type == 1: # Traceback
                color_map[coord[0]][coord[1]] = -6
        
        if type == 0 and coords[-1] != (-1, -1): # filling
            color_map[coords[-1][0]][coords[-1][1]] = -7
        elif type == 1 and coords[-1] != (-1, -1):
            color_map[coords[-1][0]][coords[-1][1]] = 5

    fig, ax = plt.subplots()
    im = ax.imshow(color_map, cmap="Spectral", vmin=-8, vmax=8)
    ax.set_xticks(range(len(seq1_chars)))
    ax.set_yticks(range(len(seq2_chars)))
    ax.set_xticklabels(seq1_chars)
    ax.set_yticklabels(seq2_chars)
    ax.tick_params(axis='both', which='major', labelbottom = False, bottom=False, top = False, labeltop=True)

    for i in range(len(seq2_chars)):
        for j in range(len(seq1_chars)):
            text = ax.text(j, i, alg[i][j], ha="center", va="center", color="w")
    
    # Turn spines off and create white grid.
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    ax.set_xticks(np.arange(len(seq1_chars)+1)-.5, minor=True)
    ax.set_yticks(np.arange(len(seq2_chars)+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=2)
    ax.tick_params(which="minor", bottom=False, left=False)
    fig.tight_layout()
    ax.set_title("Algorithme de Needleman-Wunsch")
    if not save:
        plt.show()
    else:
        plt.savefig(f"NW_{itr}.png", bbox_inches='tight', dpi=200)
    plt.close()
    


print(needleman("TAPS", "TOP", [1, -1, -2]))
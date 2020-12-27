def is_positive(x, y, minx = 0, miny = 0):
    return x >= minx  and y >= miny

def needleman(seq1, seq2, cost_table = None, cost_mat = None, key = None):
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
        print("Error: cost_mat must have the same length of the suqare of the length of key + 1 (the last number is the gap)")
        return
    
    letter_dict = {}
    gap = 0

    if key and cost_mat:
        letter_dict = { key[i]: i for i in range(len(key)) }
        gap = cost_mat[len(key)]
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

    for j in range(1, len_seq2+1):
        alignement_mat[j][0] = alignement_mat[j - 1][0] + gap

    # Filling:
    for j in range(1, len_seq2+1):
        for i in range(1, len_seq1+1):
            left_val = alignement_mat[j][i - 1] + gap
            up_val = alignement_mat[j - 1][i] + gap
            diag_val = alignement_mat[j - 1][i - 1] + get_cost(seq1[i - 1], seq2[j - 1])
            alignement_mat[j][i] = max(max(left_val, up_val), diag_val)

    # Trace back:
    coord = (len_seq2, len_seq1)
    output_seq1 = ""
    output_seq2 = ""
    while coord != (0, 0):
        if coord[0] == 0:
            coord = (coord[0], coord[1] - 1)
            output_seq1 = seq1[coord[1]] + output_seq1
            output_seq2 = '-' + output_seq2
        elif coord[1] == 0:
            coord = (coord[0] - 1, coord[1])
            output_seq1 = '-' + output_seq1
            output_seq2 = seq2[coord[0]] + output_seq2
        elif seq2[coord[0] - 1] == seq1[coord[1] - 1]:
            coord = (coord[0] - 1, coord[1] - 1)
            output_seq1 = seq1[coord[1]] + output_seq1
            output_seq2 = seq2[coord[0]] + output_seq2
        else:
            neighbours = [ (coord[0], coord[1] - 1), (coord[0] - 1, coord[1] - 1), (coord[0] - 1, coord[1]) ]
            highest_neighbour = [c for c in neighbours if alignement_mat[c[0]][c[1]] == max(alignement_mat[c1[0]][c1[1]] for c1 in neighbours)][0]
            
            if highest_neighbour == neighbours[1]:
                output_seq1 = seq1[highest_neighbour[1]] + output_seq1
                output_seq2 = seq2[highest_neighbour[0]] + output_seq2
            elif highest_neighbour == neighbours[0]:
                output_seq1 = seq1[highest_neighbour[1]] + output_seq1
                output_seq2 = '-' + output_seq2
            else:
                output_seq1 = '-' + output_seq1
                output_seq2 = seq2[highest_neighbour[0]] + output_seq2
            coord = highest_neighbour
    return [ output_seq1, output_seq2, alignement_mat[len_seq2][len_seq1] ]



def needleman_all(seq1, seq2, cost_table = None, cost_mat = None, key = None):
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
        An array contains all possible alignements with their respective scores
        E.g: [ [seq1 alignement 1, seq2 alignement 1, score 1], [seq1 alignement 2, seq2 alignement 2, score 2] ]
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
        print("Error: cost_mat must have the same length of the suqare of the length of key + 1 (the last number is the gap)")
        return

    letter_dict = {}
    gap = 0

    if key and cost_mat:
        letter_dict = { key[i]: i for i in range(len(key)) }
        gap = cost_mat[len(key)]
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
    # Matrix that contain directions coded with 3 binary digits for all the possibles combinations of diections
    # xyz: z is the digonal bit, y is the left bit, x is the upward bit
    # x y z
    # | | |
    # U L D (U:Up / L: Left / D:Diag )
    mat_dir = [ [0 for _ in range(len_seq1 + 1) ] for _ in range(len_seq2 + 1) ]

    # Init step:
    for i in range(1, len_seq1+1):
        alignement_mat[0][i] = alignement_mat[0][i - 1] + gap
        mat_dir[0][i] = 1 << 1 # we go left all the way left!

    for j in range(1, len_seq2+1):
        alignement_mat[j][0] = alignement_mat[j - 1][0] + gap
        mat_dir[j][0] = 1 << 2 # we go up all the way up!

    # Filling:
    for j in range(1, len_seq2+1):
        for i in range(1, len_seq1+1):
            left_val = alignement_mat[j][i - 1] + gap
            up_val = alignement_mat[j - 1][i] + gap
            diag_val = alignement_mat[j - 1][i - 1] + get_cost(seq1[i - 1], seq2[j - 1])
            alignement_mat[j][i] = max(max(left_val, up_val), diag_val)
            if diag_val == alignement_mat[j][i]:
                mat_dir[j][i] |= 1
            if left_val == alignement_mat[j][i]:
                mat_dir[j][i] |= (1 << 1)
            if up_val == alignement_mat[j][i]:
                mat_dir[j][i] |= (1 << 2)

    # Trace back:
    coord = (len_seq2, len_seq1)
    output = []
    coord_fifo = [ (len_seq2, len_seq1) ]
    path_fifo = [ [ "", "", alignement_mat[len_seq2][len_seq1] ] ]
    seq1 = "-"+seq1
    seq2 = "-"+seq2

    while len(coord_fifo):
        coord = coord_fifo[0]
        path = path_fifo[0]

        while (1):
            if coord == (0, 0):
                output.append(path)
                path_fifo.pop(0)
                coord_fifo.pop(0)
                break

            taken = False
            coord_tmp = coord
            nc = coord # new coord that will be our path in this loop
            org_path = path[:]

            if mat_dir[coord[0]][coord[1]] & 1: # Diag
                coord_tmp = (coord[0] - 1, coord[1] - 1)
                nc = coord_tmp
                path[0] = seq1[coord[1]] + path[0]
                path[1] = seq2[coord[0]] + path[1]
                taken = True
            if mat_dir[coord[0]][coord[1]] & (1 << 1):  # Left
                coord_tmp = (coord[0], coord[1] - 1)
                if not taken:
                    nc = coord_tmp
                    taken = True
                    path[0] = seq1[coord[1]] + path[0]
                    path[1] = '-' + path[1]
                else:
                    path_fifo.append(org_path[:])
                    coord_fifo.append(coord_tmp)
                    path_fifo[-1][0] = seq1[coord[1]] + path_fifo[-1][0]
                    path_fifo[-1][1] = '-' + path_fifo[-1][1]
            if mat_dir[coord[0]][coord[1]] & (1 << 2):  # Up
                coord_tmp = (coord[0] - 1, coord[1])
                if not taken:
                    nc = coord_tmp
                    taken = True
                    path[0] = '-' + path[0]
                    path[1] = seq2[coord[0]] + path[1]
                else:
                    path_fifo.append(org_path[:])
                    coord_fifo.append(coord_tmp)
                    path_fifo[-1][0] = '-' + path_fifo[-1][0]
                    path_fifo[-1][1] = seq2[coord[0]] + path_fifo[-1][1]
            coord = nc
    
    return output

# m = needleman_all("GAAT", "GGAT", [1, 0, 0])
# for l in m:
#     print(l)
# print("--------------")

# # https://biopython.org/docs/1.75/api/Bio.pairwise2.html
# from Bio import pairwise2
# alignments = pairwise2.align.globalms("GAAT", "GGAT", 1, 0, 0, 0)
# formated_alignments = [ [ a[0], a[1], int(a[2]) ] for a in alignments ]
# for l in formated_alignments:
#     print(l)

# print(sorted(m) == sorted(formated_alignments))
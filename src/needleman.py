
def needleman(seq1, seq2, mat):
    '''

    '''
    len_seq1, len_seq2 = len(seq1), len(seq2)
    match, mismatch, gap = mat[0], mat[1], mat[2]
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
            diag_val = alignement_mat[j - 1][i - 1]
            if seq1[i - 1] == seq2[j - 1]:
                diag_val += match
            else:
                diag_val +=  mismatch
            alignement_mat[j][i] = max(max(left_val, up_val), diag_val)

    # Trace back:
    coord = (len_seq2, len_seq1)
    output_seq1 = ""
    output_seq2 = ""
    while (coord != (0, 0)):
        if seq2[coord[0] - 1] == seq1[coord[1] - 1]:
            coord = (coord[0] - 1, coord[1] - 1)
            if alignement_mat[coord[0] + 1][coord[1] + 1] > alignement_mat[coord[0]][coord[1]]:
                output_seq1 = seq1[coord[1]] + output_seq1
                output_seq2 = seq2[coord[0]] + output_seq2
            else:
                output_seq1 = seq1[coord[1]] + output_seq1
                output_seq2 = seq2[coord[0]] + output_seq2
        else:
            neighbours = [ (coord[0], coord[1] - 1), (coord[0] - 1, coord[1] - 1), (coord[0] - 1, coord[1]) ]
            highest_neighbour = [c for c in neighbours if alignement_mat[c[0]][c[1]] == max(alignement_mat[c1[0]][c1[1]] for c1 in neighbours)][0]
            
            if highest_neighbour == neighbours[1]:
                if alignement_mat[coord[0]][coord[1]] > alignement_mat[highest_neighbour[0]][highest_neighbour[1]]:
                    pass
                else:
                    pass
                output_seq1 = seq1[highest_neighbour[1]] + output_seq1
                output_seq2 = seq2[highest_neighbour[0]] + output_seq2
            elif highest_neighbour == neighbours[0]:
                output_seq1 = seq1[highest_neighbour[1]] + output_seq1
                output_seq2 = '-' + output_seq2
            else:
                output_seq1 = '-' + output_seq1
                output_seq2 = seq2[highest_neighbour[0]] + output_seq2
            coord = highest_neighbour
    return [ output_seq1, output_seq2 ]


def needleman_exprimental(seq1, seq2, mat):
    '''

    '''
    len_seq1, len_seq2 = len(seq1), len(seq2)
    match, mismatch, gap = mat[0], mat[1], mat[2]
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
            diag_val = alignement_mat[j - 1][i - 1]
            if seq1[i - 1] == seq2[j - 1]:
                diag_val += match
            else:
                diag_val +=  mismatch
            alignement_mat[j][i] = max(max(left_val, up_val), diag_val)

    for l in alignement_mat:
        print(l) 

    # Trace back:
    coord_stack = [ (len_seq2, len_seq1) ]
    path_stack = [ ["", "", 0] ]
    output_pool = [  ]

    while len(coord_stack):
        coord = coord_stack[0]
        path = path_stack[0]
        print("-- START OF PATH --")

        while (1):
            print(f"Coord: {coord} - Path: {path}")
            if coord == (0, 0):
                output_pool.append(path)
                path_stack.pop(0)
                coord_stack.pop(0)
                print("-- END OF PATH --")
                break

            highest_neighbour = (-1, -1)
            neighbours = [ (coord[0] - 1, coord[1] - 1), (coord[0], coord[1] - 1), (coord[0] - 1, coord[1]) ]
            old_path = path[:]

            if seq2[coord[0] - 1] == seq1[coord[1] - 1]:
                highest_neighbour = (coord[0] - 1, coord[1] - 1)
                if alignement_mat[highest_neighbour[0] + 1][highest_neighbour[1] + 1] > alignement_mat[highest_neighbour[0]][highest_neighbour[1]]:
                    path[2] += match
                else:
                    path[2] += mismatch
                path[0] = seq1[highest_neighbour[1]] + path[0]
                path[1] = seq2[highest_neighbour[0]] + path[1]
            else:
                highest_neighbours = [c for c in neighbours if alignement_mat[c[0]][c[1]] == max(alignement_mat[c1[0]][c1[1]] for c1 in neighbours)]
                
                for hn in highest_neighbours:
                    if highest_neighbour == hn: # remove this elemnt its already taken into account
                        continue
                    if highest_neighbour != (-1, -1):
                        # Copy the last seen path and coordinates to stack for further processing later
                        path_stack.append(old_path)
                        coord_stack.append(hn)
                        print(f"\tAnother possible solution is found {hn} {path_stack[-1]}")
                        continue
                    if hn == neighbours[0]: # Either a match or mismatch
                        if alignement_mat[coord[0]][coord[1]] > alignement_mat[hn[0]][hn[1]]:
                            path[2] += match
                        else:
                            path[2] += mismatch
                        path[0] = seq1[hn[1]] + path[0]
                        path[1] = seq2[hn[0]] + path[1]
                        highest_neighbour= hn
                    elif hn == neighbours[1]: # Its a gap
                        path[0] = seq1[hn[1]] + path[0]
                        path[1] = '-' + path[1]
                        path[2] += gap
                        highest_neighbour= hn
                    else:
                        path[0] = '-' + path[0]
                        path[1] = seq2[hn[0]] + path[1]
                        path[2] += gap
                        highest_neighbour= hn
            
            coord = highest_neighbour

    return output_pool

# m = needleman("ATGCT", "AGCT",  [1, -1, -2])
# for l in m:
#     print(l) 

# m = needleman_exprimental("ATGCT", "AGCT",  [1, -1, -1])
# for l in m:
#     print(l) 

m = needleman_exprimental("GCATGCU", "GATTACA",  [1, -1, -1])
for l in m:
    print(l) 
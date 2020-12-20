
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

    # return alignement_mat

    # Trace back:
    coord = (len_seq2, len_seq1)
    # TODO: Continue with trace back

m = needleman("GAATTCAGTTA", "GGATCGA",  [1, 0, 0])
for l in m:
    print(l) 


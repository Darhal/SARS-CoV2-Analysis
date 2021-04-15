
def lev_rec(seq1, seq2):
    '''Function that return the Levenshtein distance between two given strings seq1 and seq2
    
    Args:
        seq1: first string also known as source string
        seq2: second string also known as target string
    
    Returns:
        Levenshtein distance
    '''
    len_seq1, len_seq2 = len(seq1), len(seq2)
    if len_seq1 == 0:
        return len_seq2

    if len_seq2 == 0:
        return len_seq1

    if seq1[0] == seq2[0]:
        return lev_rec(seq1[1:], seq2[1:])
    
    return 1 + min(
        min(
            lev_rec(seq1[1:], seq2), 
            lev_rec(seq1, seq2[1:])
        ),
        lev_rec(seq1[1:], seq2[1:])
    )


def lev_dp(seq1, seq2):
    '''Function that return the Levenshtein distance between two given strings seq1 and seq2, but uses Dynamic Programming
        
        Args:
            seq1: first string also known as source string
            seq2: second string also known as target string

        Returns:
            Levenshtein distance
    '''
    dp = [[ -1 for _ in range(len(seq2) + 1) ] for _ in range(len(seq1) + 1)]

    def lambda_lev_dp(seq1, seq2, dp):
        '''Function that return the Levenshtein distance between two given strings seq1 and seq2, but uses Dynamic Programming
        
        Args:
            seq1: first string also known as source string
            seq2: second string also known as target string
            dp: two dimensional array of length m by m (where m is the max length)
        
        Returns:
            Levenshtein distance
        '''
        len_seq1, len_seq2 = len(seq1), len(seq2)
        
        if dp[len_seq1][len_seq2] != -1:
            return dp[len_seq1][len_seq2]

        if len_seq1 == 0:
            dp[len_seq1][len_seq2] = len_seq2
            return dp[len_seq1][len_seq2]
        
        if len_seq2 == 0:
            dp[len_seq1][len_seq2] = len_seq1
            return dp[len_seq1][len_seq2]
        
        if seq1[0] == seq2[0]:
            dp[len_seq1][len_seq2] = lambda_lev_dp(seq1[1:], seq2[1:], dp)
            return dp[len_seq1][len_seq2]
                
        dp[len_seq1][len_seq2] = 1 + min(
                min(lambda_lev_dp(seq1[1:], seq2, dp), lambda_lev_dp(seq1, seq2[1:], dp)),
                lambda_lev_dp(seq1[1:], seq2[1:], dp)
            )
        return dp[len_seq1][len_seq2]

    return lambda_lev_dp(seq1, seq2, dp)

def lev(seq1, seq2):
    '''Function that return the Levenshtein distance between two given strings seq1 and seq2, uses DP

        Args:
            seq1: first string also known as source string
            seq2: second string also known as target string

        Returns:
            Levenshtein distance
    '''
    dp = [[-1 for _ in range(len(seq2) + 1) ] for _ in range(len(seq1) + 1)]
    len_seq1, len_seq2 = len(seq1), len(seq2)

    for i in range(len_seq1 + 1):
        for j in range(len_seq2 + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1])
    
    return dp[len_seq1][len_seq2]
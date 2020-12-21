
def lev(str1, str2):
    '''Function that return the Levenshtein distance between two given strings str1 and str2
    
    Args:
        str1: first string also known as source string
        str2: second string also known as target string
    
    Returns:
        Levenshtein distance
    '''
    len_str1, len_str2 = len(str1), len(str2)
    if len_str1 == 0:
        return len_str2

    if len_str2 == 0:
        return len_str1

    if str1[0] == str2[0]:
        return lev(str1[1:], str2[1:])
    
    return 1 + min(
        min(
            lev(str1[1:], str2), 
            lev(str1, str2[1:])
        ),
        lev(str1[1:], str2[1:])
    )


def lev_dp(str1, str2):
    '''Function that return the Levenshtein distance between two given strings str1 and str2, but uses Dynamic Programming

        Args:
            str1: first string also known as source string
            str2: second string also known as target string

        Returns:
            Levenshtein distance
    '''
    dp = [[ -1 for _ in range(len(str2) + 1) ] for _ in range(len(str1) + 1)]

    def lambda_lev_dp(str1, str2, dp):
        '''Function that return the Levenshtein distance between two given strings str1 and str2, but uses Dynamic Programming
        
        Args:
            str1: first string also known as source string
            str2: second string also known as target string
            dp: two dimensional array of length m by m (where m is the max length)
        
        Returns:
            Levenshtein distance
        '''
        len_str1, len_str2 = len(str1), len(str2)
        
        if dp[len_str1][len_str2] != -1:
            return dp[len_str1][len_str2]

        if len_str1 == 0:
            dp[len_str1][len_str2] = len_str2
            return dp[len_str1][len_str2]
        
        if len_str2 == 0:
            dp[len_str1][len_str2] = len_str1
            return dp[len_str1][len_str2]
        
        if str1[0] == str2[0]:
            dp[len_str1][len_str2] = lambda_lev_dp(str1[1:], str2[1:], dp)
            return dp[len_str1][len_str2]
                
        dp[len_str1][len_str2] = 1 + min(
                min(lambda_lev_dp(str1[1:], str2, dp), lambda_lev_dp(str1, str2[1:], dp)),
                lambda_lev_dp(str1[1:], str2[1:], dp)
            )
        return dp[len_str1][len_str2]

    return lambda_lev_dp(str1, str2, dp)

def lev_itr(str1, str2):
    dp = [[ -1 for _ in range(len(str2) + 1) ] for _ in range(len(str1) + 1)]
    len_str1, len_str2 = len(str1), len(str2)

    for i in range(len_str1 + 1):
        for j in range(len_str2 + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1])
    
    return dp[len_str1][len_str2]
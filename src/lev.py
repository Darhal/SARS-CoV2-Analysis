
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
    m = max(len(str1), len(str2)) + 1
    dp = [[ -1 for _ in range(m) ] for _ in range(m)]

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
            dp[len_str1 - 1][len_str2 - 1] = lev(str1[1:], str2[1:])
            return dp[len_str1 - 1][len_str2 - 1]
        
        dp[len_str1 - 1][len_str2] = lev(str1[1:], str2)
        dp[len_str1][len_str2 - 1] = lev(str1, str2[1:])
        dp[len_str1 - 1][len_str2 - 1] = lev(str1[1:], str2[1:])

        minlev = -1
        coord = (0, 0)
        if dp[len_str1 - 1][len_str2] < dp[len_str1][len_str2 - 1]:
            minlev = dp[len_str1 - 1][len_str2]
            coord = (len_str1 - 1, len_str2)
        else:
            minlev = dp[len_str1][len_str2 - 1]
            coord = (len_str1, len_str2 - 1)

        if minlev > dp[len_str1 - 1][len_str2 - 1]:
            minlev = dp[len_str1 - 1][len_str2 - 1]
            coord = (len_str1 - 1, len_str2 - 1)

        dp[coord[0]][coord[1]] = 1 + minlev
        return dp[coord[0]][coord[1]]

    return lambda_lev_dp(str1, str2, dp)
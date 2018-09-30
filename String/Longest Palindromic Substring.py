# import numpy as np
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        #dynamic programming - Overtime 
        left, right, lgth = 0,0,0
        size = len(s)
        # dp[i][j] indicates s[i:j] is palidrome
        dp = np.array( [[ False ] * size] * size )
        for i in range(size):
            for j in range(i):
                dp[j][i] = (s[i] == s[j] and (dp[j+1][i-1] or i - j < 2))
                if(dp[j][i] and lgth < i - j + 1):
                    left = j
                    right = i
                    lgth = i - j + 1
            dp[i][i] = True
        return(s[left:right+1])
        """
        """ Manacher's Algo"""
        ### pre-processing
        ### list is iterable
        def preProcess(s):
            if not s:
                return ['^', '$']
            T = ['^']
            for c in s:
                T +=  ['#', c]
            T += ['#', '$']
            return T
     
        T = preProcess(s)
        P = [0] * len(T)
        center, right = 0, 0
        for i in range(1, len(T) - 1):
            i_mirror = 2 * center - i
            if right > i:
                P[i] = min(right - i, P[i_mirror])
            else:
                P[i] = 0

            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > right:
                center, right = i, i + P[i]

        max_i = 0
        for i in range(1, len(T) - 1):
            if P[i] > P[max_i]:
                max_i = i
        start = (max_i - 1 - P[max_i]) / 2
        return s[start : start + P[max_i]]
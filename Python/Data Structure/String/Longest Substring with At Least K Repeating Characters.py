class Solution:

	class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # use set
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
        
    '''
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # use bit mask - time excceed
        res, left = 0, 0 
        while left + k <= len(s):
            mask, max_ind, map = 0, left,[0] * 26
            for j in range(left,len(s)):
                t =  ord(s[j]) - ord('a')
                map[t] += 1
                if map[t] < k:
                    mask |= (1 << t)
                else:
                    mask &= (~(1 << t))
                if mask == 0:
                    res = max(res,j - left + 1)
                    max_ind = j
                    print(max_ind)
            left += max_ind + 1
        return res
    '''
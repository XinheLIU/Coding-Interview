class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = [-1] * 256
        res, left = 0, -1 # begin of the string
        for i in range(len(s)):
            left = max(map[ord(s[i])], left)
            map[ord(s[i])] = i
            res = max(i-left,res)
        return res
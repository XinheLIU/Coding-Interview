class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_list = [-1]*256
        res, left = 0,0
        for i in range(len(s)):
            if hash_list[ord(s[i])] == -1 or hash_list[ord(s[i])] < left:
                res = max(res, i - left + 1)
            else:
                left = hash_list[ord(s[i])] + 1 # one after last appearance 
            hash_list[ord(s[i])] = i
        return(res)
            
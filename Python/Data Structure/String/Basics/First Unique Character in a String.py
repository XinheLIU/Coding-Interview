class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = [0] * 256
        for c in s:
            map[ord(c)] += 1
        for i,c in enumerate(s):
            if map[ord(c)] == 1:
                return i
        return -1
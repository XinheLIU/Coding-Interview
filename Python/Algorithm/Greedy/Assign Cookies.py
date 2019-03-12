class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # two pointers and greedy
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                # one more cookie
                j += 1
            i += 1
        return j
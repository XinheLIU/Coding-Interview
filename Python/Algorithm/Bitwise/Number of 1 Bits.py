class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # x % 2, x >> 1 so slow
        cnt = 0
        while n:
            n &= (n-1)
            cnt += 1
        return cnt
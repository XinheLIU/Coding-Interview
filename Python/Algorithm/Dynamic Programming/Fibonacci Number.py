class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return 0 if not N else 1
        else:
            x, y = 0, 1 #f0, f1
            for _ in range(N-1): #starts from f2
                x, y = y, x + y
            return y
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        else:
            return self.myPow(x * x, n // 2)
'''
    # iterative
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n *= -1
        ret = 1
        while n:
            if n & 1:
                ret *= x
            x *= x
            n >>= 1
        return ret
'''
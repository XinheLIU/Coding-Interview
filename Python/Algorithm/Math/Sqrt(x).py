class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # bisection or Newton's method
        # f(r) = r ^ 2 - x = 0, r_n+1 = r_n - f(r)/f`(r) = r_n - (r_n^2-x)/2r = r_n/2 + x/2_rn
        r = x
        while r * r > x:
            r = (r + x/r) / 2
        return r
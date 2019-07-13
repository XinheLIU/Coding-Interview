class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Newton's method
        # f(r) = r ^ 2 - x = 0, r_n+1 = r_n - f(r)/f`(r) = r_n - (r_n^2-x)/2r_n = r_n/2 + x/2_rn
        r = x
        while r * r > x:
            r = (r + x/r) / 2
        return r

'''
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l + 1 < r:
            mid = l + (r-l) // 2
            if mid * mid < x:
                l = mid
            else:
                r = mid
        if r * r <= x:
            return int(r)
        return int(l)

class Solution:
	def mySqrt(self, x):
    """
    @param x: An integer
    @return: The sqrt of x
    """
	i, j = 0, x / 2 + 1
    while i <= j:
      mid = (i + j) / 2
      cur = mid ** 2
      if cur == x:
        return mid
      elif cur < x:
        i = mid + 1
      else:
        j = mid - 1
    return (i + j) / 2
'''
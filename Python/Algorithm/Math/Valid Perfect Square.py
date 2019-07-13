class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 1, num // 2 + 1
        while l + 1 < r:
            mid = l + (r-l) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                r = mid
            else:
                l = mid
        return True if r * r == num or l * l == num else False
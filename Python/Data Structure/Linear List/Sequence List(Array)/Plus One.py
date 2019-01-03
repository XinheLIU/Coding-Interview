class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ret = [0] * len(digits)
        one = 1
        for i in range(len(digits) - 1, -1, -1):
            x = digits[i] + one
            one = x / 10
            ret[i] = x % 10
        if one > 0:
            ret = [1] + ret
        eturn ret
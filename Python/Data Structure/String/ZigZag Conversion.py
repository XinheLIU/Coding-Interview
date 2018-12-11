class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        res = ""
        step = 2 * numRows - 2
        for i in range(numRows):
            j = i
            while j < len(s):
                res += s[j]
                temp = j + step - 2 * i
                if i != 0 and i != numRows - 1 and temp < len(s):
                    res += s[temp]
                j += step
        return res

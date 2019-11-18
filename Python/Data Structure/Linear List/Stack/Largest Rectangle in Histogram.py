class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack, res = [-1], 0
        for i in range(len(heights)):
            # an increasing stack
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res

"""
# TLE Brute Force
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ret = 0
        for i in range(len(heights)):
            min_h = float('inf')
            for j in range(i, len(heights)):
                min_h = min(min_h, heights[j])
                ret = max(ret, (j-i+1)*min_h)
        return ret
"""
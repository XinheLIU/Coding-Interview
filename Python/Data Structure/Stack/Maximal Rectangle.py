class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0)
        stack, res = [-1], 0
        for i in range(len(heights)):
            # an increasing stack
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        heights.pop()
        return res
    
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        # look at rectangles rowwise
        heights, res = [0] * n , 0
        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            res = max(res, self.largestRectangleArea(heights))
        return res
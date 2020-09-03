#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]: return
        dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                dp[r+1][c+1] = dp[r+1][c] + dp[r][c+1] + matrix[r][c] - dp[r][c]
        self.dp = dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        dp = self.dp
        return dp[row2 + 1][col2 + 1] - dp[row1][col2 + 1] - dp[row2 + 1][col1] + dp[row1][col1]
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end


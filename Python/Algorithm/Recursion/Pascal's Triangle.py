class Solution:
    def generate(self, numRows: 'int') -> 'List[List[int]]':
        dp = []
        for i in range(numRows):
            dp.append([1] * (i + 1))
            for j in range(1,i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp
        
'''
    def generate(self, numRows: 'int') -> 'List[List[int]]':
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        # recursive
        upper = self.generate(numRows - 1)
        preRow = upper[-1]
        row = [1]
        for i in range(len(preRow) - 1):
            row.append(preRow[i] + preRow[i + 1])
        row.append(1)
        upper.append(row)
        return upper
'''
        
        
        
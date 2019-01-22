class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        # could also use set for diff and sum
        self.DFS(n, [], [], [])
        return self.res
        
    def DFS(self, n, queens, xy_diff, xy_sum):
        p = len(queens) # col pos in every row
        if p == n:
            self.res += 1
            return
        for q in range(n):
            if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                self.DFS(n, queens + [q], xy_diff + [p-q], xy_sum + [p+q])
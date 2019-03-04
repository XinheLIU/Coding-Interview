class Solution:
    def DFS(self, n, queens, xy_diff, xy_sum):
        p = len(queens) # col pos in every row
        if p == n:
            self.res.append(queens)
            return
        for q in range(n):
            if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                self.DFS(n, queens + [q], xy_diff + [p-q], xy_sum + [p+q])
                
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        # could also use set for diff and sum
        self.DFS(n, [], [], [])
        return [["." * i + "Q" + "." *(n-i-1) for i in sol] for sol in self.res ]
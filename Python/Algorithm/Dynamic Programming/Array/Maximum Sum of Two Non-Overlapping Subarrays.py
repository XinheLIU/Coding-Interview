class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n, ret = len(A), 0
        dp0, dp1 = [0 for _ in range(n)], [0 for _ in range(n)]
        for i in range(n):
            dp0[i] = sum(A[i:min(i + L, n)])
            dp1[i] = sum(A[i:min(i + M, n)])
        for i in range(n):
            for j in range(n):
                if (i < j and i + L <= j) or (i > j and j + M <= i):
                    ret = max(dp0[i] + dp1[j], ret)
        return ret
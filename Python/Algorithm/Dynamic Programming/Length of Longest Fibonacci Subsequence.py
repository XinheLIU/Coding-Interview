class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        # Dp[i,j] is the longest FibSubSeq ending with i, j
        index = {v: k for k, v in enumerate(A)}
        dp = collections.defaultdict(lambda: 2)
        ret = 0
        for k, v in enumerate(A):
            for j in range(k):
                i = index.get(v - A[j], None)
                if i is not None and i < j:
                    x = dp[j, k] = dp[i,j] + 1
                    ret = max(x, ret)
        return ret if ret >= 3 else 0
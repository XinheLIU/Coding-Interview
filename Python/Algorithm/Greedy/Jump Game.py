class Solution:
	# greedy
    def canJump(self, nums: List[int]) -> bool:
        # reach is the maximum reachable length
        n, reach = len(nums), 0
        for i in range(n):
            if reach >= n - 1:
                return True
            elif i > reach:
                return False
            reach = max(i + nums[i], reach)

"""
# dynamic programming

    def canJump(self, nums: List[int]) -> bool:
        # dp[ i ] is the step left to be used when arrive in pos i
        n = len(nums)
        dp = [0] * n
        for i in range(1, n):
            dp[i] = max(dp[i-1], nums[i-1]) - 1
            if dp[i] < 0:
                return False
        return True
"""
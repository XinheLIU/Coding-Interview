class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # Fabonacci
        dp = [0] * (len(cost) + 1) # cost -1, 0, ...N
        for i in range(2,len(cost) + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[-1]
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i] should be the max(pos max, neg min) with i selected, add one more dimension for pos and neg change
        if not nums: return 0
        dp = [[0] * 2 for _ in range(2)] # 0 is pos, 1 is neg
        dp[0][0], dp[0][1], res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            x, y = i % 2, (i-1) % 2
            dp[x][0] = max(nums[i], dp[y][0] * nums[i], dp[y][1] * nums[i])
            dp[x][1] = min(nums[i], dp[y][0] * nums[i], dp[y][1] * nums[i])
            res = max(res, dp[x][0])
        return res
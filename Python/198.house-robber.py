#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp1, dp2 = nums[:], nums[:]
        dp1[0] = 0
        # two state
        for i in range(1, len(nums)):
            dp1[i] = max(dp1[i-1], dp2[i-1])
            dp2[i] = dp1[i-1] + nums[i]
        return(max(dp1[-1], dp2[-1]))
# @lc code=end


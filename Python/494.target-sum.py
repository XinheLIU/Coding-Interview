#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution(object):
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
        return dic.get(S, 0)  
# @lc code=end
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = [{} for _ in range(len(nums))]
        def dfs(sum, nums, S, i):
            if i == len(nums):
                if sum == S:
                    return 1
                else:
                    return 0
            else:
                if sum in memo[i]:
                    return memo[i][sum]
                add = dfs(sum + nums[i], nums, S, i + 1)
                substract = dfs(sum - nums[i], nums, S, i + 1)
                memo[i][sum] = add + substract
                return memo[i][sum]
        return dfs(0, nums, S, 0)
'''


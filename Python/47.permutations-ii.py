#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(ret, out, nums):
            if not nums:
                ret.append(out)
                return
            for i in range(len(nums)):
                if i and nums[i] == nums[i-1]: continue
                dfs(ret, out + [nums[i]], nums[:i] + nums[i+1:])
        ret = []
        dfs(ret, [], sorted(nums))
        return ret
# @lc code=end


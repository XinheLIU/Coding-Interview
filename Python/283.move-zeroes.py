#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i, v in enumerate(nums):
            if v != 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
# @lc code=end


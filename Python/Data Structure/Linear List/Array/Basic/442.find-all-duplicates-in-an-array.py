#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
       ret = []
       for num in nums:
           if nums[abs(num) - 1] > 0:
               nums[abs(num) - 1] *= -1
           else:
                ret.append(abs(num))
       return ret
# @lc code=end

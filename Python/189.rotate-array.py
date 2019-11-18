#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n, start = len(nums), 0
        while n and k % n:
            k %= n
            for i in range(k):
                nums[i + start], nums[n - k + i + start] = nums[n- k + i + start], nums[i + start]
            n -= k
            start += k

'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ret = [0] * n
        for i, v in enumerate(nums):
            ret[(i+k) % n] = v
        for i in range(n):
            nums[i] = ret[i]
'''
        
# @lc code=end


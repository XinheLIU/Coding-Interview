class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j, v in enumerate(nums):
            if v != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
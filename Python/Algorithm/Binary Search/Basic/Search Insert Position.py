class Solution(object):
    def searchInsert(self, nums, target):
        """
        input: int[] input, int target
        return: int
        """
        if not len(nums):
            return 0
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid            
        if target <= nums[l]:
            return l
        if target <= nums[r]:
            return r
        return len(nums)
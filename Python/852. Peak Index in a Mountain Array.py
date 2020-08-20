class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid-1]:
                r = mid
            elif nums[mid] < nums[mid+1]:
                l = mid
            else:
                return mid
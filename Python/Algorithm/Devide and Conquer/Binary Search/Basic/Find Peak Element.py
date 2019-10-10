class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) >> 1
            if nums[mid] < nums[mid - 1]:
                r = mid
            elif nums[mid] < nums[mid + 1]:
                l = mid
            else:
                return mid
        if nums[l] < nums[r]:
            return r
        else:
            return l
            
    '''         
	class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums or not len(nums):
            return None
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r-l) // 2
            if (mid == 0 or nums[mid] > nums[mid-1]) and (mid == n - 1 or nums[mid] > nums[mid+1]):
                return mid
            elif mid > 0 and nums[mid] < nums[mid-1]:
                r = mid - 1
            else:
                l = mid + 1
        return mid
     '''
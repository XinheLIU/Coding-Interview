class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
                # left is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid
            else:
                # right is sorted
                if nums[r] >= target > nums[mid]:
                    l = mid
                else:
                    r = mid
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1
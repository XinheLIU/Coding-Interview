#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k > len(nums) or k < 1:
            return None
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            pivot_idx = self.parition(nums, l, r)
            if pivot_idx == n - k:
                return nums[pivot_idx]
            elif pivot_idx > n - k:
                r = pivot_idx - 1
            else:
                l = pivot_idx + 1
        return nums[pivot_idx]


    def parition(self, nums, l, r):
        rand = random.randint(l, r)
        nums[rand], nums[r] = nums[r], nums[rand]
        i, pivot = l - 1, nums[r]
        for j in range(l, r):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[r] = nums[r], nums[i+1]
        return i+1
            
        
# @lc code=end


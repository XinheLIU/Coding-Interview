class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or k < 1 or k > len(nums):
            return None
        l, r, n = 0, len(nums) - 1, len(nums)
        while l <= r:
            pivot_pos = self.partition(nums, l, r)
            if pivot_pos == n - k:
                return nums[pivot_pos]
            elif pivot_pos < n - k:
                l = pivot_pos + 1
            else:
                r = pivot_pos - 1
                
   
    # quick sort
    def partition(self, nums, l, r):
        """
        make sure start <= k <= end
        compare the pivots position with k
        whether to repeat again 
        """
        i, pivot = l - 1, nums[r]
        for j in range(l,r):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[r] = nums[r], nums[i+1]
        return i + 1

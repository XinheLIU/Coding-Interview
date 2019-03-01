class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or k < 1 or k > len(nums):
            return None
        return self.partition(nums, 0, len(nums)-1, len(nums)-k) # the pivoting is from small to large
    
    # quick sort
    def partition(self, nums, start, end, k):
        """
        make sure start <= k <= end
        compare the pivots position with k
        whether to repeat again 
        """
        if start >= end:
            return nums[k]
        l, r = start, end
        pivot = nums[(l + r) // 2]
        while l <= r:
            while l <= r and nums[l] < pivot:
                l += 1
            while l <= r and nums[r] > pivot:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l +=1
                r -= 1
        if k <= r:
            return self.partition(nums, start, r, k)
        if k >= l:
            return self.partition(nums, l, end, k )
        return nums[k]class Solution(object):
  def sort(self, array):
    """
    input: int[] array
    return: int[]
    """
    # sort it in place
    for i in range(1, len(array)):
      cur, k = array[i], i
      while k > 0 and array[k-1] > cur:
        array[k] = array[k-1]
        k -= 1
      array[k] = cur
    return array
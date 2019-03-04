class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # key: compare mid and start 
        len_t = len(nums)
        if len_t == 0:
            return -1
        start, end = 0, len_t - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
        return min(nums[start],nums[end])
class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        start, end = 1, len(A) - 2  # len(A) and len(A-1) is also okay
        while start + 1 < end:
            mid = (start + end) >> 1
            if A[mid] < A[mid - 1]:
                end = mid
            elif A[mid] < A[mid + 1]:
                start = mid
            else:
                end = mid
        if A[start] < A[end]:
            return end
        else:
            return start 
    '''         
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums[-1] = nums[n] = -∞ is important
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) / 2
            if (mid == 0 or nums[mid] > nums[mid-1]) and \
            (mid == len(nums)-1 or nums[mid] > nums[mid+1]):
                return mid
            elif mid > 0 and nums[mid] < nums[mid-1]:
                right = mid - 1
            else:
                left = mid + 1
        return mid
     '''
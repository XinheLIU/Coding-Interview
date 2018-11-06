class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use binary search
        l, r = 1, len(nums) - 1
        while l < r:
            mid = (l + r) >> 1
            # count the numbers that <= mid 
            cnt = 0
            for num in nums: 
                if num <= mid:
                    cnt += 1
            if cnt <= mid:
                l = mid + 1
            else:
                r = mid
        return l
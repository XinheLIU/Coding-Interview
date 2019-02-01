class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or not len(nums):
            return 0
        lgth, last, maxl = 1, nums[0], 1
        for n in nums[1:]:
            if n > last:
                lgth += 1
                maxl = max(maxl, lgth)
            else:
                lgth = 1
            last = n
        return maxl
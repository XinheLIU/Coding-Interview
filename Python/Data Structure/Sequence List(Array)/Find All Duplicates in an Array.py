class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for i, num in enumerate(nums):
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] *= -1
            else:
                ret.append(abs(num))
        return ret
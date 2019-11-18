class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # do in place
        for num in nums:
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] *= -1 
        ret = []
        for i,num in enumerate(nums):
            if num > 0:
                ret.append(i+1)
        return ret

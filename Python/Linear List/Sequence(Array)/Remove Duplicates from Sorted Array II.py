class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i, j = 0, 0
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        return i + 1
        
class Solution(object):
    def removeDuplicates(self, nums):
        i, prev = 0, None
        for num in nums:
            if num == prev: continue
            prev = nums[i] = num
            i += 1
        return i
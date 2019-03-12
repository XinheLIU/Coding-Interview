class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)< 2:
            return len(nums)
        i, j, count = 0, 1, 1
        # count is the maximum allowed repeat 
        while j < len(nums):
            if nums[i] == nums[j] and count == 0:
                j += 1
            else:  
                if nums[i] == nums[j]:
                    count -= 1
                else:
                    count = 1
                i += 1
                nums[i] = nums[j]
                j += 1
        return i + 1


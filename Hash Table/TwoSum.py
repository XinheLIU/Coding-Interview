class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = dict()
        for i,num in enumerate(nums):
            if (target - num) in hash_table:
                return([ hash_table.get(target - num), i])
            hash_table[num] = i
        return None
            
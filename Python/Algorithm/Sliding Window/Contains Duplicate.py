class Solution:
    def containsDuplicate(self, nums: 'List[int]') -> 'bool':
        # we can use set very easily, or do sort or dictionary
        dict = {}
        for num in nums:
            if num in dict:
                return True
            else:
                dict[num] = 1
        return False
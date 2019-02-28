class Solution:
    def sortColors(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        # one-pass algo
        r, i, b = 0, 0, len(nums) - 1 # red, i, blue
        while i <= b:
            if nums[i] == 0 and r != i:
                nums[i], nums[r] = nums[r], nums[i]
                r += 1
            elif nums[i] == 2:
                nums[i], nums[b] = nums[b], nums[i]
                b -= 1
            else: 
                i += 1
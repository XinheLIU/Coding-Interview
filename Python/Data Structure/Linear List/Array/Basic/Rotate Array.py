class Solution:
	def rotate(self, nums, k):
        # Write your code here
        length = len(nums)
        k = k % length
        result = nums[length - k : length] + nums[:length - k]
        return result
        
'''
    def rotate(self, nums: 'List[int]', k: 'int') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        if not len(nums): return
        n, start = len(nums), 0
        while n and k % n:
            k %= n
            for i in range(k):
                nums[i + start], nums[n - k + i + start] = nums[n- k + i + start], nums[i + start]
            n -= k
            start += k
'''
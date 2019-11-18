class Solution:
    def rotate(self, nums: 'List[int]', k: 'int') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        n, start, i = len(nums), 0, 0
        k %= n
        if n == 0 or k == 0: return 
        cur = nums[0]
        for _ in range(n):
            i = (i + k) % n
            # save nums[i] as t, change t to be current 
            t = nums[i]
            nums[i] = cur
            if i == start: # one cycle is finished, move start
                start += 1
                i += 1
                cur = nums[i]
            else:
                cur = t
'''
class Solution:
    def rotate(self, nums: 'List[int]', k: 'int') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        if not len(nums): return
        n, start = len(nums), 0
        while n and k % n:
            k %= n
            for i in range(k):
                print(i+start, n - k + i + start)
                nums[i + start], nums[n - k + i + start] = nums[n- k + i + start], nums[i + start]
            n -= k
            start += k
'''
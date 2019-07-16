class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def threeSumSmaller(self, nums, target):
        # Write your code here
        ans = 0
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    ans += right-left
                    left += 1
                else:
                    right -= 1
        return ans
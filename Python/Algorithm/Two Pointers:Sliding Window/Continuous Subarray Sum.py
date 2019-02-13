class Solution:
    def checkSubarraySum(self, nums: 'List[int]', k: 'int') -> 'bool':
        if not nums: return False
        # use sliding windows
        for i in range(len(nums)):
            sum = nums[i]
            for j in range(i + 1, len(nums)):
                sum += nums[j]
                if sum == k:
                    return True
                elif k != 0 and sum % k == 0:
                    return True
        return False
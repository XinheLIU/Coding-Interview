class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0: return 0
        # dp[i] is longest subsequence ended with nums[i]
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return(max(dp))
        
'''
# O(NlogN) Solution
class Solution:
    def binary_search(self, list, a):
        l, r = 0, len(list) - 1
        while l < r:
            mid = l + ( r - l) // 2
            if list[mid] < a:
                l = mid + 1
            else:
                r = mid
        # l < a, r >= a
        return(r)
        
    def lengthOfLIS(self, nums):
        if not nums or not len(nums):
            return 0
        LIS = [nums[0]] # not true LIS, but length should be the same
        for n in nums:
            if n < LIS[0]:
                LIS[0] = n
            elif n > LIS[-1]:
                LIS.append(n)
            else:
                r = self.binary_search(LIS, n)
                LIS[r] = n  
        return(len(LIS))
'''
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # cumSum is a non-decreasing dp value, we dont let it decrease
        # if decrease, we prefer to start new
        cumsum, maxsum = 0, -float('inf')
        for n in nums:
            cumsum = max(cumsum + n, n)
            maxsum = max(maxsum, cumsum)
        return maxsum
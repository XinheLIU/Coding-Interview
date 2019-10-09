class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n, maxm = len(nums), float('-inf')
        if n < k:
            return sum(nums) / n
        summ = sum(nums[:k])
        maxm = max(maxm, summ)
        for i in range(k, n):
            summ = summ - nums[i-k] + nums[i]
            maxm = max(maxm, summ)
        return maxm / k
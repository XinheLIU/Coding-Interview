class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # if use max heap - will time out NlogK time
        # deque with indices in the queue
        if not nums:
            return []
        window, res = [],[]
        for i,x in enumerate(nums):
            # the left most (front) is the largest
            if i >= k and window[0] <= i - k:
                window.pop(0)
            while window and nums[window[-1]] <= x:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res
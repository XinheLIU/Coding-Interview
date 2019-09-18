class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # if use max heap - will time out NlogK time
        # deque with indices in the queue
        ret = []
        if not nums:
            return ret
        window = []
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i - k:
                window.pop(0)
            while window and nums[window[-1]] <= x:
                window.pop()
            window.append(i)
            if i >= k - 1:
                ret.append(nums[window[0]])
        return ret
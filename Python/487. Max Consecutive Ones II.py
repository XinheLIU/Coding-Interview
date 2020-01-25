class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret = 0
        l = 0
        K = 1
        zeros = 0
        q = collections.deque() # record the index of 0s
        for r, v in enumerate(nums):
            if v == 0:
                q.append(r)
                zeros += 1
            while zeros > K:
                l = q.popleft() + 1
                zeros -= 1
            ret = max(ret, r - l + 1)
        return ret      
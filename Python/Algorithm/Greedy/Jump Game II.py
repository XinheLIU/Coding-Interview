class Solution:
    # greedy
    def jump(self, nums: List[int]) -> int:
        cur = 0
        N = len(nums)
        count = 0
        pos = 0
        while cur < N - 1:
            count += 1
            pre = cur
            while pos <= pre:
                cur = max(cur, pos + nums[pos])
                pos += 1
        return count

"""
# dynamic programming

    def jump(self, nums: List[int]) -> int:
        p = [0]
        for i in range(len(nums) - 1):
            while(i + nums[i] >= len(p) and len(p) < len(nums)):
                p.append(p[i] + 1)
        return p[-1]
"""
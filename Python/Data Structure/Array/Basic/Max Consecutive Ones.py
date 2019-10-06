class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret, cnt = 0, 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                cnt = 0
            ret = max(ret, cnt)
        return ret
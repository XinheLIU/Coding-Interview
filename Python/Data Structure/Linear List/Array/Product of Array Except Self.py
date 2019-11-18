class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # cumprod array (till left)
        ret = [1] * n
        for i in range(1,n):
            ret[i] = nums[i-1] * ret[i-1]
        r = 1
        # reverse
        for i in range(n-1, -1, -1):
            ret[i] *= r
            r *= nums[i]
        return ret
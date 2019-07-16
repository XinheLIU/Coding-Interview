class Solution(object):
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, nums):
        nums.sort()
        ret = []
        length = len(nums)
        for i in range(0, len(nums) - 1):
            if nums[i] > 0:
                break
            target = 0 - nums[i]
            if i and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, length - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    ret.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l] + nums[r] > target:
                     r -= 1
                else:
                    l += 1
        return ret
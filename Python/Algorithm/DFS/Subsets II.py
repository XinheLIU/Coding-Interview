class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()
        self.helper(nums, 0, [])
        return self.res
      
    def helper(self, nums, start, out):
        self.res.append(out[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            out.append(nums[i])
            self.helper(nums, i + 1, out)
            out.pop()
            
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.helper(nums, 0, [])
        return self.res
      
    def helper(self, nums, start, out):
        self.res.append(out[:])
        for i in range(start, len(nums)):
            out.append(nums[i])
            self.helper(nums, i + 1, out)
            out.pop()
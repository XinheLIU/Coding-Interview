class Solution:
    """
    @param: nums: A set of numbers
    @return: A list of lists
    """
    def helper(self, out, nums, start):
        self.results.append(out)
        for i in range(start, len(nums)):
            self.helper(out + [nums[i]], nums, i + 1)
        
   
    def subsets(self, nums):
        self.results = []
        self.helper( [], sorted(nums), 0)
        return self.results
        
    """    
    def search(self, nums, S, index):
        if index == len(nums):
            self.results.append(S)
            return
        self.search(nums, S + [nums[index]], index + 1)
        self.search(nums, S, index + 1)
        
    def subsets(self, nums):
        self.results = []
        self.search(sorted(nums), [], 0)
        return self.results
    """    
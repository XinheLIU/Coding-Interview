class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result, flags = [], [False] * len(nums)
        self.getPermutation(nums, result, flags, [])

        return result

    def getPermutation(self, nums, result, flags, temp):
        if len(temp) == len(nums):
            result.append(temp[:])
            return

        for i in range(len(nums)):
            if flags[i]:
                continue
            flags[i] = True
            temp.append(nums[i])
            self.getPermutation(nums, result, flags, temp)
            temp.pop()
            flags[i] = False
'''
# DFS
def permute(self, nums):
    res = []
    self.dfs(nums, [], res)
    return res
    
def dfs(self, nums, path, res):
    if not nums:
        res.append(path)
        # return # backtracking
    for i in xrange(len(nums)):
        self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
'''
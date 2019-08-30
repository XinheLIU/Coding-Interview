class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, out, ret, visited):
            if len(out) == len(nums):
                ret.append(out[:])
            for i, v in enumerate(nums):
                if visited[i]:
                    continue
                else:
                    if (i > 0 and not visited[i-1] and nums[i] == nums[i-1]): 
                        continue
                    visited[i] = True
                    dfs(nums, out + [v], ret, visited)
                    visited[i] = False
        ret = []
        dfs(sorted(nums), [], ret, [False for _ in nums])
        return ret  


class Solution(object):
    # DFS
    def permuteUnique(self, nums):
        res, visited = [], [False]*len(nums)
        nums.sort()
        self.dfs(nums, visited, [], res)
        return res
    
    def dfs(self, nums, visited, path, res):
        if len(nums) == len(path):
            res.append(path)
            return 
        for i in xrange(len(nums)):
            if not visited[i]: 
                if not visited[i-1] and i>0 and nums[i] == nums[i-1]:  # here should pay attention
                    continue
                visited[i] = True
                self.dfs(nums, visited, path+[nums[i]], res)
                visited[i] = False
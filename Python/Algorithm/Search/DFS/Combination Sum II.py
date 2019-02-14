class Solution:
    def combinationSum2(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        self.res = []
        if not candidates or len(candidates) < 0: return self.res
        candidates.sort()
        self.helper([], candidates, target, 0)
        return self.res
    
    def helper(self, temp, candidates, target, start):
        if target == 0:
            self.res.append(temp[:])
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]: continue
            temp.append(candidates[i])
            self.helper(temp, candidates, target - candidates[i], i + 1)
            temp.pop()
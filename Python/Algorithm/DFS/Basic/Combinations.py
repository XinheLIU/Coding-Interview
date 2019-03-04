class Solution:
    def combine(self, n: 'int', k: 'int') -> 'List[List[int]]':   
        # write your code here  
        self.res = []
        self.dfs(n, k, 1, [])       
        return self.res

    def dfs(self, n, k, m, tmp):
        if k == len(tmp):
            self.res.append(tmp[:])
            return
        if len(tmp) > k:
            return
        for i in range(m, n+1):            
            tmp.append(i)            
            self.dfs(n, k, i+1, tmp)            
            tmp.pop()
        
class Solution:  
    # @param num, a list of integer  
    # @return a list of lists of integer  
    # a dfs problem  
    def dfs(self, res, val, num, start):  
        if val not in res:  
            res.append(val)  
        for i in range(start, len(num)):  
            self.dfs(res, val+[num[i]], num, i+1)  
            
    def subsetsWithDup(self, S):  
        res = []  
        if len(S) == 0:  
            return res  
        S.sort()  
        val = []  
        self.dfs(res, val, S, 0)  
        return res  
    """
    @param: nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    
    def subsetsWithDup(self, S):
        # write your code here
        S.sort()
        p = [[S[x] for x in range(len(S)) if i>>x&1] for i in range(2**len(S))]
        func = lambda x,y:x if y in x else x + [y]
        p = reduce(func, [[], ] + p)
        return list(reversed(p))
    """
        
        
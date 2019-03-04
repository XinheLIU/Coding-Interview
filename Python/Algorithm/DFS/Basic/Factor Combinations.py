class Solution(object):
  
  def dfs(self, n, subset, start):
    while start * start <= n:      
      if n % start == 0:
        self.result.append(subset + [start, n//start])
        self.dfs(n//start, subset + [start], start)        
      start += 1    
  
  def combinations(self, target):
    """
    input: int target
    return: int[][]
    """
    self.result = []
    self.dfs(target, [], 2)
    return self.result
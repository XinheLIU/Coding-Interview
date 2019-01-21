class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.list = []
        self._gen(n, 0, 0, "")
        return self.list
    
    def _gen(self, n, left, right, result):
        if left == n and right == n:
            self.list.append(result)
            return
        if left < n:
            self._gen(n, left + 1, right, result + "(")
        if right < n and right < left:
            self._gen(n, left, right + 1, result + ")")
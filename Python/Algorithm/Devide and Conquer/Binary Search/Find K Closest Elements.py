class Solution:
    def findClosestElements(self, A: 'List[int]', k: 'int', x: 'int') -> 'List[int]':
        left, right = 0, len(A) - k
        while left < right:
            mid = (left + right) // 2
            if x - A[mid] > A[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return A[left:left + k]
        
        
'''
class Solution(object):
    def closest(self, A, x):
        l, r = 0, len(A) - 1
        if r < 0:
            return -1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if A[mid] < x:
                l = mid
            elif A[mid] > x:
                r = mid
            else:
                return mid
        return l if abs(A[l] - x) < abs(A[r] - x) else r
    
    def kClosest(self, A, x, k):
        """
        input: int[] array, int target, int k
        return: int[]
        """
        res = []
        if not len(A) or k == 0: return res
        close = self.closest(A,x)
        res.append(A[close])
        l, r = close - 1, close + 1
        total = len(A)
        while len(res) < k and (l >= 0 or r < total):
            if r < total and (l < 0 or  abs(A[l] - x) > abs(A[r] - x)):
                res.append(A[r])
                r += 1
            elif l >= 0:
                res.append(A[l])
                l -= 1
        return res
'''
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        def iseven(num):
            return num % 2 == 0
        l, r = 0, len(A) - 1
        while l < r:
            m, n = A[l], A[r]
            if not iseven(m) and iseven(n):
                 A[l], A[r] = n, m
            elif not iseven(m):
                r -= 1
            elif iseven(n):
                l += 1
            else:
                l += 1
                r -= 1
        return A
          
#  return sorted(A, key=lambda x: x % 2)
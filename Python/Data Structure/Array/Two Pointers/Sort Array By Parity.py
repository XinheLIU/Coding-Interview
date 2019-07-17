class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l, r = 0, len(A) - 1
        while l < r:
            m, n = A[l], A[r]
            if m % 2 == 1 and n % 2 == 0:
                A[l], A[r] = n, m
            elif m % 2 == 1:
                r -= 1
            elif n % 2 == 0:
                l += 1
            else:
                l += 1
                r -= 1
        return A      
#  return sorted(A, key=lambda x: x % 2)
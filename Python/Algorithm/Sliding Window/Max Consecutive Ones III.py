class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        ret, zeros, left = 0, 0, 0
        for right, v in enumerate(A):
            if v == 0:
                zeros += 1
            # move left 
            while zeros > K:
                if A[left] == 0:
                    zeros -= 1
                left += 1
            ret = max(ret, right - left + 1)
        return ret
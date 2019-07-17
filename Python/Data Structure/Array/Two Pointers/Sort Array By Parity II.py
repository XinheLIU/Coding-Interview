class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        # two pointers
        j = 1
        for i in range(0, len(A), 2): #even
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A    
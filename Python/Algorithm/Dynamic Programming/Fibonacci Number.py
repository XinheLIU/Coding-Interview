class Solution:
    def fib(self, N: int) -> int:
        if N == 0: return 0
        x, y = 1, 1
        for i in range(2, N):
            x, y = x + y, x
        return x